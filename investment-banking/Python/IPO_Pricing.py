# ======================================================================
#  IPO PRICING (COMPARABLES) – BEGINNER EDITION
#  (charts saved in the SAME folder as the script)
# ======================================================================
#  WHAT THIS FILE DOES
#  -------------------
#  1. Ask you for a few numbers (inside the yellow fence)
#  2. Loads peer multiples (P/E, EV/EBITDA, etc.) – your choice
#  3. Takes the **median** multiple to avoid outlier bias
#  4. Applies an IPO discount (10-15 %) to entice new investors
#  5. Tells you the IPO price per share and money raised
#  6. Draws a simple bar chart (optional) – no extra packages
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
import numpy as np
import os
import datetime as dt

# ------------------------------------------------------------------
# 🟡🟡🟡  BEGINNER INPUTS – CHANGE ONLY HERE  🟡🟡🟡
# ------------------------------------------------------------------
COMPANY_NAME          = "DemoCo"
COMPANY_EBITDA_M      = 50        # Last 12-month EBITDA ($ M)
COMPANY_NET_INCOME_M  = 30        # Last 12-month net income ($ M)
SHARES_OUTSTANDING_M  = 10        # shares to be sold in IPO (millions)

# Peer multiples – add as many as you want, keep format (Name, Multiple)
PEERS_PE = {          # Price / Earnings
    "Peer A": 25.0,
    "Peer B": 22.0,
    "Peer C": 28.0,
    "Peer D": 24.0
}

PEERS_EBITDA = {       # Enterprise-Value / EBITDA (optional)
    "Peer A": 12.0,
    "Peer B": 11.0,
    "Peer C": 13.0,
    "Peer D": 12.5
}

IPO_DISCOUNT_PCT      = 0.15      # 15 % discount to fair value
SAVE_PLOTS            = True
OUTPUT_FOLDER         = "."       # "." = same folder as this script
# ------------------------------------------------------------------
# 🔴  STOP – do NOT edit below unless you want to learn Python
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# 1. HELPER: median without outliers
# ------------------------------------------------------------------
def median(vals):
    """Return median of a list or dict_values"""
    s = sorted(vals)
    n = len(s)
    return (s[n//2 - 1] + s[n//2]) / 2 if n % 2 == 0 else s[n//2]

# ------------------------------------------------------------------
# 2. CALCULATE MEDIAN MULTIPLES
#    💡NOTE: POLLING THE AUDIENCE
#    We're looking at the "neighbors" to see what the market
#    "temperature" is. Median avoids the "Crazy Neighbor" outlier.
# ------------------------------------------------------------------
median_pe = median(PEERS_PE.values())
median_ev_ebitda = median(PEERS_EBITDA.values())

print("\n"+"="*60)
print(f"{COMPANY_NAME}  IPO Pricing  ({dt.datetime.now().strftime('%Y-%m-%d')})")
print("="*60)
print("Peer Medians")
print(f"P/E:        {median_pe:.1f}×")
print(f"EV/EBITDA:  {median_ev_ebitda:.1f}×")

# ------------------------------------------------------------------
# 3. VALUATION USING P/E (change block if you prefer EV/EBITDA)
# ------------------------------------------------------------------
fair_equity_value = COMPANY_NET_INCOME_M * median_pe
fair_price_per_share = fair_equity_value / SHARES_OUTSTANDING_M
ipo_price_per_share = fair_price_per_share * (1 - IPO_DISCOUNT_PCT)
ipo_discount_amt = fair_price_per_share - ipo_price_per_share

# ------------------------------------------------------------------
# 4. MONEY RAISED
# ------------------------------------------------------------------
gross_proceeds = ipo_price_per_share * SHARES_OUTSTANDING_M

print("\nPricing Summary (P/E Method)")
print(f"Fair Equity Value:     ${fair_equity_value:,.0f} M")
print(f"Fair Price / Share:    ${fair_price_per_share:.2f}")
print(f"IPO Discount ({IPO_DISCOUNT_PCT:.0%}):      -${ipo_discount_amt:.2f}")
print("-" * 40)
print(f"RECOMMENDED IPO PRICE:  ${ipo_price_per_share:.2f}")
print(f"Gross Proceeds Raised:  ${gross_proceeds:,.0f} M")

# The Story
print(f"\n💡 INSIGHT: THE 'FIRST DATE' STRATEGY!")
print(f"   You're pricing at a {IPO_DISCOUNT_PCT:.0%} discount to fair value.")
print(f"   This creates a 'Day 1 Pop'—making your new shareholders happy.")
print(f"   Happy shareholders = future business and a strong IPO story.")

# ------------------------------------------------------------------
# 5. EXTRA INPUTS – safe places to add more detail
# ------------------------------------------------------------------
# 5a. Use EV/EBITDA instead → replicate block 3 with EV logic, subtract net debt
# 5b. Multiple metrics → average the P/E and EV/EBITDA answers (weight 50/50?)
# 5c. Different discounts → 10 % for hot market, 20 % for volatile sector
# 5d. More peers → just add lines inside PEERS_PE or PEERS_EBITDA dicts
# 5e. Forward earnings → replace COMPANY_NET_INCOME_M with forecast year+1
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# 6. PURE-MATPLOTLIB CHART (optional) – peer multiples bar chart
# ------------------------------------------------------------------
if SAVE_PLOTS:
    # 6a. Bar chart: peer P/E vs median
    plt.figure(figsize=(5,3))
    peers = list(PEERS_PE.keys())
    mults = list(PEERS_PE.values())
    plt.bar(peers + ["Median"], mults + [median_pe], color=["skyblue"]*len(peers) + ["darkblue"])
    plt.title("Peer P/E Multiples")
    plt.ylabel("P/E (×)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("peer_multiples_bar.png", dpi=150)
    plt.close()

print(f"\nChart saved → same folder as this script")
