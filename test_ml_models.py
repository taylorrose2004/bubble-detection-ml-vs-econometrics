from src.ml_models import fit_random_forest
import pandas as pd
import numpy as np

def test_rf_fit():
    idx = pd.date_range('2010-01-01', periods=200, freq='D')
    X = pd.DataFrame({
        'a': np.random.randn(len(idx)),
        'b': np.random.randn(len(idx))
    }, index=idx)
    y = pd.Series((X['a'] + 0.2*X['b'] > 0).astype(int), index=idx)
    model = fit_random_forest(X, y)
    assert hasattr(model, 'predict_proba')
