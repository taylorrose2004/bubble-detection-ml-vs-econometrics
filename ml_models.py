import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import classification_report, roc_auc_score
import joblib

def fit_random_forest(X: pd.DataFrame, y: pd.Series, n_splits: int = 5):
    tscv = TimeSeriesSplit(n_splits=n_splits)
    model = RandomForestClassifier(n_estimators=300, max_depth=None, random_state=42, n_jobs=-1)
    # Simple fit on full data; extend with CV/tuning if desired.
    model.fit(X, y)
    return model

def evaluate_classifier(model, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    proba = model.predict_proba(X_test)[:,1]
    preds = (proba >= 0.5).astype(int)
    return {
        "roc_auc": roc_auc_score(y_test, proba),
        "report": classification_report(y_test, preds, output_dict=True),
    }

def save_model(model, path: str):
    joblib.dump(model, path)
