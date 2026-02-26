"""
================================================================================
BANK DCF VALUATION MODEL - TEMPLATE
================================================================================

What this does:
    Values a bank using Discounted Cash Flow (FCFE) methodology.
    Projects 5 years of Free Cash Flow to Equity and calculates terminal value.

USAGE:
    1. Modify the INPUTS section below with your bank's data
    2. Run: python bank_dcf_model.py
    3. Review the output - implied share price and sensitivity analysis

INPUTS TO MODIFY:
    - current_stock_price: Current share price in dollars
    - shares_outstanding: Number of shares in millions
    - net_income_base: Current annual net income ($ millions)
    - revenue_growth: Expected annual revenue growth (e.g., 0.05 = 5%)
    - terminal_growth: Long-term growth rate (typically 0.02-0.03)
    - See INPUTS section below for more

For help understanding the model, see: ../valuation-methods/BANK_VALUATION_TUTORIAL.md
================================================================================
"""

# =============================================================================
# SECTION 1: INPUTS - Change these values for your bank
# =============================================================================

# Company Information
# ------------------
current_stock_price = 45.00       # Current share price ($)
shares_outstanding = 100           # Shares outstanding (millions)

# Financial Data ($ millions)
# --------------------------
net_income_base = 500              # Current annual net income
interest_income_base = 1200        # Current annual interest income  
interest_expense_base = 450        # Current annual interest expense
non_interest_income_base = 400     # Current annual non-interest income
operating_expenses_base = 850      # Current annual operating expenses
provisions_base = 100              # Current loan loss provisions

# Growth Rates (as decimals)
# -------------------------
revenue_growth = 0.05             # Annual revenue growth rate (5%)
opex_growth = 0.04                # Operating expense growth (4%)
provision_growth = 0.03           # Provision growth (3%)

# Balance Sheet ($ millions)
# -----------------------
total_equity_base = 2000           # Current total equity
net_borrowing_annual = 80          # Annual net borrowing

# Valuation Assumptions
# --------------------
risk_free_rate = 0.045            # 10-year Treasury yield (4.5%)
market_risk_premium = 0.06        # Market risk premium (6%)
beta = 1.15                       # Bank beta - measure of risk
terminal_growth = 0.03            # Terminal growth rate (3%)
tax_rate = 0.21                   # Corporate tax rate (21%)

# =============================================================================
# SECTION 2: CALCULATION ENGINE - Don't change unless you understand the math
# =============================================================================

def calculate_cost_of_equity(rf, beta, mrp):
    """
    Calculate cost of equity using CAPM formula:
    Re = Rf + Beta × (Rm - Rf)
    
    Args:
        rf: Risk-free rate (10-year Treasury)
        beta: Measure of systematic risk
        mrp: Market risk premium
    
    Returns:
        Cost of equity as decimal
    """
    return rf + beta * mrp

def project_fcfe(years=5):
    """
    Project Free Cash Flow to Equity for specified number of years.
    
    FCFE = Net Income - Net Borrowing (simplified for banks)
    """
    projections = []
    
    # Get cost of equity for discounting
    cost_of_equity = calculate_cost_of_equity(risk_free_rate, beta, market_risk_premium)
    
    for year in range(1, years + 1):
        # Apply growth rates to income statement items
        # Formula: Base × (1 + growth_rate)^year
        net_income = net_income_base * ((1 + revenue_growth) ** year)
        
        # FCFE for banks: Net Income minus net borrowing
        # In reality, you'd also account for D&A, CapEx, working capital
        fcfe = net_income - net_borrowing_annual
        
        # Calculate present value (PV) - discount future cash flow to today
        # Formula: FCFE / (1 + r)^year
        discount_factor = 1 / ((1 + cost_of_equity) ** year)
        pv = fcfe * discount_factor
        
        projections.append({
            'Year': year,
            'Net Income': net_income,
            'FCFE': fcfe,
            'Discount Factor': discount_factor,
            'PV of FCFE': pv
        })
    
    return projections

def calculate_terminal_value(fcfe_final, g, r):
    """
    Calculate terminal value using Gordon Growth Model.
    
    Formula: TV = FCF × (1 + g) / (r - g)
    
    This values the company from year 6 onwards as a perpetuity.
    
    Args:
        fcfe_final: Final year's FCFE
        g: Terminal growth rate
        r: Discount rate (cost of equity)
    """
    return (fcfe_final * (1 + g)) / (r - g)

# =============================================================================
# SECTION 3: MAIN EXECUTION
# =============================================================================

