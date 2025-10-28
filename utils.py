import pandas as pd
import numpy as np

def ensure_datetime_index(df: pd.DataFrame, date_col: str = None) -> pd.DataFrame:
    if date_col and date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col])
        df = df.set_index(date_col).sort_index()
    elif not isinstance(df.index, pd.DatetimeIndex):
        raise ValueError("DataFrame must have a DatetimeIndex or provide date_col.")
    return df

def log_returns(series: pd.Series) -> pd.Series:
    return np.log(series).diff()

def rolling_vol(series: pd.Series, window: int = 21) -> pd.Series:
    return series.pct_change().rolling(window).std() * np.sqrt(252)

def sma_ratio(series: pd.Series, fast: int = 20, slow: int = 100) -> pd.Series:
    return series.rolling(fast).mean() / series.rolling(slow).mean()
