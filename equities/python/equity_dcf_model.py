"""
================================================================================
EQUITY DCF VALUATION MODEL - TEMPLATE
================================================================================

What this does:
    Values a company using Discounted Cash Flow (DCF) methodology.
    Projects Free Cash Flow to Firm (FCFF) and calculates terminal value.

USAGE:
    1. Modify the INPUTS section below with your company's data
    2. Run: python equity_dcf_model.py
    3. Review the implied share price and sensitivity analysis

INPUTS TO MODIFY:
    - company_name: Name of the company
    - current_stock_price: Current share price ($)
    - shares_outstanding: Number of shares (millions)
    - revenue_base: Current annual revenue ($ millions)
    - revenue_growth: Expected revenue growth rate (e.g., 0.10 = 10%)
    - ebitda_margin: EBITDA as % of revenue (e.g., 0.22 = 22%)
    - wacc: Weighted Average Cost of Capital (discount rate)
    - terminal_growth: Long-term growth rate (typically 0.02-0.03)

For help: See DCF_TUTORIAL.md and WACC_TUTORIAL.md
================================================================================
"""

# =============================================================================
# SECTION 1: INPUTS - Change these values for your company
# =============================================================================

# Company Information
company_name = "TechCorp Inc."
current_stock_price = 45.00       # Current share price ($)
shares_outstanding = 500           # Shares outstanding (millions)

# Income Statement Data ($ millions)
revenue_base = 10000              # Current annual revenue
revenue_growth = 0.10            # Revenue growth rate (10%)
ebitda_margin = 0.22             # EBITDA as % of revenue (22%)
depreciation_pct = 0.05          # D&A as % of revenue (5%)
capex_pct = 0.06                 # CapEx as % of revenue (6%)
nwc_pct = 0.02                   # Change in NWC as % of revenue change
tax_rate = 0.21                  # Corporate tax rate (21%)

# Balance Sheet ($ millions)
net_debt = 2000                  # Net debt (debt - cash)

# Valuation Assumptions
wacc = 0.096                    # Weighted Average Cost of Capital (9.6%)
terminal_growth = 0.03           # Terminal growth rate (3%)
terminal_multiple = 12           # Exit EBITDA multiple (alternative method)

# =============================================================================
# SECTION 2: CALCULATION ENGINE
# =============================================================================

def project_fcff(years=5):
    """
    Project Free Cash Flow to Firm for specified years.
    
    FCFF = NOPAT + D&A - CapEx - Change in Working Capital
    
    Where:
    - NOPAT = EBIT × (1 - Tax Rate)
    - D&A = Depreciation & Amortization
    - CapEx = Capital Expenditures
    - NWC = Net Working Capital
    """
    projections = []
    
    for year in range(1, years + 1):
        # Step 1: Calculate revenue with growth
        revenue = revenue_base * ((1 + revenue_growth) ** year)
        
        # Step 2: Calculate EBITDA
        ebitda = revenue * ebitda_margin
        
        # Step 3: Calculate D&A
        depreciation = revenue * depreciation_pct
        
        # Step 4: Calculate EBIT
        ebit = ebitda - depreciation
        
        # Step 5: Calculate NOPAT (Net Operating Profit After Tax)
        taxes = ebit * tax_rate
        nopat = ebit - taxes
        
        # Step 6: Calculate FCFF
        capex = revenue * capex_pct
        nwc_change = revenue * nwc_pct
        fcff = nopat + depreciation - capex - nwc_change
        
        # Step 7: Calculate Present Value (discount to today)
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
    
    return projections

def calculate_terminal_gordon(fcff_final, g, r):
    """
    Calculate terminal value using Gordon Growth Model.
    
    Formula: TV = FCF × (1+g) / (r-g)
    
    Assumes company grows at rate 'g' forever.
    """
    return (fcff_final * (1 + g)) / (r - g)

def calculate_terminal_multiple(ebitda_final, multiple):
    """
    Calculate terminal value using Exit Multiple method.
    
    Formula: TV = EBITDA × Multiple
    
    Values company at a market multiple similar to recent transactions.
    """
    return ebitda_final * multiple

# =============================================================================
# SECTION 3: MAIN EXECUTION
# =============================================================================