def run_valuation():
    """Main valuation function - runs the entire model"""
    
    print("=" * 70)
    print("BANK DCF VALUATION MODEL")
    print("=" * 70)
    
    # Step 1: Calculate Cost of Equity using CAPM
    cost_of_equity = calculate_cost_of_equity(risk_free_rate, beta, market_risk_premium)
    print(f"\n>>> STEP 1: Cost of Equity (CAPM)")
    print(f"    Formula: Re = Rf + Beta × MRP")
    print(f"    Re = {risk_free_rate:.2%} + {beta} × {market_risk_premium:.2%}")
    print(f"    Cost of Equity: {cost_of_equity:.2%}")
    
    # Step 2: Project FCFE for 5 years
    print(f"\n>>> STEP 2: Project Free Cash Flow to Equity (5 years)")
    print("-" * 70)
    
    projections = project_fcfe(years=5)
    
    # Print header
    print(f"  Year    Net Income    FCFE       Discount    PV of FCFE")
    print(f"  ----    ----------   ----       --------    ----------")
    
    for p in projections:
        print(f"    {p['Year']}    ${p['Net Income']:>6,.0f}M   ${p['FCFE']:>5,.0f}M   {p['Discount Factor']:.4f}    ${p['PV of FCFE']:>5,.0f}M")
    
    # Sum of PV
    sum_pv = sum(p['PV of FCFE'] for p in projections)
    print(f"  ----    ----------   ----       --------    ----------")
    print(f"  SUM:                                          ${sum_pv:,.0f}M")
    
    # Step 3: Calculate Terminal Value
    print(f"\n>>> STEP 3: Terminal Value (Years 6+)")
    print("-" * 70)
    
    final_fcfe = projections[-1]['FCFE']
    final_discount_factor = projections[-1]['Discount Factor']
    
    # Gordon Growth: TV = FCF × (1+g) / (r-g)
    terminal_value = calculate_terminal_value(final_fcfe, terminal_growth, cost_of_equity)
    pv_terminal = terminal_value * final_discount_factor
    
    print(f"    Terminal FCFE (Year 6):   ${final_fcfe:,.0f}M")
    print(f"    Formula: TV = FCF × (1+g) / (r-g)")
    print(f"    TV = ${final_fcfe:,.0f}M × (1+{terminal_growth:.2%}) / ({cost_of_equity:.2%} - {terminal_growth:.2%})")
    print(f"    Terminal Value:          ${terminal_value:,.0f}M")
    print(f"    PV of Terminal Value:    ${pv_terminal:,.0f}M")
    
    # Step 4: Calculate Enterprise and Equity Value
    print(f"\n>>> STEP 4: Valuation Summary")
    print("-" * 70)
    
    enterprise_value = sum_pv + pv_terminal
    equity_value = enterprise_value  # Simplified - no debt adjustment
    
    implied_price = equity_value / shares_outstanding
    upside = (implied_price - current_stock_price) / current_stock_price
    
    print(f"    PV of FCFE (Years 1-5):    ${sum_pv:,.0f}M")
    print(f"    PV of Terminal Value:      ${pv_terminal:,.0f}M")
    print(f"    Enterprise Value:          ${enterprise_value:,.0f}M")
    print(f"    Implied Share Price:       ${implied_price:.2f}")
    print(f"    Current Share Price:        ${current_stock_price:.2f}")
    print(f"    Upside/(Downside):         {upside:+.1%}")
    
    # Step 5: Sensitivity Analysis
    print(f"\n>>> STEP 5: Sensitivity Analysis")
    print("-" * 70)
    print("    How share price changes with different assumptions:")
    print()
    print("             Cost of Equity ->")
    print("Terminal    9%      10%     11%     12%     13%")
    print("Growth")
    
    for g in [0.02, 0.025, 0.03, 0.035, 0.04]:
        row = f"    {g:.1%}     "
        for r in [0.09, 0.10, 0.11, 0.12, 0.13]:
            tv = calculate_terminal_value(final_fcfe, g, r)
            pv_tv = tv * final_discount_factor
            ev = sum_pv + pv_tv
            price = ev / shares_outstanding
            row += f"${price:>5.0f}   "
        print(row)
    
    print()
    print("=" * 70)
    print("MODEL COMPLETE - Modify inputs to use for different banks")
    
    return implied_price

# =============================================================================
# RUN THE MODEL
# =============================================================================

if __name__ == "__main__":
    print("\nRunning Bank DCF Model...")
    print("To modify: Change values in the INPUTS section above\n")
    result = run_valuation()
