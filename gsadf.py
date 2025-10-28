# Placeholder GSADF implementation hooks.
# For production, implement the recursive right-tailed ADF with expanding/shrinking windows,
# bootstrap critical values, and dating algorithm per Phillips, Shi & Yu (2015).

import pandas as pd
from dataclasses import dataclass

@dataclass
class GSADFResult:
    sup_adf: float
    critical_95: float
    bubble_periods: list  # list of (start_date, end_date)

def run_gsadf(price: pd.Series, min_window: int = 36) -> GSADFResult:
    # TODO: implement full GSADF. For now, return a dummy structure to keep the pipeline working.
    # Replace this with a real implementation or a call to a dedicated econometrics package.
    return GSADFResult(sup_adf=0.0, critical_95=0.0, bubble_periods=[])
