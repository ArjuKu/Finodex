"""
CAPM & Cost of Equity Calculator
================================
Calculates cost of equity using the Capital Asset Pricing Model (CAPM)
and other methods.

USAGE:
------
1. Modify the INPUTS section with market data and company beta
2. Run the script
3. Review the calculated required return and sensitivity analysis

CAPM Formula: Re = Rf + Beta × (Rm - Rf)
"""

import pandas as pd
import numpy as np

# =============================================================================
# INPUTS - Modify these values
# =============================================================================

# Market Data
risk_free_rate = 0.045           # 10-year Treasury yield (4.5%)
market_return = 0.105            # Expected market return (10.5%)
market_risk_premium = market_return - risk_free_rate

# Company-Specific
company_name = "TechCorp Inc."
company_beta = 1.20              # Levered beta
company_debt = 7500              # Market value of debt ($M)
company_equity = 22500           # Market value of equity ($M)
company_tax_rate = 0.21          # Corporate tax rate

# Alternative: Use unlevered beta from industry
use_unlevered_beta = False
industry_unlevered_beta = 1.00  # Industry unlevered beta
industry_debt_equity = 0.50      # Industry D/E ratio

# =============================================================================
# CALCULATION ENGINE
# =============================================================================

def calculate_beta_levered(beta_u, d_e, tax_rate):
    """Calculate levered beta from unlevered beta"""
    return beta_u * (1 + (1 - tax_rate) * d_e)

def calculate_beta_unlevered(beta_l, d_e, tax_rate):
    """Calculate unlevered beta from levered beta"""
    return beta_l / (1 + (1 - tax_rate) * d_e)

def calculate_capm(rf, beta, mrp):
    """
    Capital Asset Pricing Model
    Re = Rf + Beta × (Rm - Rf)
    """
    return rf + beta * mrp

def calculate_buildup(rf, beta, mrp, size_premium=0, specific_premium=0):
    """
    Build-Up Method
    Re = Rf + Beta × MRP + Size Premium + Specific Risk Premium
    """
    return rf + (beta * mrp) + size_premium + specific_premium

