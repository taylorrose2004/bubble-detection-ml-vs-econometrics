# Early Detection of Financial Bubbles using GSADF and Machine Learning

**Repo goal:** Compare early-warning power of the GSADF econometric test versus Machine Learning (Random Forest / XGBoost) across the Dot‑com bubble, the 2008 GFC, and crypto bubbles.

## Quickstart
```bash
pip install -r requirements.txt
jupyter notebook
# open notebooks/01-data-prep.ipynb
```

## Repository Structure
```
data/
  raw/            # place CSVs here (sp500.csv, ftse100.csv, btc_usd.csv, macro_data.csv)
  processed/
notebooks/
  01-data-prep.ipynb
  02-gsadf-analysis.ipynb
  03-ml-bubble-detection.ipynb
  04-performance-evaluation.ipynb
  05-visualization-results.ipynb
results/
  charts/
  model_outputs/
paper-summary/
  report.md
  figures/
src/
  gsadf.py
  feature_engineering.py
  ml_models.py
  backtesting.py
  utils.py
tests/
  test_gsadf.py
  test_ml_models.py
```

## Data Sources (suggested)
- Equity indices: S&P 500, FTSE 100
- Crypto: BTC/USD
- Macro: interest rates, CPI, GDP (e.g., FRED/World Bank/IMF)

> Replace placeholder CSVs in `data/raw/` with real series. The starter notebook can generate synthetic data so the pipeline runs end-to-end.

## Methods
- **GSADF**: Phillips, Shi & Yu (2015) test for explosive behavior and bubble dating.
- **ML**: Random Forest (primary), XGBoost (optional) trained on engineered features and GSADF-derived labels.

## Outputs
- Bubble dating tables and GSADF statistics
- ML classification metrics (precision, recall, AUC)
- Lead-time comparisons: how early did each method signal before major drawdowns?

## License
MIT
