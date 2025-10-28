import pandas as pd

def label_from_bubble_periods(index, bubble_periods):
    """Create a binary label Series indexed to `index` with 1 during bubble periods."""
    y = pd.Series(0, index=index)
    for start, end in bubble_periods:
        y.loc[start:end] = 1
    return y.astype(int)

def compute_lead_time(signal_series: pd.Series, crash_dates: list, lookahead_days: int = 60):
    """Compute lead times: days the signal was active before a crash date."""
    results = []
    for crash in crash_dates:
        active_window = signal_series.loc[:crash].tail(lookahead_days)
        days_active = (active_window > 0).sum()
        results.append({"crash_date": crash, "lead_days": int(days_active)})
    return pd.DataFrame(results)
