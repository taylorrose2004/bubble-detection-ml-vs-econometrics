from src.gsadf import run_gsadf
import pandas as pd

def test_gsadf_runs():
    idx = pd.date_range('2000-01-01', periods=120, freq='M')
    s = pd.Series(range(1,121), index=idx, dtype='float')
    res = run_gsadf(s)
    assert hasattr(res, 'bubble_periods')
