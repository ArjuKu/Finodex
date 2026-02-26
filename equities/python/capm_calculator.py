"""
CAPM CALCULATOR (Risk vs. Reward)
==================================
The Capital Asset Pricing Model (CAPM) calculates the required return 
for a stock based on its risk level.

HOW TO USE:
-----------
1. Edit the 'INPUTS' section with market data.
2. Run the script to see the 'Cost of Equity' (required return).
"""

def calculate_capm():
    # --- INPUTS ---
    print("--- 1. MARKET DATA INPUTS ---")
    # REPLACE WITH THE COMPANY YOU ARE EVALUATING
    company_name = "[ENTER COMPANY NAME]"
    
    risk_free_rate = 0.045        # 10-Year US Treasury = 4.5%
    market_risk_premium = 0.06   # Historical market premium = 6%
    beta = 1.25                   # Stock is 25% more volatile than market

    print(f"\nCalculating required return for {company_name}...")

    # --- CAPM FORMULA ---
    # Cost of Equity = Rf + Beta × (Market Risk Premium)
    cost_of_equity = risk_free_rate + beta * market_risk_premium

    print("\n--- 2. CAPM BREAKDOWN ---")
    print(f"Risk-Free Rate (Rf):        {risk_free_rate * 100:.2f}%")
    print(f"Beta (Risk Level):           {beta:.2f}")
    print(f"Market Risk Premium:         {market_risk_premium * 100:.2f}%")
    print("-" * 35)
    print(f"COST OF EQUITY (Required Return): {cost_of_equity * 100:.2f}%")

    # --- INTERPRETATION ---
    print("\n--- 3. INTERPRETATION ---")
    if beta < 1.0:
        risk_level = "LOWER than market (Defensive)"
    elif beta == 1.0:
        risk_level = "EQUAL to market"
    else:
        risk_level = "HIGHER than market (Aggressive)"
    
    print(f"Beta of {beta} means this stock is {risk_level}.")
    print(f"\nThis means you should require at least {cost_of_equity * 100:.1f}% annual return")
    print(f"to compensate for the risk of holding {company_name}.")

    print("\n--- HIGH RETENTION RECAP ---")
    print("1. The Risk-Free Rate is your 'floor' return (US Treasury bonds).")
    print("2. Beta tells you how much 'extra risk' this stock has vs. the market.")
    print("3. The Market Risk Premium is what you demand for taking on that extra risk.")

if __name__ == "__main__":
    calculate_capm()
