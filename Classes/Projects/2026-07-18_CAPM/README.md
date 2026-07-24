# CAPM Return Calculator

A Streamlit web app that calculates and visualizes stock returns using the Capital Asset Pricing Model (CAPM), pulling live data from Yahoo Finance and FRED.

## What it does

- Lets you pick up to 4 stocks and a lookback period (1–10 years)
- Pulls historical closing prices via **yfinance**
- Pulls the S&P 500 series from **FRED** via `pandas_datareader` (no API key needed for this dataset)
- Shows raw and normalized closing prices, daily returns, and normalized daily returns as interactive Plotly charts
- Calculates each stock's **beta** (via linear regression against the S&P 500) and its **alpha**
- Computes expected return using the CAPM formula:

  `Expected Return = Risk-Free Rate + Beta * (Market Return - Risk-Free Rate)`

  (risk-free rate is currently set to 0 in the app)

## Files

- `capm_return.py` — main Streamlit app
- `capm_functions.py` — helper functions (plotting, normalization, daily return, beta calculation)

## Setup

1. Navigate to this folder:
   ```bash
   cd Classes/Projects/capm_analysis
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run capm_return.py
   ```

## Notes

- Built and tested on Arch Linux.
- No `.env` or API key setup needed — the FRED data used here (`sp500` series) is pulled through `pandas_datareader` without authentication.
- If you hit `command not found` errors after installing, double-check your virtual environment is activated (`which python` should point inside `venv/`).
