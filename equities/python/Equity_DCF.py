# ======================================================================
#  EQUITY DCF (FCFE) – BEGINNER EDITION
#  (chart saved in the SAME folder as the script)
# ======================================================================
#  WHAT THIS FILE DOES
#  -------------------
#  1. Ask you for a few numbers (inside the yellow fence)
#  2. Projects 5-year Free Cash Flow to Equity (FCFE)
#  3. Adds a terminal value (Gordon growth) for all cash after year 5
#  4. Discounts everything back to today's dollars
#  5. Tells you the **intrinsic share price** and **margin of safety**
#  6. Draws a tiny bar chart (optional) – no seaborn needed
#
#  HOW TO USE
#  ----------
#  a) Install packages (only once):
#        pip install yfinance matplotlib pandas numpy
#  b) Scroll to the yellow fence, change ONLY those numbers
#  c) Save file → run in VS Code terminal:  python filename.py
# ======================================================================

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
import os
import datetime as dt

# ------------------------------------------------------------------
#  REAL-WORLD REFERENCE RANGES (for beginners)
#  ------------------------------------------------------------------
#  Risk-Free Rate (10-Y US Treasury)
#      Normal times:  2 % – 4 %
#      2022-2024:     4 % – 5 %
#      Crisis / ZIRP: 0 % – 1 %
#
#  Market Risk Premium (Rm – Rf)
#      US large-cap:  4 % – 6 %
#      Emerging mkts: 6 % – 8 %
#      Conservative:  5 %
#
#  Beta
#      Defensive utilities: 0.3 – 0.7
#      Market average:        1.0
#      Growth tech:         1.2 – 2.0
#      Penny stocks:        > 2.5
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# 🟡🟡🟡  BEGINNER INPUTS – CHANGE ONLY HERE  🟡🟡🟡
# ------------------------------------------------------------------
COMPANY_NAME          = "DemoCo"
CURRENT_SHARE_PRICE   = 45.00        # today's market price ($)
SHARES_OUTSTANDING_M  = 100           # shares in millions

# Starting income statement (last 12 months, $ millions)
NET_INCOME_0          = 100
DEPRECIATION_0        = 30
CAPEX_0               = 25
CHANGE_NWC_0          = 10
NET_BORROWING_0       = 0             # positive = new debt, negative = pay-down

# Growth & discount assumptions
NET_INCOME_GROWTH     = 0.08          # 8 % per year
TERMINAL_GROWTH       = 0.03          # perpetual GDP-style growth (≤ 4 %)

# Market data (set AUTO_* = False to lock your own number)
AUTO_RF               = True          # download 10-Y Treasury?
AUTO_BETA             = True          # download beta from Yahoo?
HARDCODED_RF          = 0.045
HARDCODED_BETA        = 1.0
MARKET_RISK_PREMIUM   = 0.06          # equity risk premium (your choice)

# Output
SAVE_PLOTS            = True
OUTPUT_FOLDER         = "."             # "." = same folder as this script
# ------------------------------------------------------------------
# 🔴  STOP – do NOT edit below unless you want to learn Python
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# 1. FETCH LIVE DATA (or fall back to hard-coded)
# ------------------------------------------------------------------
def get_rf() -> float:
    """Download 10-Year US Treasury yield; fallback if fail"""
    try:
        return yf.Ticker("^TNX").history(period="1d")["Close"].iloc[-1] / 100
    except Exception as e:
        print("Could not fetch 10-Y Treasury:", e, "- using hard-coded value")
        return HARDCODED_RF

def get_beta(ticker: str) -> float:
    """Download beta from Yahoo; fallback if fail"""
    try:
        info = yf.Ticker(ticker).info
        return info.get("beta", HARDCODED_BETA)
    except Exception as e:
        print("Could not fetch beta:", e, "- using hard-coded value")
        return HARDCODED_BETA

# Use live or hard-coded values
rf = get_rf() if AUTO_RF else HARDCODED_RF
beta_used = get_beta(COMPANY_NAME) if AUTO_BETA else HARDCODED_BETA
cost_of_equity = rf + beta_used * MARKET_RISK_PREMIUM

