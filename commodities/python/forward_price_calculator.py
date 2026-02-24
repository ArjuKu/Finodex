"""
Commodity Forward Price Calculator
=================================
Calculates forward/futures prices using cost of carry model.

USAGE:
------
1. Modify the INPUTS with commodity and market data
2. Run the script
3. Review forward curve and sensitivity analysis

Formula: F = S × e^((r + u - y) × t)

Where:
  S = Spot price
  r = Risk-free rate
  u = Storage cost (as decimal)
  y = Convenience yield (as decimal)
  t = Time to maturity (in years)
"""

import pandas as pd
import numpy as np

# =============================================================================
# INPUTS - Modify these values for your commodity
# =============================================================================

# Commodity Information
commodity_name = "Crude Oil (WTI)"
commodity_unit = "per barrel"  # or "per oz", "per MMBtu", etc.

# Current Spot Price
spot_price = 75.00  # $ per unit

# Market Parameters
risk_free_rate = 0.045    # Annual risk-free rate (4.5%)
storage_cost = 0.02       # Annual storage cost as % of spot (2%)
convenience_yield = 0.01 # Annual convenience yield as % of spot (1%)

# Time to maturity options (in months)
maturity_months = [1, 3, 6, 9, 12, 18, 24]

# =============================================================================
# CALCULATION ENGINE
# =============================================================================

def calculate_forward_price(spot, r, u, y, t_years):
    """
    Calculate forward price using cost of carry model
    
    F = S × e^((r + u - y) × t)
    """
    net_carry = r + u - y
    forward = spot * np.exp(net_carry * t_years)
    return forward

def calculate_implied_convenience_yield(spot, forward, r, u, t_years):
    """
    Calculate implied convenience yield from forward price
    
    y = r + u - ln(F/S) / t
    """
    implied_yield = r + u - np.log(forward / spot) / t_years
    return implied_yield

def run_forward_analysis():
    """Main forward price analysis"""
    
    print("=" * 70)
    print(f"COMMODITY FORWARD PRICE CALCULATOR: {commodity_name}")
    print("=" * 70)
    
    # Display inputs
    print("\n" + "-" * 70)
    print("INPUT PARAMETERS")
    print("-" * 70)
    print(f"\n  Spot Price:              ${spot_price:.2f} {commodity_unit}")
    print(f"  Risk-Free Rate:          {risk_free_rate:.2%}")
    print(f"  Storage Cost:            {storage_cost:.2%}")
    print(f"  Convenience Yield:       {convenience_yield:.2%}")
    print(f"  Net Carry Cost:          {risk_free_rate + storage_cost - convenience_yield:.2%}")
    
    # Calculate forward curve
    print("\n" + "-" * 70)
    print("FORWARD CURVE")
    print("-" * 70)
    
    forward_prices = []
    net_carry = risk_free_rate + storage_cost - convenience_yield
    
    print(f"\n  {'Maturity':<12} {'Time (yrs)':<12} {'Forward Price':<15} {'% Premium':<15} {'Carry $/unit':<15}")
    print("  " + "-" * 70)
    
    for months in maturity_months:
        t = months / 12  # Convert to years
        fwd = calculate_forward_price(spot_price, risk_free_rate, storage_cost, convenience_yield, t)
        premium = (fwd / spot_price - 1) * 100
        carry = fwd - spot_price
        
        forward_prices.append({
            'months': months,
            'time_years': t,
            'forward_price': fwd,
            'premium_pct': premium,
            'carry': carry
        })
        
        print(f"  {months:>3} months    {t:>8.3f}      ${fwd:>8.2f}       {premium:>+6.2f}%       ${carry:>+7.2f}")
    
    # Determine market structure
    first_fwd = forward_prices[0]['forward_price']
    last_fwd = forward_prices[-1]['forward_price']
    
    print("\n  Market Structure: ", end="")
    if last_fwd > spot_price:
        print("CONTANGO (upward curve)")
        print(f"    → Futures prices higher than spot (normal market)")
        print(f"    → Roll yield is negative for long positions")
    elif last_fwd < spot_price:
        print("BACKWARDATION (downward curve)")
        print(f"    → Futures prices lower than spot")
        print(f"    → Roll yield is positive for long positions")
    else:
        print("FLAT")
    
    # Spot vs Forward comparison
    print("\n" + "-" * 70)
    print("SPOT VS FORWARD COMPARISON")
    print("-" * 70)
    
    print(f"\n  Spot Price (immediate delivery):  ${spot_price:.2f}")
    print(f"  12-Month Forward:                 ${forward_prices[4]['forward_price']:.2f}")
    print(f"  Annualized Roll Cost:             {(forward_prices[4]['forward_price']/spot_price - 1):.2%}")
    
    # Sensitivity Analysis
    print("\n" + "-" * 70)
    print("SENSITIVITY ANALYSIS")
    print("Forward Price vs. Storage Cost & Convenience Yield")
    print("-" * 70)
    
    # 12-month forward as base
    t = 12 / 12
    
    print("\n  Forward Price ($/unit) for 12-month maturity:")
    print("\n  Storage ->     1.0%      1.5%      2.0%      2.5%      3.0%")
    print("  Conv Yield")
    
    for cy in [0.0, 0.5, 1.0, 1.5, 2.0]:
        row = f"  {cy:>5.1f}%      "
        for sc in [0.01, 0.015, 0.02, 0.025, 0.03]:
            fwd = calculate_forward_price(spot_price, risk_free_rate, sc, cy, t)
            row += f"${fwd:>6.2f}   "
        print(row)
    
    # Interest Rate Sensitivity
    print("\n" + "-" * 70)
    print("INTEREST RATE IMPACT")
    print("-" * 70)
    
    print("\n  12-Month Forward Price at Different Interest Rates:")
    print("\n  Rate      Forward Price    Change vs Base")
    print("  " + "-" * 45)
    
    base_fwd = forward_prices[4]['forward_price']
    for rate in [0.02, 0.03, 0.04, 0.05, 0.06, 0.07]:
        fwd = calculate_forward_price(spot_price, rate, storage_cost, convenience_yield, 1.0)
        change = fwd - base_fwd
        print(f"  {rate:.1%}      ${fwd:>8.2f}       ${change:>+7.2f}")
    
    # Break-even analysis
    print("\n" + "-" * 70)
    print("BREAK-EVEN ANALYSIS")
    print("-" * 70)
    
    # What forward price breaks even given storage costs?
    print(f"\n  Given storage cost of {storage_cost:.2%}:")
    print(f"    At risk-free rate {risk_free_rate:.2%}:")
    print(f"    Break-even forward price = ${spot_price * np.exp((risk_free_rate + storage_cost) * 1.0):.2f}")
    print(f"    (This assumes zero convenience yield)")
    
    # Option Pricing Context
    print("\n" + "-" * 70)
    print("CONTEXT: OPTIONS PRICING IMPLICATIONS")
    print("-" * 70)
    
    print("""
  In options pricing:
  - Forward price is used instead of spot (Black-76 model)
  - Cost of carry affects forward but not spot
  - High storage costs → higher forward → higher call option premiums
  - High convenience yield → lower forward → lower call premiums
  
  For hedging:
  - Contango: Long hedgers pay premium (negative roll yield)
  - Backwardation: Long hedgers earn premium (positive roll yield)
""")
    
    print("=" * 70)
    
    return {
        'spot_price': spot_price,
        'forward_prices': forward_prices,
        'structure': 'contango' if last_fwd > spot_price else 'backwardation'
    }

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    results = run_forward_analysis()
