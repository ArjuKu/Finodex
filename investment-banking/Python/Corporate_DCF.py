# ======================================================================
#  BANK DCF TEMPLATE – BEGINNER EDITION
# ======================================================================
#  WHAT THIS FILE DOES
#  -------------------
#  1. Asks you for a few financial numbers (inside the yellow fence)
#  2. Projects 5 years of Free Cash Flow to Equity (FCFE)
#  3. Adds a "terminal value" for all cash flows after year 5
#  4. Discounts everything back to today's dollars
#  5. Tells you the implied share price and upside vs. current price
#  6. Draws two simple charts (no seaborn needed)
#
#  HOW TO USE
#  ----------
#  a) Install packages (only once):
#        pip install yfinance matplotlib pandas numpy
#  b) Scroll to the yellow fence below, change ONLY those numbers
#  c) Save file → run in VS Code terminal:  python filename.py
#
#  WANT MORE DETAIL?
#  -----------------
#  Search for "EXTRA INPUTS" in the code – comments show safe places
#  to add new lines (extra years, macro scenarios, etc.) without breaking
# ======================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import os
import datetime as dt

# ------------------------------------------------------------------
# 0. QUICK INSTALL CHECK (uncomment if you want to auto-install)
# ------------------------------------------------------------------
# import subprocess, sys
# for pkg in ['yfinance', 'matplotlib', 'pandas', 'numpy']:
#     subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg])

# ------------------------------------------------------------------
# 🟡🟡🟡  BEGINNER INPUTS – CHANGE ONLY HERE  🟡🟡🟡
# ------------------------------------------------------------------
# Company identity
TICKER                = "JPM"        # used to download beta & 10-Y Treasury
CURRENT_PRICE         = 45.00        # today's market price ($)
SHARES_OUTSTANDING_M  = 100          # shares in millions

# Starting income statement (all $ millions)
NET_INTEREST_INCOME_0 = 1_200
NON_INT_INCOME_0      = 400
OPERATING_EXPENSE_0   = 850
PROVISIONS_0          = 100
NET_INCOME_0          = 500

# Growth assumptions (decimal: 0.05 = 5 %)
REVENUE_GROWTH        = 0.05   # top-line growth
OPEX_GROWTH           = 0.04   # cost growth
PROVISION_GROWTH      = 0.03   # loan-loss provision growth
TERMINAL_GROWTH       = 0.03   # perpetual growth (≤ nominal GDP)

# Bank-specific plug (teaching simplification)
REGULATORY_CAP_PCT    = 0.03   # % of NI kept for regulatory capital
NET_BORROWING_ANNUAL  = 80      # positive = issuing debt, negative = pay-down

# Market data (set AUTO_* = False to lock your own number)
AUTO_RF               = True
AUTO_BETA             = True
HARDCODED_RF          = 0.045
HARDCODED_BETA        = 1.15
MARKET_RISK_PREMIUM   = 0.06   # equity risk premium (your choice)

# Output
SAVE_PLOTS            = True
OUTPUT_FOLDER         = "charts"
# ------------------------------------------------------------------
# 🔴  STOP – do NOT edit below unless you want to learn Python
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# 1. FETCH MARKET DATA (or fall back to hard-coded)
# ------------------------------------------------------------------
def get_rf() -> float:
    """Download 10-Year US Treasury yield from Yahoo; fallback if fail"""
    try:
        return yf.Ticker("^TNX").history(period="1d")["Close"].iloc[-1] / 100
    except Exception as e:
        print("Could not fetch 10-Y Treasury:", e, "- using hard-coded value")
        return HARDCODED_RF

def get_beta(ticker: str) -> float:
    """Download beta from Yahoo; fallback if fail"""
    try:
        return yf.Ticker(ticker).info.get("beta", HARDCODED_BETA)
    except Exception as e:
        print("Could not fetch beta:", e, "- using hard-coded value")
        return HARDCODED_BETA

risk_free = get_rf() if AUTO_RF else HARDCODED_RF
beta = get_beta(TICKER) if AUTO_BETA else HARDCODED_BETA
cost_of_eq = risk_free + beta * MARKET_RISK_PREMIUM

# ------------------------------------------------------------------
# 2. PROJECT 5-YEAR FCFE  (core DCF step 1)
#    FCFE = Net Income – regulatory capital – net borrowing
# ------------------------------------------------------------------
def project_five_year_fcfe():
    rows = []
    for year in range(1, 6):
        ni = NET_INCOME_0 * ((1 + REVENUE_GROWTH) ** year)
        reg_cap = ni * REGULATORY_CAP_PCT   # teaching plug
        fcfe = ni - reg_cap - NET_BORROWING_ANNUAL
        discount_factor = 1 / ((1 + cost_of_eq) ** year)
        rows.append({
            "Year": year,
            "Net Income": ni,
            "FCFE": fcfe,
            "PV": fcfe * discount_factor
        })
    return pd.DataFrame(rows)

