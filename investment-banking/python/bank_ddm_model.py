"""
Bank Dividend Discount Model (DDM)
==================================
Values a bank based on expected future dividend payments.

USAGE:
------
1. Modify the INPUTS section with your bank's dividend data
2. Run the script
3. Review the implied share price and sensitivity analysis

Gordon Growth Model: P0 = D1 / (r - g)
Two-Stage DDM: Accounts for high-growth phase followed by stable growth
"""

import pandas as pd
import numpy as np

# =============================================================================
# INPUTS - Modify these values for your bank
# =============================================================================

# Company Information
current_stock_price = 45.00       # Current share price ($)
shares_outstanding = 100           # Shares outstanding (millions)
dividend_per_share = 2.00           # Current annual dividend per share

# Dividend Growth Assumptions
dividend_growth_short = 0.08       # Short-term dividend growth (8%) 
dividend_growth_long = 0.03        # Long-term sustainable growth (3%)
high_growth_years = 5               # Years of high growth before stable growth

# Valuation Assumptions
risk_free_rate = 0.045            # 10-year Treasury (4.5%)
market_risk_premium = 0.06        # Market risk premium (6%)
beta = 1.15                       # Bank beta

# Alternative: Direct required return (overrides CAPM calculation)
use_custom_required_return = False
custom_required_return = 0.10     # 10% required return if use_custom = True

# =============================================================================
# CALCULATION ENGINE
# =============================================================================

def calculate_required_return(rf, beta, mrp):
    """Calculate cost of equity using CAPM"""
    return rf + beta * mrp

def gordon_growth_model(d1, r, g):
    """
    Gordon Growth (Single-Stage) DDM
    P0 = D1 / (r - g)
    """
    if r <= g:
        return None  # Invalid: growth cannot exceed return
    return d1 / (r - g)

def two_stage_ddm(d0, r, g_high, g_low, n_years):
    """
    Two-Stage Dividend Discount Model
    
    Stage 1: High growth for n_years
    Stage 2: Stable long-term growth
    
    P0 = Sum(D0*(1+g_high)^t / (1+r)^t) + Dn*(1+g_low) / (r - g_low) / (1+r)^n
    """
    # Stage 1: Present value of high-growth dividends
    stage1_pv = 0
    for t in range(1, n_years + 1):
        dividend = d0 * ((1 + g_high) ** t)
        pv = dividend / ((1 + r) ** t)
        stage1_pv += pv
    
    # Dividend at end of high-growth period
    dn = d0 * ((1 + g_high) ** n_years)
    
    # Stage 2: Terminal value using stable growth
    terminal_value = (dn * (1 + g_low)) / (r - g_low)
    stage2_pv = terminal_value / ((1 + r) ** n_years)
    
    return stage1_pv + stage2_pv