# ------------------------------------------------------------------
# 2. PROJECT 5-YEAR FCFE  (core DCF step 1)
#    FCFE = Net Income + Depreciation – Capex – ΔWorking-Capital + Net Borrowing
# ------------------------------------------------------------------
def project_five_year_fcfe():
    rows = []
    ni = NET_INCOME_0
    dep = DEPRECIATION_0
    capex = CAPEX_0
    d_nwc = CHANGE_NWC_0
    net_borr = NET_BORROWING_0

    for year in range(1, 6):
        # grow line items
        ni *= (1 + NET_INCOME_GROWTH)
        dep *= (1 + NET_INCOME_GROWTH)      # simplistic: grow with NI
        capex *= (1 + NET_INCOME_GROWTH)
        d_nwc *= (1 + NET_INCOME_GROWTH)
        # FCFE formula
        fcfe = ni + dep - capex - d_nwc + net_borr
        # discount factor
        df = 1 / ((1 + cost_of_equity) ** year)
        rows.append({
            "Year": year,
            "Net Income": ni,
            "FCFE": fcfe,
            "PV": fcfe * df
        })
    return pd.DataFrame(rows)

proj_df = project_five_year_fcfe()

# print the forecast
print("\n5-Year FCFE Forecast ($ M)")
print(proj_df.to_string(index=False, float_format="%.0f"))

# ------------------------------------------------------------------
# 3. TERMINAL VALUE  (core DCF step 2)
#    Gordon Growth: TV = FCF in year-6 / (cost_of_equity – terminal_growth)
# ------------------------------------------------------------------
terminal_fcfe = proj_df.iloc[-1]["FCFE"] * (1 + TERMINAL_GROWTH)
terminal_value = terminal_fcfe / (cost_of_equity - TERMINAL_GROWTH)
terminal_pv = terminal_value * 1 / ((1 + cost_of_equity) ** 5)

# ------------------------------------------------------------------
# 4. ADD UP TODAY'S VALUE  (core DCF step 3)
# ------------------------------------------------------------------
pv_five = proj_df["PV"].sum()
equity_value = pv_five + terminal_pv
intrinsic_share_price = equity_value / SHARES_OUTSTANDING_M
margin_of_safety = (intrinsic_share_price - CURRENT_SHARE_PRICE) / intrinsic_share_price

# ------------------------------------------------------------------
# 5. PRINT A HUMAN STORY
# ------------------------------------------------------------------
print("\n"+"="*60)
print(f"Equity DCF – {COMPANY_NAME}  ({dt.datetime.now().strftime('%Y-%m-%d')})")
print("="*60)
print(f"Cost of Equity: {cost_of_equity:.1%}  (rf={rf:.2%}  β={beta_used:.2f})")
print(f"Current Price:  ${CURRENT_SHARE_PRICE:.2f}")
print(f"Intrinsic Price:${intrinsic_share_price:.2f}")
print(f"Margin of Safety: {margin_of_safety*100:.1f}%")

# ------------------------------------------------------------------
# 6. SIMPLE IF-VERDICT BASED ON MARGIN OF SAFETY
# ------------------------------------------------------------------
if margin_of_safety > 0.20:
    verdict = "UNDervalued – potential BUY (margin > 20 %)."
elif margin_of_safety > 0.05:
    verdict = "FAIR value – within 5-20 % band."
else:
    verdict = "OVERvalued – potential SELL (or wait for better entry)."
print(f"Verdict: {verdict}")

# ------------------------------------------------------------------
# 7. EXTRA INPUTS – safe places to add more detail
# ------------------------------------------------------------------
# 7a. More forecast years → change range(1, 6) to range(1, 11) and add
#     extra growth drivers for years 6-10 (usually lower).
# 7b. Different terminal growth → set TERMINAL_GROWTH = 0.02 for slow utility
# 7c. Country risk → add +0.02 to MARKET_RISK_PREMIUM for emerging market
# 7d. Management options → dilute SHARES_OUTSTANDING_M by option pool
# 7e. Scenario analysis → duplicate the whole projection block with
#     bull / base / bear drivers (lower/higher growth, higher/lower beta)
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# 8. PURE-MATPLOTLIB CHART (optional) – intrinsic vs current price
# ------------------------------------------------------------------
if SAVE_PLOTS:
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # 8a. Bar chart: current vs intrinsic price
    plt.figure(figsize=(3,3))
    labels = ["Current Price", "Intrinsic Price"]
    prices = [CURRENT_SHARE_PRICE, intrinsic_share_price]
    colors = ["orange", "green"]
    plt.bar(labels, prices, color=colors)
    plt.ylabel("$ per Share")
    plt.title("Price Comparison")
    plt.tight_layout()
    plt.savefig("price_comparison.png", dpi=150)
    plt.close()

print(f"\nChart saved → same folder as this script") 
