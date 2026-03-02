# ======================================================================
#  LBO TEACHING TEMPLATE – BEGINNER EDITION
#  (charts saved in the SAME folder as the script)
# ======================================================================
#  WHAT THIS FILE DOES
#  -------------------
#  1. Ask you for a few numbers (inside the yellow fence)
#  2. Builds a 5-year forecast: EBITDA → cash → debt pay-down
#  3. Sells the company at the same EBITDA-multiple (or different)
#  4. Tells you how much money the equity investor makes (IRR & MoM)
#  5. Drops two charts **right next to this file** (no sub-folder hunting)
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
# 🟡🟡🟡  BEGINNER INPUTS – CHANGE ONLY HERE  🟡🟡🟡
# ------------------------------------------------------------------
COMPANY_NAME          = "DemoCo"
PURCHASE_EV_M         = 1000     # Enterprise Value paid ($ millions)
ENTRY_EBITDA_M        = 200       # LTM EBITDA at purchase

# Capital structure
DEBT_PCT              = 0.70      # 70 % debt, 30 % equity

# Forecast drivers
EBITDA_GROWTH         = 0.05      # 5 % per year
INTEREST_RATE         = 0.08      # 8 % coupon on debt
TAX_RATE              = 0.21      # 21 % corporate tax
CAPEX_PCT_OF_EBITDA   = 0.25      # simple plug for capex
EXIT_MULTIPLE         = 5.0         # same as entry multiple (change if you want)

# Output
SAVE_PLOTS            = True
OUTPUT_FOLDER         = "."         # "." = same folder as this .py file
# ------------------------------------------------------------------
# 🔴  STOP – do NOT edit below unless you want to learn Python
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# 1. BUILD THE DEAL AT CLOSING
# ------------------------------------------------------------------
debt_at_close = PURCHASE_EV_M * DEBT_PCT
equity_at_close = PURCHASE_EV_M - debt_at_close
entry_multiple = PURCHASE_EV_M / ENTRY_EBITDA_M

print("\n"+"="*60)
print(f"{COMPANY_NAME}  LBO  ({dt.datetime.now().strftime('%Y-%m-%d')})")
print("="*60)
print(f"Purchase EV:     ${PURCHASE_EV_M:,.0f} M  @ {entry_multiple:.1f}× EBITDA")
print(f"Debt:            ${debt_at_close:,.0f} M  ({DEBT_PCT:.0%})")
print(f"Equity:          ${equity_at_close:,.0f} M  ({1-DEBT_PCT:.0%})")

# ------------------------------------------------------------------
# 2. 5-YEAR FORECAST – EBITDA → CASH → DEBT PAYDOWN
# ------------------------------------------------------------------
forecast = []
ebitda = ENTRY_EBITDA_M
debt = debt_at_close

for year in range(1, 6):
    ebitda *= (1 + EBITDA_GROWTH)                    # grow top-line
    interest = debt * INTEREST_RATE                  # cash interest
    tax = max(0, (ebitda - interest)) * TAX_RATE    # tax shield
    capex = ebitda * CAPEX_PCT_OF_EBITDA             # simplistic capex
    cash_paydown = ebitda - interest - tax - capex  # free cash left
    debt -= cash_paydown                             # amortise debt
    forecast.append({
        "Year": year,
        "EBITDA": ebitda,
        "Interest": interest,
        "Tax": tax,
        "Capex": capex,
        "Cash Paydown": cash_paydown,
        "Debt End": max(debt, 0)
    })

forecast_df = pd.DataFrame(forecast)

# print the amortisation table
print("\n5-Year Debt Amortisation ($ M)")
print(forecast_df.to_string(index=False, float_format="%.0f"))

# ------------------------------------------------------------------
# 3. EXIT VALUATION – sell at same multiple
# ------------------------------------------------------------------
exit_ebitda = forecast_df.iloc[-1]["EBITDA"]
exit_ev = exit_ebitda * EXIT_MULTIPLE
exit_equity_value = exit_ev - forecast_df.iloc[-1]["Debt End"]

# ------------------------------------------------------------------
# 4. RETURNS TO EQUITY INVESTOR
# ------------------------------------------------------------------
mom = exit_equity_value / equity_at_close
irr = (mom ** (1/5)) - 1

print("\nExit Summary")
print(f"Exit EV:           ${exit_ev:,.0f} M")
print(f"Less Debt:        -${forecast_df.iloc[-1]['Debt End']:,.0f} M")
print(f"Exit Equity:       ${exit_equity_value:,.0f} M")
print(f"Multiple of Money:  {mom:.2f}×")
print(f"IRR (5-yr hold):     {irr*100:.1f}%")

# ------------------------------------------------------------------
# 5. PURE-MATPLOTLIB CHARTS (saved in SAME folder)
# ------------------------------------------------------------------
if SAVE_PLOTS:
    # 5a. Debt balance over time
    plt.figure(figsize=(5,3))
    plt.plot(forecast_df["Year"], forecast_df["Debt End"], marker="o", color="darkred")
    plt.title("Debt Balance Amortisation")
    plt.ylabel("$ M")
    plt.tight_layout()
    plt.savefig("debt_amort.png", dpi=150)
    plt.close()

    # 5b. Cash-flow waterfall (stacked bars)
    plt.figure(figsize=(6,3))
    bottom = np.zeros(5)
    plt.bar(forecast_df["Year"], forecast_df["Cash Paydown"], label="Cash to Debt", bottom=bottom, color="royalblue")
    bottom += forecast_df["Cash Paydown"]
    plt.bar(forecast_df["Year"], forecast_df["Tax"], label="Tax", bottom=bottom, color="orange")
    bottom += forecast_df["Tax"]
    plt.bar(forecast_df["Year"], forecast_df["Capex"], label="Capex", bottom=bottom, color="grey")
    plt.title("Cash-Flow Waterfall")
    plt.ylabel("$ M")
    plt.legend()
    plt.tight_layout()
    plt.savefig("cash_waterfall.png", dpi=150)
    plt.close()

print(f"\nCharts saved → same folder as this script")
