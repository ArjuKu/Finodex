"""
CORPORATE DCF VALUATION MODEL (Unlevered FCF)
=============================================
This model values a company based on the cash it generates for all investors.

HOW TO USE:
-----------
1. Edit the 'INPUTS' section with your target company's data.
2. Run the script to see the 'Enterprise Value' and 'Equity Value'.
"""

def calculate_corporate_dcf():
    # --- INPUTS ---
    print("--- 1. COMPANY DATA INPUTS ---")
    # REPLACE WITH THE COMPANY YOU ARE EVALUATING
    company_name = "[ENTER COMPANY NAME]"
    current_revenue = 1000.0  # $ in millions
    revenue_growth = 0.10     # 10% annual growth
    ebit_margin = 0.20        # 20% operating margin
    tax_rate = 0.21           # 21% corporate tax rate
    
    capex_pct = 0.05          # 5% for Capital Expenditures
    depreciation_pct = 0.04   # 4% for Depreciation
    change_nwc_pct = 0.02     # 2% for Change in Net Working Capital
    
    wacc = 0.09               # 9% Weighted Average Cost of Capital
    terminal_growth = 0.025   # 2.5% Perpetual Growth Rate
    
    net_debt = 500.0          # $ in millions
    shares_outstanding = 50.0 # millions of shares

    print(f"\nValuing {company_name} using Unlevered Free Cash Flow...")

    # --- 5-YEAR FORECAST ---
    print("\n--- 2. 5-YEAR CASH FLOW FORECAST ($M) ---")
    print(f"{'Year':<6} | {'Revenue':<10} | {'EBIT':<10} | {'UFCF':<10} | {'PV':<10}")
    print("-" * 55)

    sum_pv_ufcf = 0
    proj_revenue = current_revenue
    ufcf = 0
    
    for year in range(1, 6):
        proj_revenue *= (1 + revenue_growth)
        ebit = proj_revenue * ebit_margin
        tax = ebit * tax_rate
        nopat = ebit - tax
        
        depreciation = proj_revenue * depreciation_pct
        capex = proj_revenue * capex_pct
        change_nwc = proj_revenue * change_nwc_pct
        ufcf = nopat + depreciation - capex - change_nwc
        
        pv_ufcf = ufcf / ((1 + wacc) ** year)
        sum_pv_ufcf += pv_ufcf
        
        print(f"{year:<6} | {proj_revenue:<10.1f} | {ebit:<10.1f} | {ufcf:<10.1f} | {pv_ufcf:<10.1f}")

    # --- TERMINAL VALUE ---
    terminal_value = (ufcf * (1 + terminal_growth)) / (wacc - terminal_growth)
    pv_terminal_value = terminal_value / ((1 + wacc) ** 5)

    # --- VALUATION SUMMARY ---
    enterprise_value = sum_pv_ufcf + pv_terminal_value
    equity_value = enterprise_value - net_debt
    implied_share_price = equity_value / shares_outstanding

    print("\n--- 3. VALUATION SUMMARY ---")
    print(f"Sum of PV (Years 1-5):    ${sum_pv_ufcf:.1f} M")
    print(f"PV of Terminal Value:    ${pv_terminal_value:.1f} M")
    print(f"Total Enterprise Value:  ${enterprise_value:.1f} M")
    print(f"Less: Net Debt:         -${net_debt:.1f} M")
    print(f"Total Equity Value:      ${equity_value:.1f} M")
    print(f"\nIMPLIED SHARE PRICE:     ${implied_share_price:.2f}")
    
    print("\n--- HIGH RETENTION RECAP ---")
    print("1. We forecast how much raw cash (UFCF) the business makes for everyone.")
    print("2. We bring all that future cash to today's value (Present Value).")
    print("3. Subtract the debt to find the value of the shares (Equity Value).")

if __name__ == "__main__":
    calculate_corporate_dcf()
