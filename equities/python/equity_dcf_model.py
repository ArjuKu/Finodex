"""
Equity DCF Valuation Model
=========================
Values a company using Discounted Cash Flow methodology.

USAGE:
------
1. Modify the INPUTS section with the company's financial data
2. Run the script
3. Review the implied share price and sensitivity analysis

The model projects Free Cash Flow to Firm (FCFF) and calculates
a terminal value using both Gordon Growth and Exit Multiple methods.
"""

import pandas as pd
import numpy as np

# =============================================================================
# INPUTS - Modify these values for your company
# =============================================================================

# Company Information
company_name = "TechCorp Inc."
current_stock_price = 45.00       # Current share price ($)
shares_outstanding = 500           # Shares outstanding (millions)

# Income Statement Data (all values in $ millions)
revenue_base = 10000              # Current annual revenue
revenue_growth = 0.10            # Revenue growth rate (10%)
ebitda_margin = 0.22             # EBITDA as % of revenue
depreciation_pct = 0.05          # D&A as % of revenue
capex_pct = 0.06                 # CapEx as % of revenue
nwc_pct = 0.02                   # Change in NWC as % of revenue change
tax_rate = 0.21                  # Corporate tax rate

# Balance Sheet
net_debt = 2000                  # Net debt (debt - cash)

# Valuation Assumptions
wacc = 0.096                    # Weighted Average Cost of Capital
terminal_growth = 0.03           # Terminal growth rate (3%)
terminal_multiple = 12           # Exit EBITDA multiple (alternative to Gordon Growth)

# =============================================================================
# CALCULATION ENGINE
# =============================================================================

def project_fcff(years=5):
    """Project Free Cash Flow to Firm"""
    
    projections = []
    
    for year in range(1, years + 1):
        # Apply growth to revenue
        revenue = revenue_base * ((1 + revenue_growth) ** year)
        
        # Calculate EBITDA
        ebitda = revenue * ebitda_margin
        
        # Calculate D&A
        depreciation = revenue * depreciation_pct
        
        # EBIT
        ebit = ebitda - depreciation
        
        # Taxes
        taxes = ebit * tax_rate
        
        # NOPAT
        nopat = ebit - taxes
        
        # FCFF = NOPAT + D&A - CapEx - Change in NWC
        capex = revenue * capex_pct
        nwc_change = revenue * nwc_pct
        
        fcff = nopat + depreciation - capex - nwc_change
        
        # Discount factor
        discount_factor = 1 / ((1 + wacc) ** year)
        
        pv = fcff * discount_factor
        
        projections.append({
            'Year': year,
            'Revenue': revenue,
            'EBITDA': ebitda,
            'EBIT': ebit,
            'NOPAT': nopat,
            'FCFF': fcff,
            'Discount Factor': discount_factor,
            'PV of FCFF': pv
        })
    
    return pd.DataFrame(projections)

def calculate_terminal_gordon(fcff_final, g, r):
    """Terminal value using Gordon Growth"""
    return (fcff_final * (1 + g)) / (r - g)

def calculate_terminal_multiple(ebitda_final, multiple):
    """Terminal value using exit multiple"""
    return ebitda_final * multiple