def run_capm_analysis():
    """Main CAPM analysis function"""
    
    print("=" * 70)
    print(f"CAPM & COST OF EQUITY CALCULATOR: {company_name}")
    print("=" * 70)
    
    # Display Market Data
    print("\n" + "-" * 70)
    print("MARKET DATA")
    print("-" * 70)
    print(f"  Risk-Free Rate (Rf):         {risk_free_rate:.2%}")
    print(f"  Expected Market Return (Rm): {market_return:.2%}")
    print(f"  Market Risk Premium (MRP):    {market_risk_premium:.2%}")
    
    # Beta Calculation
    print("\n" + "-" * 70)
    print("BETA CALCULATION")
    print("-" * 70)
    
    if use_unlevered_beta:
        # Relever the industry beta for this company's capital structure
        company_d_e = company_debt / company_equity
        levered_beta = calculate_beta_levered(
            industry_unlevered_beta, 
            company_d_e, 
            company_tax_rate
        )
        print(f"\n  Using Unlevered Beta Method:")
        print(f"    Industry Unlevered Beta:    {industry_unlevered_beta:.2f}")
        print(f"    Industry D/E Ratio:         {industry_debt_equity:.2f}")
        print(f"    Company D/E Ratio:          {company_d_e:.2f}")
        print(f"    Tax Rate:                   {company_tax_rate:.1%}")
        print(f"\n  Relevered Beta:              {levered_beta:.2f}")
    else:
        levered_beta = company_beta
        print(f"\n  Using Company Beta:")
        print(f"    Levered Beta:              {levered_beta:.2f}")
    
    # Beta interpretation
    print("\n  Beta Interpretation:")
    if levered_beta < 0.8:
        print(f"    Beta = {levered_beta:.2f} → Less volatile than market (Defensive)")
    elif levered_beta > 1.2:
        print(f"    Beta = {levered_beta:.2f} → More volatile than market (Aggressive)")
    else:
        print(f"    Beta = {levered_beta:.2f} → Similar volatility to market")
    
    # CAPM Calculation
    print("\n" + "-" * 70)
    print("COST OF EQUITY (CAPM)")
    print("-" * 70)
    
    cost_of_equity = calculate_capm(risk_free_rate, levered_beta, market_risk_premium)
    
    print(f"\n  Formula: Re = Rf + β × (Rm - Rf)")
    print(f"  Re = {risk_free_rate:.2%} + {levered_beta:.2f} × {market_risk_premium:.2%}")
    print(f"  Re = {risk_free_rate:.2%} + {levered_beta * market_risk_premium:.2%}")
    print(f"\n  Cost of Equity (Required Return):  {cost_of_equity:.2%}")
    
    # Build-Up Method (optional)
    print("\n" + "-" * 70)
    print("BUILD-UP METHOD (Optional)")
    print("-" * 70)
    
    # Size premium example (small cap premium)
    size_premium = 0.02  # 2% for small cap
    specific_premium = 0  # Company-specific risk
    
    buildup = calculate_buildup(risk_free_rate, levered_beta, market_risk_premium, 
                               size_premium, specific_premium)
    
    print(f"\n  Formula: Re = Rf + β × MRP + Size Premium + Specific Premium")
    print(f"  Re = {risk_free_rate:.2%} + {levered_beta:.2f} × {market_risk_premium:.2%} + {size_premium:.2%} + {specific_premium:.2%}")
    print(f"  Re = {risk_free_rate:.2%} + {levered_beta * market_risk_premium:.2%} + {size_premium:.2%}")
    print(f"\n  Cost of Equity (Build-Up):   {buildup:.2%}")
    
    # WACC Components
    print("\n" + "-" * 70)
    print("WEIGHTED AVERAGE COST OF CAPITAL (WACC) COMPONENTS")
    print("-" * 70)
    
    total_capital = company_equity + company_debt
    equity_weight = company_equity / total_capital
    debt_weight = company_debt / total_capital
    
    # Cost of debt (simplified - use actual if available)
    cost_of_debt_pre = 0.055  # Pre-tax cost of debt
    cost_of_debt = cost_of_debt_pre * (1 - company_tax_rate)
    
    wacc = (equity_weight * cost_of_equity) + (debt_weight * cost_of_debt)
    
    print(f"\n  Capital Structure:")
    print(f"    Market Value of Equity:    ${company_equity:,.0f}M")
    print(f"    Market Value of Debt:      ${company_debt:,.0f}M")
    print(f"    Total Capital:             ${total_capital:,.0f}M")
    print(f"\n  Weights:")
    print(f"    Equity Weight (E/V):      {equity_weight:.1%}")
    print(f"    Debt Weight (D/V):         {debt_weight:.1%}")
    print(f"\n  Cost of Capital:")
    print(f"    Cost of Equity (Re):       {cost_of_equity:.2%}")
    print(f"    Cost of Debt (Rd):         {cost_of_debt:.2%} (after-tax)")
    print(f"\n  WACC = (E/V × Re) + (D/V × Rd × (1-T))")
    print(f"  WACC = ({equity_weight:.1%} × {cost_of_equity:.2%}) + ({debt_weight:.1%} × {cost_of_debt:.2%})")
    print(f"\n  WACC:                       {wacc:.2%}")
    
    # Sensitivity Analysis
    print("\n" + "-" * 70)
    print("SENSITIVITY ANALYSIS")
    print("Cost of Equity vs. Beta & Market Risk Premium")
    print("-" * 70)
    
    sensitivities = []
    for beta in [0.8, 1.0, 1.2, 1.4, 1.6]:
        for mrp in [0.04, 0.05, 0.06, 0.07, 0.08]:
            re = calculate_capm(risk_free_rate, beta, mrp)
            sensitivities.append({
                'Beta': beta,
                'MRP': mrp,
                'Cost of Equity': re
            })
    
    sens_df = pd.DataFrame(sensitivities)
    pivot = sens_df.pivot(index='Beta', columns='MRP', values='Cost of Equity')
    print("\n" + pivot.round(2).to_string())
    
    # WACC Sensitivity
    print("\n" + "-" * 70)
    print("WACC SENSITIVITY")
    print("-" * 70)
    
    wacc_sens = []
    for re in [0.08, 0.10, 0.12, 0.14, 0.16]:
        for rd in [0.03, 0.04, 0.05, 0.06, 0.07]:
            w = (equity_weight * re) + (debt_weight * rd * (1 - company_tax_rate))
            wacc_sens.append({
                'Cost of Equity': re,
                'Cost of Debt': rd,
                'WACC': w
            })
    
    wacc_df = pd.DataFrame(wacc_sens)
    wacc_pivot = wacc_df.pivot(index='Cost of Equity', columns='Cost of Debt', values='WACC')
    print("\n" + wacc_pivot.round(2).to_string())
    
    print("\n" + "=" * 70)
    
    return {
        'cost_of_equity': cost_of_equity,
        'wacc': wacc,
        'beta': levered_beta
    }

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    results = run_capm_analysis()
