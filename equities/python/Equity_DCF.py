"""
EQUITY DCF MODEL (FCFE)
=======================
This model values a company's stock by forecasting the cash available 
to shareholders (FCFE) and discounting it back to today.

HOW TO USE:
-----------
1. Edit the 'INPUTS' section with your target company's data.
2. Run the script to see the 'Intrinsic Value' per shares.
3. Compare this to the current stock price to find the Margin of Safety.
"""

def calculate_equity_dcf():
    # --- INPUTS ---
    print("--- 1. COMPANY DATA INPUTS ---")
    company_name = "GrowthTech Inc."
    current_stock_price = 45.00  # $ per share
    shares_outstanding = 100.0   # millions of shares
    
    net_income = 100.0          # $ in millions (Year 1)
    net_income_growth = 0.08    # 8% annual growth
    
    depreciation = 30.0          # $M (add back)
    capex = 25.0                # $M (subtract)
    change_nwc = 10.0           # $M (subtract)
    net_borrowing = 0.0         # $M (simplified)
    
    cost_of_equity = 0.11       # 11% required return
    terminal_growth = 0.03      # 3% perpetual growth

    print(f"\nValuing {company_name} using FCFE...")
    print(f"Current Stock Price: ${current_stock_price:.2f}")

    # --- 5-YEAR FORECAST ---
    print("\n--- 2. 5-YEAR FREE CASH FLOW TO EQUITY ($M) ---")
    print(f"{'Year':<6} | {'Net Income':<12} | {'FCFE':<12} | {'PV of FCFE':<12}")
    print("-" * 50)

    sum_pv_fcfe = 0
    fcfe = 0
    
    for year in range(1, 6):
        fcfe = net_income + depreciation - capex - change_nwc + net_borrowing
        pv_fcfe = fcfe / ((1 + cost_of_equity) ** year)
        sum_pv_fcfe += pv_fcfe
        
        print(f"{year:<6} | ${net_income:<11.1f} | ${fcfe:<11.1f} | ${pv_fcfe:<11.1f}")
        
        net_income *= (1 + net_income_growth)

    # --- TERMINAL VALUE ---
    terminal_fcfe = fcfe * (1 + terminal_growth)
    terminal_value = terminal_fcfe / (cost_of_equity - terminal_growth)
    pv_terminal_value = terminal_value / ((1 + cost_of_equity) ** 5)

    # --- VALUATION SUMMARY ---
    intrinsic_equity_value = sum_pv_fcfe + pv_terminal_value
    intrinsic_share_price = intrinsic_equity_value / shares_outstanding
    margin_of_safety = (intrinsic_share_price - current_stock_price) / intrinsic_share_price

    print("\n--- 3. VALUATION SUMMARY ---")
    print(f"Sum of PV (Years 1-5):    ${sum_pv_fcfe:.1f} M")
    print(f"PV of Terminal Value:     ${pv_terminal_value:.1f} M")
    print(f"Total Equity Value:       ${intrinsic_equity_value:.1f} M")
    print(f"\nINTRINSIC SHARE PRICE:   ${intrinsic_share_price:.2f}")
    print(f"CURRENT STOCK PRICE:       ${current_stock_price:.2f}")
    print(f"MARGIN OF SAFETY:         {margin_of_safety * 100:.1f}%")

    if margin_of_safety > 0:
        print(f"\nConclusion: Undervalued by {margin_of_safety * 100:.1f}% - POTENTIAL BUY")
    else:
        print(f"\nConclusion: Overvalued by {abs(margin_of_safety) * 100:.1f}% - POTENTIAL SELL")
    
    print("\n--- HIGH RETENTION RECAP ---")
    print("1. We calculate how much cash the company can give to shareholders (FCFE).")
    print("2. We discount future FCFE to today's dollars using the Cost of Equity.")
    print("3. If Intrinsic Value > Market Price, we have a 'Margin of Safety' (potential bargain!).")

if __name__ == "__main__":
    calculate_equity_dcf()
