"""
================================================================================
CAPM & WACC CALCULATOR - TEMPLATE
================================================================================

What this does:
    Calculates Cost of Equity using CAPM (Capital Asset Pricing Model)
    and WACC (Weighted Average Cost of Capital).

USAGE:
    1. Modify the INPUTS section below
    2. Run: python capm_calculator.py
    3. Review calculated required return and WACC

INPUTS TO MODIFY:
    - risk_free_rate: 10-year Treasury yield (e.g., 0.045 = 4.5%)
    - market_risk_premium: Historical market return minus risk-free (5-7%)
    - beta: Company beta (1.0 = same risk as market)
    - company_debt: Market value of company debt ($M)
    - company_equity: Market value of company equity ($M)
    - cost_of_debt: Interest rate on debt
    - tax_rate: Corporate tax rate

For help: See WACC_TUTORIAL.md
================================================================================
"""

# =============================================================================
# SECTION 1: INPUTS - Change these values
# =============================================================================

# Market Data
risk_free_rate = 0.045           # 10-year Treasury yield (4.5%)
market_risk_premium = 0.06        # Market risk premium (6%)

# Company-Specific Data
company_name = "TechCorp Inc."
company_beta = 1.20              # Company beta
company_debt = 7500              # Market value of debt ($M)
company_equity = 22500           # Market value of equity ($M)
company_tax_rate = 0.21          # Corporate tax rate (21%)

# Cost of Debt (pre-tax)
cost_of_debt_pre = 0.055        # Pre-tax cost of debt (5.5%)

# =============================================================================
# SECTION 2: CALCULATION ENGINE
# =============================================================================

def calculate_beta_levered(beta_u, d_e, tax_rate):
    """
    Calculate levered beta from unlevered beta.
    
    Formula: Beta_L = Beta_U × [1 + (1-T) × D/E]
    """
    return beta_u * (1 + (1 - tax_rate) * d_e)

def calculate_beta_unlevered(beta_l, d_e, tax_rate):
    """
    Calculate unlevered beta from levered beta.
    """
    return beta_l / (1 + (1 - tax_rate) * d_e)

def calculate_capm(rf, beta, mrp):
    """
    Calculate Cost of Equity using CAPM.
    
    Formula: Re = Rf + Beta × (Rm - Rf)
    """
    return rf + beta * mrp

def calculate_wacc(equity_weight, debt_weight, cost_equity, cost_debt, tax_rate):
    """
    Calculate Weighted Average Cost of Capital.
    
    Formula: WACC = (E/V × Re) + (D/V × Rd × (1-T))
    """
    return (equity_weight * cost_equity) + (debt_weight * cost_debt * (1 - tax_rate))

# =============================================================================
# SECTION 3: MAIN EXECUTION
# =============================================================================

