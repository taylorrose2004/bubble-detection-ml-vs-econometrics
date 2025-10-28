import pandas as pd
from .utils import log_returns, rolling_vol, sma_ratio

def build_features(price: pd.Series, macro: pd.DataFrame = None) -> pd.DataFrame:
    """Create a basic feature set from prices (+ optional macro inputs).
    Features:
      - log returns
      - rolling volatility (21d)
      - SMA ratio (20/100)
    """
    df = pd.DataFrame(index=price.index.copy())
    df['price'] = price
    df['log_ret'] = log_returns(price)
    df['vol_21'] = df['price'].pct_change().rolling(21).std() * (252 ** 0.5)
    df['sma_ratio_20_100'] = sma_ratio(price, 20, 100)
    if macro is not None:
        macro = macro.reindex(df.index).ffill()
        for c in macro.columns:
            df[f"macro_{c}"] = macro[c]
    return df.dropna()
