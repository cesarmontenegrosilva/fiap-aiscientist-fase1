import pandas as pd

def categorize_nps(score: float) -> str:
    if score <= 6:
        return "Detrator"
    if score <= 8:
        return "Neutro"
    return "Promotor"

def load_and_prepare(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["nps_class"] = df["nps_score"].apply(categorize_nps)
    return df

def build_features(df: pd.DataFrame):
    drop_cols = ["nps_score", "nps_class", "customer_id", "order_id"]
    X = df.drop(columns=[c for c in drop_cols if c in df.columns])
    y = df["nps_score"]
    return X, y
