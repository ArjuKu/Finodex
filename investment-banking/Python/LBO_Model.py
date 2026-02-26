"""
LBO VALUATION MODEL (The "House Mortgage" Metaphor)
===================================================
This model calculates the return for a Private Equity firm buying a company 
using debt.

HOW TO USE:
-----------
1. Edit the 'INPUTS' section with the purchase and exit assumptions.
2. Run the script to see the 'IRR' and 'Multiple of Money (MoM)'.
"""

def calculate_lbo():
    # --- INPUTS ---
    print("--- 1. DEAL DATA INPUTS ---")
    company_name = "SecureLogistics Co."
    purchase_price = 1000.0   # $ in millions (Enterprise Value)
    purchase_ebitda = 200.0   # $ in millions
    
    debt_used_pct = 0.70      # 70% Debt, 30% Equity
    debt_used = purchase_price * debt_used_pct
    equity_investment = purchase_price - debt_used
    
    ebitda_growth = 0.05      # 5% annual EBITDA growth
    interest_rate = 0.08      # 8% annual interest on debt
    tax_rate = 0.21           # 21% corporate tax rate
    
    exit_multiple = 5.0       # Sell for the same multiple we bought it for

    print(f"\nBuying {company_name} for ${purchase_price}M...")
    print(f"Equity Investment: ${equity_investment:.1f}M | Debt: ${debt_used:.1f}M")

    # --- 5-YEAR DEBT PAYDOWN ---
    print("\n--- 2. 5-YEAR DEBT PAYDOWN ($M) ---")
    print(f"{'Year':<6} | {'EBITDA':<10} | {'Interest':<10} | {'Paydown':<10} | {'Debt End':<10}")
    print("-" * 55)

    current_ebitda = purchase_ebitda
    current_debt = debt_used
    
    for year in range(1, 6):
        current_ebitda *= (1 + ebitda_growth)
        interest_exp = current_debt * interest_rate
        
        tax = (current_ebitda - interest_exp) * tax_rate
        capex = current_ebitda * 0.25 
        
        cash_for_paydown = current_ebitda - interest_exp - tax - capex
        current_debt -= cash_for_paydown
        
        print(f"{year:<6} | {current_ebitda:<10.1f} | {interest_exp:<10.1f} | {cash_for_paydown:<10.1f} | {current_debt:<10.1f}")

    # --- EXIT VALUATION ---
    exit_enterprise_value = current_ebitda * exit_multiple
    exit_equity_value = exit_enterprise_value - current_debt
    
    multiple_of_money = exit_equity_value / equity_investment
    irr = (multiple_of_money ** (1/5)) - 1

    print("\n--- 3. RETURN SUMMARY ---")
    print(f"Exit Enterprise Value:   ${exit_enterprise_value:.1f} M")
    print(f"Less: Remaining Debt:   -${current_debt:.1f} M")
    print(f"Exit Equity Value:       ${exit_equity_value:.1f} M")
    print(f"\nMultiple of Money (MoM):  {multiple_of_money:.2f}x")
    print(f"Internal Rate of Return:  {irr * 100:.1f}%")
    
    print("\n--- HIGH RETENTION RECAP ---")
    print("1. We buy the business using a 'Mortgage' (Debt) and a small 'Down Payment' (Equity).")
    print("2. We use the business's profits for 5 years to pay back the loan (Paydown).")
    print("3. We sell the business and keep the difference—which is huge because the debt is gone!")

if __name__ == "__main__":
    calculate_lbo()