def run_dcf_valuation():
    """Main DCF valuation function"""
    
    print("=" * 70)
    print(f"EQUITY DCF VALUATION: {company_name}")
    print("=" * 70)
    
    # Display key inputs
    print("\n>>> KEY INPUTS")
    print("-" * 50)
    print(f"    Revenue (Base):       ${revenue_base:,.0f}M")
    print(f"    Revenue Growth:        {revenue_growth:.1%}")
    print(f"    EBITDA Margin:         {ebitda_margin:.1%}")
    print(f"    WACC (Discount Rate): {wacc:.2%}")
    print(f"    Terminal Growth:       {terminal_growth:.1%}")
    
    # Project FCFF
    print(f"\n>>> STEP 1: Project Free Cash Flow to Firm (5 years)")
    print("-" * 70)
    
    projections = project_fcff(years=5)
    
    # Print header
    print("    Year   Revenue   EBITDA    EBIT    NOPAT    FCFF      PV")
    print("    " + "-" * 65)
    
    for p in projections:
        print(f"      {p['Year']}    ${p['Revenue']:>6,.0f}  ${p['EBITDA']:>5,.0f}  ${p['EBIT']:>4,.0f}  ${p['NOPAT']:>4,.0f}  ${p['FCFF']:>4,.0f}   ${p['PV of FCFF']:>4,.0f}")
    
    sum_pv = sum(p['PV of FCFF'] for p in projections)
    print("    " + "-" * 65)
    print(f"    SUM:                                           ${sum_pv:,.0f}M")
    
    # Terminal Value - Gordon Growth
    print(f"\n>>> STEP 2: Terminal Value (Gordon Growth)")
    print("-" * 50)
    
    final_fcff = projections[-1]['FCFF']
    final_ebitda = projections[-1]['EBITDA']
    final_discount = projections[-1]['Discount Factor']
    
    # Gordon Growth method
    tv_gordon = calculate_terminal_gordon(final_fcff, terminal_growth, wacc)
    pv_tv_gordon = tv_gordon * final_discount
    
    print(f"    Terminal FCFF (Year 6):  ${final_fcff:,.0f}M")
    print(f"    Formula: TV = FCF × (1+g) / (WACC-g)")
    print(f"    TV = ${final_fcff:,.0f}M × (1+{terminal_growth:.2%}) / ({wacc:.2%}-{terminal_growth:.2%})")
    print(f"    Terminal Value:         ${tv_gordon:,.0f}M")
    print(f"    PV of Terminal Value:   ${pv_tv_gordon:,.0f}M")
    
    # Terminal Value - Exit Multiple
    print(f"\n>>> STEP 3: Terminal Value (Exit Multiple)")
    print("-" * 50)
    
    tv_multiple = calculate_terminal_multiple(final_ebitda, terminal_multiple)
    pv_tv_multiple = tv_multiple * final_discount
    
    print(f"    Terminal EBITDA:         ${final_ebitda:,.0f}M")
    print(f"    Exit Multiple:           {terminal_multiple}x EBITDA")
    print(f"    Terminal Value:         ${tv_multiple:,.0f}M")
    print(f"    PV of Terminal Value:   ${pv_tv_multiple:,.0f}M")
    
    # Valuation Summary
    print(f"\n>>> STEP 4: Valuation Summary")
    print("-" * 50)
    
    # Gordon Growth method
    ev_gordon = sum_pv + pv_tv_gordon
    equity_gordon = ev_gordon - net_debt
    price_gordon = equity_gordon / shares_outstanding
    
    print(f"    [Gordon Growth Method]")
    print(f"    Enterprise Value:       ${ev_gordon:,.0f}M")
    print(f"    Less: Net Debt:        ${net_debt:,.0f}M")
    print(f"    Equity Value:          ${equity_gordon:,.0f}M")
    print(f"    Implied Share Price:   ${price_gordon:.2f}")
    
    # Exit Multiple method
    ev_multiple = sum_pv + pv_tv_multiple
    equity_multiple = ev_multiple - net_debt
    price_multiple = equity_multiple / shares_outstanding
    
    print(f"\n    [Exit Multiple Method]")
    print(f"    Enterprise Value:       ${ev_multiple:,.0f}M")
    print(f"    Equity Value:          ${equity_multiple:,.0f}M")
    print(f"    Implied Share Price:   ${price_multiple:.2f}")
    
    # Compare to current price
    upside_g = (price_gordon - current_stock_price) / current_stock_price
    upside_m = (price_multiple - current_stock_price) / current_stock_price
    
    print(f"\n>>> COMPARISON TO MARKET")
    print("-" * 50)
    print(f"    Current Price:          ${current_stock_price:.2f}")
    print(f"    Gordon Growth Implied:  ${price_gordon:.2f} ({upside_g:+.1%})")
    print(f"    Exit Multiple Implied:  ${price_multiple:.2f} ({upside_m:+.1%})")
    
    # Sensitivity Analysis
    print(f"\n>>> SENSITIVITY ANALYSIS")
    print("-" * 50)
    print("    How price changes with WACC and Terminal Growth:")
    print()
    print("                WACC ->")
    print("    Growth    8%      9%      10%     11%     12%")
    print("    " + "-" * 50)
    
    for g in [0.02, 0.025, 0.03, 0.035, 0.04]:
        row = f"      {g:.1%}    "
        for w in [0.08, 0.09, 0.10, 0.11, 0.12]:
            tv = calculate_terminal_gordon(final_fcff, g, w)
            pv_tv = tv * final_discount
            ev = sum_pv + pv_tv
            equity = ev - net_debt
            price = equity / shares_outstanding
            row += f"${price:>5.0f}   "
        print(row)
    
    print("\n" + "=" * 70)
    print("MODEL COMPLETE - Modify inputs to value different companies")
    
    return price_gordon

# =============================================================================
# RUN THE MODEL
# =============================================================================

if __name__ == "__main__":
    print("\nRunning Equity DCF Model...")
    print("To modify: Change values in the INPUTS section\n")
    result = run_dcf_valuation()