def run_capm_analysis():
    """Main CAPM and WACC calculation"""
    
    print("=" * 70)
    print(f"CAPM & WACC CALCULATOR: {company_name}")
    print("=" * 70)
    
    # Step 1: Display Market Inputs
    print("\n>>> STEP 1: Market Data")
    print("-" * 50)
    print(f"    Risk-Free Rate (Rf):        {risk_free_rate:.2%}")
    print(f"    Market Risk Premium (MRP):   {market_risk_premium:.2%}")
    print(f"    Company Beta:                {company_beta}")
    
    # Step 2: Calculate Cost of Equity (CAPM)
    print("\n>>> STEP 2: Cost of Equity (CAPM)")
    print("-" * 50)
    print("    Formula: Re = Rf + Beta x MRP")
    print(f"    Re = {risk_free_rate:.2%} + {company_beta} x {market_risk_premium:.2%}")
    
    cost_of_equity = calculate_capm(risk_free_rate, company_beta, market_risk_premium)
    beta_contribution = company_beta * market_risk_premium
    
    print(f"    Re = {risk_free_rate:.2%} + {beta_contribution:.2%}")
    print(f"    >>> Cost of Equity: {cost_of_equity:.2%}")
    
    # Beta interpretation
    print(f"\n    Beta Interpretation:")
    if company_beta < 0.8:
        print(f"    Beta = {company_beta} -> Less volatile than market (Defensive)")
    elif company_beta > 1.2:
        print(f"    Beta = {company_beta} -> More volatile than market (Aggressive)")
    else:
        print(f"    Beta = {company_beta} -> Similar volatility to market")
    
    # Step 3: Calculate Capital Structure
    print("\n>>> STEP 3: Capital Structure")
    print("-" * 50)
    
    total_capital = company_equity + company_debt
    equity_weight = company_equity / total_capital
    debt_weight = company_debt / total_capital
    
    print(f"    Market Value of Equity:   ${company_equity:,.0f}M")
    print(f"    Market Value of Debt:     ${company_debt:,.0f}M")
    print(f"    Total Capital:           ${total_capital:,.0f}M")
    print(f"\n    Equity Weight (E/V):     {equity_weight:.1%}")
    print(f"    Debt Weight (D/V):      {debt_weight:.1%}")
    
    # Step 4: Calculate Cost of Debt
    print("\n>>> STEP 4: Cost of Debt")
    print("-" * 50)
    
    cost_of_debt_after = cost_of_debt_pre * (1 - company_tax_rate)
    
    print(f"    Pre-tax Cost of Debt:    {cost_of_debt_pre:.2%}")
    print(f"    Tax Rate:                {company_tax_rate:.1%}")
    print(f"    >>> After-tax Cost of Debt: {cost_of_debt_after:.2%}")
    
    # Step 5: Calculate WACC
    print("\n>>> STEP 5: Weighted Average Cost of Capital (WACC)")
    print("-" * 50)
    
    wacc = calculate_wacc(equity_weight, debt_weight, cost_of_equity, 
                        cost_of_debt_pre, company_tax_rate)
    
    print("    Formula: WACC = (E/V x Re) + (D/V x Rd x (1-T))")
    print(f"    WACC = ({equity_weight:.1%} x {cost_of_equity:.2%}) + ({debt_weight:.1%} x {cost_of_debt_after:.2%})")
    print(f"    WACC = {equity_weight * cost_of_equity:.2%} + {debt_weight * cost_of_debt_after:.2%}")
    print(f"\n    >>> WACC: {wacc:.2%}")
    
    # What WACC Means
    print("\n>>> WHAT THIS MEANS")
    print("-" * 50)
    print(f"    A WACC of {wacc:.2%} means:")
    print(f"    - This is the MINIMUM return the company should earn")
    print(f"    - Use this as DISCOUNT RATE in DCF valuations")
    print(f"    - Projects should earn more than {wacc:.2%} to create value")
    
    # Sensitivity Analysis
    print("\n>>> SENSITIVITY ANALYSIS")
    print("-" * 50)
    print("    How WACC changes with different capital structures:")
    print()
    print("               Cost of Debt ->")
    print("    E/V      3%      4%      5%      6%      7%")
    print("    " + "-" * 50)
    
    for ew in [0.3, 0.5, 0.7, 0.9]:
        dw = 1 - ew
        row = f"    {ew:.0%}      "
        for rd in [0.03, 0.04, 0.05, 0.06, 0.07]:
            w = calculate_wacc(ew, dw, cost_of_equity, rd, company_tax_rate)
            row += f"{w:>5.1%}   "
        print(row)
    
    # Typical WACC by industry
    print("\n>>> TYPICAL WACC BY INDUSTRY")
    print("-" * 50)
    industries = [
        ("Utilities", 0.06),
        ("Banks", 0.09),
        ("Manufacturing", 0.10),
        ("Tech", 0.11),
        ("Biotech", 0.15)
    ]
    for industry, typical_wacc in industries:
        diff = wacc - typical_wacc
        sign = "+" if diff > 0 else ""
        print(f"    {industry:<15} {typical_wacc:.0%}  (Your company: {sign}{diff:.1%})")
    
    print("\n" + "=" * 70)
    print("MODEL COMPLETE - Modify inputs to calculate for different companies")
    
    return wacc

# =============================================================================
# RUN THE MODEL
# =============================================================================

if __name__ == "__main__":
    print("\nRunning CAPM & WACC Calculator...")
    print("To modify: Change values in the INPUTS section\n")
    result = run_capm_analysis()
