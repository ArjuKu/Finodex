# ======================================================================
#  CAPM CALCULATOR – BEGINNER EDITION
#  (chart saved in the SAME folder as the script)
# ======================================================================
#  WHAT THIS FILE DOES
#  -------------------
#  1. Ask you for a few numbers (inside the yellow fence)
#  2. Downloads live 10-Y Treasury yield (optional) and beta (optional)
#  3. Calculates required return:  Rf + β × (Rm – Rf)
#  4. Prints a human sentence: "You should expect at least X % per year"
#  5. Draws a tiny bar chart (optional) – no seaborn needed
#
#  HOW TO USE
#  ----------
#  a) Install packages (only once):
#        pip install yfinance matplotlib numpy
#  b) Scroll to the yellow fence, change ONLY those numbers
#  c) Save file → run in VS Code terminal:  python filename.py
# ======================================================================

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
#      Conservative:    5 %
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
BETA                  = 1.25      # stock volatility vs market (>1 = aggressive)

# Market data (set AUTO_* = False to lock your own number)
AUTO_RF               = True      # download 10-Y Treasury?
AUTO_BETA             = True      # download beta from Yahoo?
HARDCODED_RF          = 0.045     # 4.5 % if download fails
HARDCODED_BETA        = 1.25
MARKET_RISK_PREMIUM   = 0.06      # historical equity premium (your choice)

# Output
SAVE_PLOTS            = True
OUTPUT_FOLDER         = "."        # "." = same folder as this script
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
beta_used = get_beta(COMPANY_NAME) if AUTO_BETA else BETA

# ------------------------------------------------------------------
# 2. CAPM FORMULA – core of the whole script
#    Required Return = Risk-Free Rate + Beta × Market Risk Premium
# ------------------------------------------------------------------
required_return = rf + beta_used * MARKET_RISK_PREMIUM

# ------------------------------------------------------------------
# 3. HUMAN STORY
# ------------------------------------------------------------------
print("\n"+"="*60)
print(f"CAPM Calculator – {COMPANY_NAME}  ({dt.datetime.now().strftime('%Y-%m-%d')})")
print("="*60)
print(f"Risk-Free Rate (10-Y Treasury):  {rf*100:.2f}%")
print(f"Beta (vs. market):              {beta_used:.2f}")
print(f"Market Risk Premium:            {MARKET_RISK_PREMIUM*100:.2f}%")
print("-" * 40)
print(f"REQUIRED RETURN (Cost of Equity):  {required_return*100:.2f}%")

# ------------------------------------------------------------------
# 4. INTERPRETATION – one-sentence English
# ------------------------------------------------------------------
if beta_used < 1.0:
    risk_words = "lower risk than the market (defensive)"
elif beta_used == 1.0:
    risk_words = "same risk as the market"
else:
    risk_words = "higher risk than the market (aggressive)"

print(f"\nBeta of {beta_used} means {COMPANY_NAME} is {risk_words}.")
print(f"You should therefore expect at least {required_return*100:.1f}% per year")
print("to compensate for that extra risk.")

# ------------------------------------------------------------------
# 5. SIMPLE IF-VERDICT BASED ON REQUIRED RETURN
# ------------------------------------------------------------------
if required_return < 0.07:
    verdict = "LOW required return – defensive, bond-like stock."
elif required_return < 0.10:
    verdict = "MODERATE required return – typical large-cap equity."
else:
    verdict = "HIGH required return – aggressive / high-beta stock."
print(f"Verdict: {verdict}")

# ------------------------------------------------------------------
# 6. EXTRA INPUTS – safe places to add more detail
# ------------------------------------------------------------------
# 6a. Different risk-free proxy → replace ^TNX with ^FVX (5-Y) or ^IRX (3-M)
# 6b. Country risk premium → add +0.02 to MARKET_RISK_PREMIUM for EM
# 6c. Forward beta → use forecast β from Bloomberg or Yahoo
# 6d. Multi-factor model → add size premium, industry premium, etc.
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# 7. PURE-MATPLOTLIB CHART (optional) – beta vs required return
# ------------------------------------------------------------------
if SAVE_PLOTS:
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # 7a. Bar chart: beta vs required return
    plt.figure(figsize=(4,3))
    labels = ["Risk-Free", "Market", COMPANY_NAME]
    returns = [rf*100, (rf + MARKET_RISK_PREMIUM)*100, required_return*100]
    colors = ["green", "blue", "red"]
    plt.bar(labels, returns, color=colors)
    plt.ylabel("Annual Return (%)")
    plt.title("Required Return Comparison")
    plt.tight_layout()
    plt.savefig("capm_bar.png", dpi=150)
    plt.close()

print(f"\nChart saved → same folder as this script") 
