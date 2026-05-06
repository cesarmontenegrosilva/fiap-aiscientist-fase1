from pathlib import Path
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from data_prep import load_and_prepare, build_features

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "raw" / "desafio_nps_fase_1.csv"
MODELS_DIR = ROOT / "models"
REPORTS_DIR = ROOT / "reports" / "tables"
MODELS_DIR.mkdir(exist_ok=True, parents=True)
REPORTS_DIR.mkdir(exist_ok=True, parents=True)

def evaluate(y_true, y_pred):
    return {
        "MAE": mean_absolute_error(y_true, y_pred),
        "RMSE": mean_squared_error(y_true, y_pred) ** 0.5,
        "R2": r2_score(y_true, y_pred),
    }

def main():
    df = load_and_prepare(DATA_PATH)
    X, y = build_features(df)
    cat_cols = X.select_dtypes(include="object").columns.tolist()
    num_cols = [c for c in X.columns if c not in cat_cols]

    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
        ("num", StandardScaler(), num_cols),
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    candidates = {
        "Ridge Regression": Pipeline([("preprocess", preprocessor), ("model", Ridge(alpha=1.0))]),
        "Random Forest Regressor": Pipeline([("preprocess", preprocessor), ("model", RandomForestRegressor(n_estimators=250, min_samples_leaf=5, random_state=42, n_jobs=-1))]),
        "Gradient Boosting Regressor": Pipeline([("preprocess", preprocessor), ("model", GradientBoostingRegressor(random_state=42))]),
    }

    rows = []
    fitted = {}
    for name, model in candidates.items():
        model.fit(X_train, y_train)
        pred = np.clip(model.predict(X_test), 0, 10)
        rows.append({"modelo": name, **evaluate(y_test, pred)})
        fitted[name] = model

    quantile_models = {}
    for q in [0.10, 0.50, 0.90]:
        q_model = Pipeline([
            ("preprocess", preprocessor),
            ("model", GradientBoostingRegressor(loss="quantile", alpha=q, random_state=42)),
        ])
        q_model.fit(X_train, y_train)
        quantile_models[q] = q_model

    pred_q10 = np.clip(quantile_models[0.10].predict(X_test), 0, 10)
    pred_q50 = np.clip(quantile_models[0.50].predict(X_test), 0, 10)
    pred_q90 = np.clip(quantile_models[0.90].predict(X_test), 0, 10)
    rows.append({
        "modelo": "Quantile Regression - mediana (q=0.50)",
        **evaluate(y_test, pred_q50),
        "Cobertura_Intervalo_80pct": ((y_test >= pred_q10) & (y_test <= pred_q90)).mean(),
    })

    metrics = pd.DataFrame(rows).sort_values("MAE")
    metrics.to_csv(REPORTS_DIR / "metricas_modelos.csv", index=False)

    best_name = metrics.iloc[0]["modelo"]
    best_model = fitted.get(best_name, fitted["Ridge Regression"])
    joblib.dump(best_model, MODELS_DIR / "modelo_regressao_nps.pkl")
    joblib.dump(quantile_models, MODELS_DIR / "modelos_regressao_quantilica.pkl")
    print(metrics)

if __name__ == "__main__":
    main()
