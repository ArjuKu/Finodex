"""
Bank DCF Valuation Model
========================
This script values a bank using Discounted Cash Flow (FCFE) methodology.

USAGE:
------
1. Modify the INPUTS section below with your bank's financial data
2. Run the script
3. Review the output - implied share price and sensitivity analysis

The model projects 5 years of Free Cash Flow to Equity (FCFE) and 
calculates a terminal value using the Gordon Growth model.
"""

import numpy as np
import pandas as pd

# =============================================================================
# INPUTS - Modify these values for your bank
# =============================================================================

# Company Information
current_stock_price = 45.00       # Current share price ($)
shares_outstanding = 100           # Shares outstanding (millions)

# Financial Projections (all values in $ millions)
net_income_base = 500              # Current annual net income
interest_income_base = 1200        # Current annual interest income
interest_expense_base = 450        # Current annual interest expense
non_interest_income_base = 400     # Current annual non-interest income
operating_expenses_base = 850      # Current annual operating expenses
provisions_base = 100              # Current loan loss provisions

# Growth Assumptions
revenue_growth = 0.05             # Annual revenue growth rate (5%)
opex_growth = 0.04                # Operating expense growth (4%)
provision_growth = 0.03           # Provision growth (3%)

# Balance Sheet
total_equity_base = 2000           # Current total equity ($M)
net_borrowing_annual = 80          # Annual net borrowing/debt repayment

# Valuation Assumptions
risk_free_rate = 0.045            # 10-year Treasury yield (4.5%)
market_risk_premium = 0.06        # Market risk premium (6%)
beta = 1.15                       # Bank beta
terminal_growth = 0.03            # Terminal growth rate (3%)
tax_rate = 0.21                   # Corporate tax rate (21%)

# =============================================================================
# CALCULATION ENGINE - Do not modify unless you understand the math
# =============================================================================

def calculate_cost_of_equity(rf, beta, mrp):
    """Calculate cost of equity using CAPM"""
    return rf + beta * mrp

def project_fcfe(years=5):
    """Project Free Cash Flow to Equity for specified years"""
    
    projections = []
    
    for year in range(1, years + 1):
        # Apply growth rates
        net_income = net_income_base * ((1 + revenue_growth) ** year)
        interest_income = interest_income_base * ((1 + revenue_growth) ** year)
        interest_expense = interest_expense_base * ((1 + revenue_growth) ** year)
        non_interest_income = non_interest_income_base * ((1 + revenue_growth) ** year)
        opex = operating_expenses_base * ((1 + opex_growth) ** year)
        provisions = provisions_base * ((1 + provision_growth) ** year)
        
        # Calculate FCFE components
        # FCFE = Net Income + D&A - CapEx - Change in NWC - Net Borrowing
        # For banks: simplified as Net Income - Net Borrowing + adjustments
        
        # Simplified FCFE for banks
        fcfe = net_income - net_borrowing_annual
        
        # Discount factor
        cost_of_equity = calculate_cost_of_equity(risk_free_rate, beta, market_risk_premium)
        discount_factor = 1 / ((1 + cost_of_equity) ** year)
        
        pv = fcfe * discount_factor
        
        projections.append({
            'Year': year,
            'Net Income': net_income,
            'FCFE': fcfe,
            'Discount Factor': discount_factor,
            'PV of FCFE': pv
        })
    
    return pd.DataFrame(projections)

def calculate_terminal_value(fcfe_final, g, r):
    """Calculate terminal value using Gordon Growth Model"""
    return (fcfe_final * (1 + g)) / (r - g)

def run_valuation():
    """Main valuation function"""
    
    print("=" * 70)
    print("BANK DCF VALUATION MODEL")
    print("=" * 70)
    
    # Cost of equity
    cost_of_equity = calculate_cost_of_equity(risk_free_rate, beta, market_risk_premium)
    print(f"\nCost of Equity (CAPM): {cost_of_equity:.2%}")
    print(f"  Risk-Free Rate: {risk_free_rate:.2%}")
    print(f"  Beta: {beta}")
    print(f"  Market Risk Premium: {market_risk_premium:.2%}")
    
    # Project FCFE
    print("\n" + "-" * 70)
    print("FREE CASH FLOW TO EQUITY PROJECTIONS")
    print("-" * 70)
    
    df = project_fcfe(years=5)
    print(df.to_string(index=False))
    
    # Sum of PV
    sum_pv = df['PV of FCFE'].sum()
    print(f"\nSum of PV (Years 1-5): ${sum_pv:,.2f}M")
    
    # Terminal Value
    print("\n" + "-" * 70)
    print("TERMINAL VALUE")
    print("-" * 70)
    
    final_fcfe = df.iloc[-1]['FCFE']
    terminal_value = calculate_terminal_value(final_fcfe, terminal_growth, cost_of_equity)
    final_discount_factor = df.iloc[-1]['Discount Factor']
    pv_terminal = terminal_value * final_discount_factor
    
    print(f"Terminal FCFE (Year 6): ${final_fcfe:,.2f}M")
    print(f"Terminal Value: ${terminal_value:,.2f}M")
    print(f"PV of Terminal Value: ${pv_terminal:,.2f}M")
    
    # Enterprise Value
    enterprise_value = sum_pv + pv_terminal
    
    print("\n" + "-" * 70)
    print("VALUATION SUMMARY")
    print("-" * 70)
    
    print(f"PV of FCFE (Years 1-5): ${sum_pv:,.2f}M")
    print(f"PV of Terminal Value:  ${pv_terminal:,.2f}M")
    print(f"Total Enterprise Value: ${enterprise_value:,.2f}M")
    
    # Equity Value (simplified - no net debt adjustment in this model)
    equity_value = enterprise_value
    
    # Per share
    implied_price = equity_value / shares_outstanding
    upside = (implied_price - current_stock_price) / current_stock_price
    
    print(f"\nImplied Share Price:    ${implied_price:.2f}")
    print(f"Current Share Price:    ${current_stock_price:.2f}")
    print(f"Upside/(Downside):      {upside:.1%}")
    
    # Sensitivity Analysis
    print("\n" + "-" * 70)
    print("SENSITIVITY ANALYSIS")
    print("Implied Price vs. Terminal Growth & Cost of Equity")
    print("-" * 70)
    
    sensitivities = []
    for g in [0.02, 0.025, 0.03, 0.035, 0.04]:
        for r in [0.09, 0.10, 0.11, 0.12, 0.13]:
            tv = calculate_terminal_value(final_fcfe, g, r)
            pv_tv = tv * final_discount_factor
            ev = sum_pv + pv_tv
            price = ev / shares_outstanding
            sensitivities.append({
                'Terminal Growth': g,
                'Cost of Equity': r,
                'Implied Price': price
            })
    
    sens_df = pd.DataFrame(sensitivities)
    pivot = sens_df.pivot(index='Terminal Growth', columns='Cost of Equity', values='Implied Price')
    print("\n" + pivot.round(2).to_string())
    
    print("\n" + "=" * 70)
    
    return {
        'implied_price': implied_price,
        'current_price': current_stock_price,
        'upside': upside,
        'projections': df
    }

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    results = run_valuation()