def run_dcf_valuation():
    """Main DCF valuation function"""
    
    print("=" * 70)
    print(f"EQUITY DCF VALUATION: {company_name}")
    print("=" * 70)
    
    # Key Assumptions
    print("\n" + "-" * 70)
    print("KEY ASSUMPTIONS")
    print("-" * 70)
    print(f"  Revenue (Base Year):    ${revenue_base:,.0f}M")
    print(f"  Revenue Growth:          {revenue_growth:.1%}")
    print(f"  EBITDA Margin:           {ebitda_margin:.1%}")
    print(f"  Tax Rate:               {tax_rate:.1%}")
    print(f"  WACC:                   {wacc:.2%}")
    print(f"  Terminal Growth:        {terminal_growth:.1%}")
    
    # Project FCFF
    print("\n" + "-" * 70)
    print("FREE CASH FLOW TO FIRM PROJECTIONS")
    print("-" * 70)
    
    df = project_fcff(years=5)
    
    print(f"\n  Year   Revenue    EBITDA    EBIT    NOPAT    FCFF      PV of FCFF")
    print(f"  " + "-" * 75)
    for _, row in df.iterrows():
        print(f"    {int(row['Year']}   ${row['Revenue']:>7,.0f}  ${row['EBITDA']:>6,.0f}  ${row['EBIT']:>5,.0f}  ${row['NOPAT']:>5,.0f}  ${row['FCFF']:>5,.0f}   ${row['PV of FCFF']:>5,.0f}")
    
    sum_pv = df['PV of FCFF'].sum()
    print(f"  " + "-" * 75)
    print(f"  Sum PV:                                                  ${sum_pv:>5,.0f}")
    
    # Terminal Value - Gordon Growth
    print("\n" + "-" * 70)
    print("TERMINAL VALUE - GORDON GROWTH")
    print("-" * 70)
    
    final_fcff = df.iloc[-1]['FCFF']
    final_ebitda = df.iloc[-1]['EBITDA']
    
    tv_gordon = calculate_terminal_gordon(final_fcff, terminal_growth, wacc)
    final_discount_factor = df.iloc[-1]['Discount Factor']
    pv_tv_gordon = tv_gordon * final_discount_factor
    
    print(f"  Terminal FCFF (Year 6):    ${final_fcff:,.0f}M")
    print(f"  Terminal Value:             ${tv_gordon:,.0f}M")
    print(f"  PV of Terminal Value:      ${pv_tv_gordon:,.0f}M")
    
    # Terminal Value - Exit Multiple
    print("\n" + "-" * 70)
    print("TERMINAL VALUE - EXIT MULTIPLE")
    print("-" * 70)
    
    tv_multiple = calculate_terminal_multiple(final_ebitda, terminal_multiple)
    pv_tv_multiple = tv_multiple * final_discount_factor
    
    print(f"  Terminal EBITDA (Year 6):   ${final_ebitda:,.0f}M")
    print(f"  Exit Multiple:               {terminal_multiple}x EBITDA")
    print(f"  Terminal Value:             ${tv_multiple:,.0f}M")
    print(f"  PV of Terminal Value:      ${pv_tv_multiple:,.0f}M")
    
    # Enterprise & Equity Value
    print("\n" + "-" * 70)
    print("VALUATION SUMMARY")
    print("-" * 70)
    
    # Using Gordon Growth
    ev_gordon = sum_pv + pv_tv_gordon
    equity_gordon = ev_gordon - net_debt
    implied_price_gordon = equity_gordon / shares_outstanding
    
    print("\n  [Gordon Growth Method]")
    print(f"    Enterprise Value:         ${ev_gordon:,.0f}M")
    print(f"    Less: Net Debt:          ${net_debt:,.0f}M")
    print(f"    Equity Value:            ${equity_gordon:,.0f}M")
    print(f"    Shares Outstanding:       {shares_outstanding}M")
    print(f"    Implied Share Price:     ${implied_price_gordon:.2f}")
    
    # Using Exit Multiple
    ev_multiple = sum_pv + pv_tv_multiple
    equity_multiple = ev_multiple - net_debt
    implied_price_multiple = equity_multiple / shares_outstanding
    
    print("\n  [Exit Multiple Method]")
    print(f"    Enterprise Value:         ${ev_multiple:,.0f}M")
    print(f"    Less: Net Debt:          ${net_debt:,.0f}M")
    print(f"    Equity Value:            ${equity_multiple:,.0f}M")
    print(f"    Implied Share Price:     ${implied_price_multiple:.2f}")
    
    # Comparison to current price
    print("\n" + "-" * 70)
    print("COMPARISON TO CURRENT PRICE")
    print("-" * 70)
    
    upside_gordon = (implied_price_gordon - current_stock_price) / current_stock_price
    upside_multiple = (implied_price_multiple - current_stock_price) / current_stock_price
    
    print(f"\n  Current Market Price:       ${current_stock_price:.2f}")
    print(f"  Gordon Growth Implied:     ${implied_price_gordon:.2f}  ({upside_gordon:+.1%})")
    print(f"  Exit Multiple Implied:    ${implied_price_multiple:.2f}  ({upside_multiple:+.1%})")
    
    # Sensitivity Analysis
    print("\n" + "-" * 70)
    print("SENSITIVITY ANALYSIS")
    print("Implied Price vs. WACC & Terminal Growth")
    print("-" * 70)
    
    sensitivities = []
    for g in [0.02, 0.025, 0.03, 0.035, 0.04]:
        for w in [0.08, 0.09, 0.10, 0.11, 0.12]:
            tv = calculate_terminal_gordon(final_fcff, g, w)
            pv_tv = tv * final_discount_factor
            ev = sum_pv + pv_tv
            equity = ev - net_debt
            price = equity / shares_outstanding
            sensitivities.append({
                'Terminal Growth': g,
                'WACC': w,
                'Implied Price': price
            })
    
    sens_df = pd.DataFrame(sensitivities)
    pivot = sens_df.pivot(index='Terminal Growth', columns='WACC', values='Implied Price')
    print("\n" + pivot.round(2).to_string())
    
    print("\n" + "=" * 70)
    
    return {
        'implied_price_gordon': implied_price_gordon,
        'implied_price_multiple': implied_price_multiple,
        'current_price': current_stock_price,
        'projections': df
    }

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    results = run_dcf_valuation()