proj_df = project_five_year_fcfe()

# ------------------------------------------------------------------
# 3. TERMINAL VALUE  (core DCF step 2)
#    Gordon Growth: TV = FCF in year-6 / (cost_of_eq – terminal_growth)
# ------------------------------------------------------------------
terminal_fcfe = proj_df.iloc[-1]["FCFE"] * (1 + TERMINAL_GROWTH)
terminal_value = terminal_fcfe / (cost_of_eq - TERMINAL_GROWTH)
terminal_pv = terminal_value * 1 / ((1 + cost_of_eq) ** 5)  # discount 5 yrs

# ------------------------------------------------------------------
# 4. ADD UP TODAY'S VALUE  (core DCF step 3)
# ------------------------------------------------------------------
pv_five = proj_df["PV"].sum()
enterprise_value = pv_five + terminal_pv
equity_value = enterprise_value                       # no net-debt adj for banks
implied_price = equity_value / SHARES_OUTSTANDING_M
upside_downside = (implied_price - CURRENT_PRICE) / CURRENT_PRICE

# ------------------------------------------------------------------
# 5. PRINT A HUMAN STORY
# ------------------------------------------------------------------
print("\n"+"="*60)
print(f"{TICKER}  Teaching DCF  ({dt.datetime.now().strftime('%Y-%m-%d')})")
print("="*60)
print(f"Cost of Equity: {cost_of_eq:.1%}  (rf={risk_free:.2%}  β={beta:.2f})")
print(proj_df.to_string(index=False, float_format="%.0f"))
print(f"\nPV FCFE yrs 1-5:  ${pv_five:,.0f}M")
print(f"PV Terminal:      ${terminal_pv:,.0f}M")
print(f"Implied Price:      ${implied_price:.2f}")
print(f"Current Price:      ${CURRENT_PRICE:.2f}")
print(f"Upside/(Downside):  {upside_downside:.1%}")

# ------------------------------------------------------------------
# 6. EXTRA INPUTS – safe places to add more detail
# ------------------------------------------------------------------
# 6a. More forecast years → change range(1, 6) to range(1, 11) and add
#     extra growth assumptions for years 6-10 (usually lower).
# 6b. Macro scenarios → duplicate the whole projection block with
#     different growth drivers (bull / base / bear).
# 6c. Monte-Carlo → replace growth & beta with random draws, run 10 k
#     loops, store implied_price each time → histogram.
# 6d. WACC for non-banks → add after-tax cost of debt, weights, etc.
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# 7. PURE-MATPLOTLIB PLOTS  (no seaborn needed)
# ------------------------------------------------------------------
if SAVE_PLOTS:
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # 7a. Bar chart: FCFE
    plt.figure(figsize=(5,3))
    plt.bar(proj_df["Year"], proj_df["FCFE"], color="royalblue")
    plt.title("Projected FCFE ($M)")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_FOLDER}/fcfe_bar.png", dpi=150)
    plt.close()

    # 7b. Cumulative PV
    plt.figure(figsize=(5,3))
    cum_pv = proj_df["PV"].cumsum()
    plt.plot(proj_df["Year"], cum_pv, marker="o", color="darkgreen", label="PV cum.")
    plt.axhline(equity_value, ls="--", color="grey", label="Total PV")
    plt.title("Cumulative PV Build-up")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_FOLDER}/pv_cumul.png", dpi=150)
    plt.close()

    # 7c. Sensitivity heat-map (plain matplotlib)
    fig, ax = plt.subplots(figsize=(5,4))
    g_vals = [0.02, 0.025, TERMINAL_GROWTH, 0.035, 0.04]
    r_vals = [cost_of_eq-0.02, cost_of_eq-0.01, cost_of_eq, cost_of_eq+0.01, cost_of_eq+0.02]
    data = []
    for g in g_vals:
        row = []
        for r in r_vals:
            tv = (proj_df.iloc[-1]["FCFE"]*(1+g))/(r-g)
            ev = pv_five + tv * 1/((1+cost_of_eq)**5)
            row.append(ev/SHARES_OUTSTANDING_M)
        data.append(row)

    im = ax.imshow(data, cmap="RdYlGn", aspect="auto")
    # labels
    ax.set_xticks(range(len(r_vals))); ax.set_xticklabels([f"{r:.1%}" for r in r_vals])
    ax.set_yticks(range(len(g_vals))); ax.set_yticklabels([f"{g:.1%}" for g in g_vals])
    ax.set_xlabel("Cost of Equity"); ax.set_ylabel("Terminal Growth")
    ax.set_title("Implied Price Sensitivity")

    # annotate cells
    for i in range(len(g_vals)):
        for j in range(len(r_vals)):
            ax.text(j, i, f"{data[i][j]:.1f}", ha="center", va="center", fontsize=8)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_FOLDER}/sensitivity_plain.png", dpi=150)
    plt.show()