def run_ddm_valuation():
    """Main DDM valuation function"""
    
    print("=" * 70)
    print("BANK DIVIDEND DISCOUNT MODEL (DDM)")
    print("=" * 70)
    
    # Calculate required return
    if use_custom_required_return:
        required_return = custom_required_return
        print(f"\nUsing custom required return: {required_return:.2%}")
    else:
        required_return = calculate_required_return(risk_free_rate, beta, market_risk_premium)
        print(f"\nCost of Equity (CAPM): {required_return:.2%}")
        print(f"  Risk-Free Rate: {risk_free_rate:.2%}")
        print(f"  Beta: {beta}")
        print(f"  Market Risk Premium: {market_risk_premium:.2%}")
    
    # Dividend projections
    print("\n" + "-" * 70)
    print("DIVIDEND PROJECTIONS (Two-Stage Model)")
    print("-" * 70)
    
    print(f"\n  Current Dividend:     ${dividend_per_share:.2f}")
    print(f"  High-Growth Rate:     {dividend_growth_short:.1%} for {high_growth_years} years")
    print(f"  Stable Growth Rate:   {dividend_growth_long:.1%} thereafter")
    print(f"  Required Return:      {required_return:.2%}")
    
    # Project dividends
    dividends = []
    for year in range(1, high_growth_years + 1):
        div = dividend_per_share * ((1 + dividend_growth_short) ** year)
        pv = div / ((1 + required_return) ** year)
        dividends.append({
            'Year': year,
            'Dividend': div,
            'PV': pv
        })
    
    # Add terminal dividend
    terminal_div = dividends[-1]['Dividend'] * (1 + dividend_growth_long)
    
    df = pd.DataFrame(dividends)
    print(f"\n  Year  Dividend    PV of Dividend")
    print(f"  ----  --------    -------------")
    for _, row in df.iterrows():
        print(f"    {int(row['Year'])}   ${row['Dividend']:>6.2f}    ${row['PV']:>6.2f}")
    
    sum_pv = df['PV'].sum()
    print(f"  ----  --------    -------------")
    print(f"  Sum PV:                    ${sum_pv:>6.2f}")
    
    # Terminal Value
    print("\n" + "-" * 70)
    print("TERMINAL VALUE (Stable Growth Phase)")
    print("-" * 70)
    
    terminal_value = gordon_growth_model(terminal_div, required_return, dividend_growth_long)
    pv_terminal = terminal_value / ((1 + required_return) ** high_growth_years)
    
    print(f"\n  Terminal Dividend (Year {high_growth_years + 1}):  ${terminal_div:.2f}")
    print(f"  Terminal Value:    ${terminal_value:.2f}")
    print(f"  PV of Terminal:   ${pv_terminal:.2f}")
    
    # Total Value
    total_value = sum_pv + pv_terminal
    
    print("\n" + "-" * 70)
    print("VALUATION SUMMARY")
    print("-" * 70)
    
    print(f"  PV of Dividends (Years 1-{high_growth_years}):  ${sum_pv:.2f}")
    print(f"  PV of Terminal Value:                  ${pv_terminal:.2f}")
    print(f"  Total Intrinsic Value:                 ${total_value:.2f}")
    print(f"\n  Implied Share Price:                    ${total_value:.2f}")
    print(f"  Current Market Price:                  ${current_stock_price:.2f}")
    
    upside = (total_value - current_stock_price) / current_stock_price
    print(f"  Upside/(Downside):                      {upside:+.1%}")
    
    # Gordon Growth (Single-Stage) comparison
    print("\n" + "-" * 70)
    print("GORDON GROWTH MODEL (Single-Stage) COMPARISON")
    print("-" * 70)
    
    # Assume 3% stable growth from today
    d1 = dividend_per_share * (1 + dividend_growth_long)
    ggm_value = gordon_growth_model(d1, required_return, dividend_growth_long)
    
    if ggm_value:
        print(f"\n  Next Dividend (D1):   ${d1:.2f}")
        print(f"  Gordon Growth Value:   ${ggm_value:.2f}")
        print(f"  vs Current Price:    ${current_stock_price:.2f}")
    
    # Sensitivity Analysis
    print("\n" + "-" * 70)
    print("SENSITIVITY ANALYSIS")
    print("Implied Price vs. Required Return & Terminal Growth")
    print("-" * 70)
    
    sensitivities = []
    for g in [0.02, 0.025, 0.03, 0.035, 0.04]:
        for r in [0.08, 0.09, 0.10, 0.11, 0.12]:
            val = gordon_growth_model(d1, r, g)
            if val:
                sensitivities.append({
                    'Terminal Growth': g,
                    'Required Return': r,
                    'Implied Price': val
                })
    
    sens_df = pd.DataFrame(sensitivities)
    pivot = sens_df.pivot(index='Terminal Growth', columns='Required Return', values='Implied Price')
    print("\n" + pivot.round(2).to_string())
    
    # Dividend Metrics
    print("\n" + "-" * 70)
    print("KEY DIVIDEND METRICS")
    print("-" * 70)
    
    dividend_yield = dividend_per_share / current_stock_price
    payout_ratio = 0.40  # Assumed payout ratio (modify as needed)
    retention_ratio = 1 - payout_ratio
    
    print(f"\n  Current Dividend Yield:    {dividend_yield:.2%}")
    print(f"  Assumed Payout Ratio:      {payout_ratio:.1%}")
    print(f"  Retention Ratio:           {retention_ratio:.1%}")
    print(f"  Implied EPS (if 40% pay): ${dividend_per_share/payout_ratio:.2f}")
    
    # Dividend sustainability
    implied_growth = required_return * retention_ratio
    print(f"\n  Implied Sustainable Growth:  {implied_growth:.2%}")
    print(f"  Your Long-Term Growth Assumption: {dividend_growth_long:.2%}")
    
    if dividend_growth_long > implied_growth:
        print("  ⚠️  Warning: Assumed growth may be unsustainable!")
    else:
        print("  ✓  Growth assumption appears sustainable")
    
    print("\n" + "=" * 70)
    
    return {
        'implied_price': total_value,
        'current_price': current_stock_price,
        'upside': upside
    }

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    results = run_ddm_valuation()
