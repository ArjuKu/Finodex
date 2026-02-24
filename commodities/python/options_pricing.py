"""
Commodity Options Pricing Calculator
===================================
Prices commodity options using Black-76 model (for futures options).

USAGE:
------
1. Modify the INPUTS with option and market parameters
2. Run the script
3. Review option prices and Greeks

Black-76 Formula (for call/put on futures):
  Call = e^(-rT) × [F × N(d1) - K × N(d2)]
  Put = e^(-rT) × [K × N(-d2) - F × N(d1)]
  
  d1 = [ln(F/K) + (σ²/2)T] / (σ√T)
  d2 = d1 - σ√T
"""

import pandas as pd
import numpy as np

# =============================================================================
# INPUTS - Modify these values
# =============================================================================

# Option Parameters
option_type = "call"             # "call" or "put"
option_style = "European"        # "European" or "American" (American = approximation)

# Underlying Futures Price
futures_price = 75.00           # Current futures price ($)

# Strike Price
strike_price = 80.00            # Option strike price ($)

# Time to Expiration
time_to_expiry = 0.25          # Time in years (0.25 = 3 months)

# Volatility
volatility = 0.25              # Annual volatility (25%)

# Risk-Free Rate
risk_free_rate = 0.045         # Annual risk-free rate (4.5%)

# Number of contracts
contracts = 1                  # Number of option contracts
contract_size = 1000           # Barrels per contract (for oil)

# =============================================================================
# CALCULATION ENGINE
# =============================================================================

def black_76_call(F, K, T, r, sigma):
    """
    Black-76 Call Option Pricing Formula
    For options on futures/forward contracts
    """
    d1 = (np.log(F / K) + (sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call_price = np.exp(-r * T) * (F * norm_cdf(d1) - K * norm_cdf(d2))
    return call_price

def black_76_put(F, K, T, r, sigma):
    """
    Black-76 Put Option Pricing Formula
    For options on futures/forward contracts
    """
    d1 = (np.log(F / K) + (sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    put_price = np.exp(-r * T) * (K * norm_cdf(-d2) - F * norm_cdf(-d1))
    return put_price

def norm_cdf(x):
    """Standard normal cumulative distribution function"""
    return 0.5 * (1 + np.erf(x / np.sqrt(2)))

def norm_pdf(x):
    """Standard normal probability density function"""
    return np.exp(-0.5 * x ** 2) / np.sqrt(2 * np.pi)

def calculate_greeks(F, K, T, r, sigma):
    """Calculate option Greeks"""
    
    d1 = (np.log(F / K) + (sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Delta
    if option_type == "call":
        delta = np.exp(-r * T) * norm_cdf(d1)
    else:
        delta = -np.exp(-r * T) * norm_cdf(-d1)
    
    # Gamma (same for call and put)
    gamma = np.exp(-r * T) * norm_pdf(d1) / (F * sigma * np.sqrt(T))
    
    # Vega (same for call and put)
    vega = np.exp(-r * T) * F * norm_pdf(d1) * np.sqrt(T) / 100  # Per 1% vol change
    
    # Theta (per day)
    term1 = -np.exp(-r * T) * F * norm_pdf(d1) * sigma / (2 * np.sqrt(T))
    if option_type == "call":
        term2 = -r * np.exp(-r * T) * (F * norm_cdf(d1) - K * norm_cdf(d2))
    else:
        term2 = -r * np.exp(-r * T) * (K * norm_cdf(-d2) - F * norm_cdf(-d1))
    theta = (term1 + term2) / 365  # Per day
    
    # Rho
    if option_type == "call":
        rho = T * np.exp(-r * T) * (F * norm_cdf(d1) - K * norm_cdf(d2))
    else:
        rho = -T * np.exp(-r * T) * (K * norm_cdf(-d2) - F * norm_cdf(-d1))
    rho = rho / 100  # Per 1% rate change
    
    return {
        'delta': delta,
        'gamma': gamma,
        'vega': vega,
        'theta': theta,
        'rho': rho,
        'd1': d1,
        'd2': d2
    }

def run_options_analysis():
    """Main options analysis function"""
    
    print("=" * 70)
    print("COMMODITY OPTIONS PRICING (BLACK-76 MODEL)")
    print("=" * 70)
    
    # Display inputs
    print("\n" + "-" * 70)
    print("OPTION PARAMETERS")
    print("-" * 70)
    
    print(f"\n  Option Type:              {option_type.upper()}")
    print(f"  Underlying Futures Price: ${futures_price:.2f}")
    print(f"  Strike Price:             ${strike_price:.2f}")
    print(f"  Time to Expiry:           {time_to_expiry:.3f} years ({time_to_expiry * 12:.1f} months)")
    print(f"  Volatility:              {volatility:.1%} (annual)")
    print(f"  Risk-Free Rate:           {risk_free_rate:.2%}")
    print(f"  Contracts:                {contracts}")
    print(f"  Contract Size:           {contract_size} units")
    
    # Moneyness
    moneyness = futures_price / strike_price
    if option_type == "call":
        if futures_price > strike_price:
            moneyness_status = "In-the-Money (ITM)"
        elif futures_price < strike_price:
            moneyness_status = "Out-of-the-Money (OTM)"
        else:
            moneyness_status = "At-the-Money (ATM)"
    else:
        if futures_price < strike_price:
            moneyness_status = "In-the-Money (ITM)"
        elif futures_price > strike_price:
            moneyness_status = "Out-of-the-Money (OTM)"
        else:
            moneyness_status = "At-the-Money (ATM)"
    
    print(f"\n  Moneyness:                {moneyness:.3f} ({moneyness_status})")
    
    # Calculate option price
    print("\n" + "-" * 70)
    print("OPTION PRICING")
    print("-" * 70)
    
    if option_type == "call":
        option_price = black_76_call(futures_price, strike_price, time_to_expiry, 
                                     risk_free_rate, volatility)
    else:
        option_price = black_76_put(futures_price, strike_price, time_to_expiry, 
                                    risk_free_rate, volatility)
    
    total_option_value = option_price * contracts * contract_size
    
    print(f"\n  Option Price (per unit):  ${option_price:.4f}")
    print(f"  Option Price (per contract): ${option_price * contract_size:.2f}")
    print(f"  Total Value ({contracts} contracts):      ${total_option_value:,.2f}")
    
    # Intrinsic and time value
    if option_type == "call":
        intrinsic = max(futures_price - strike_price, 0)
    else:
        intrinsic = max(strike_price - futures_price, 0)
    
    time_value = option_price - intrinsic
    
    print(f"\n  Intrinsic Value:          ${intrinsic:.4f} per unit")
    print(f"  Time Value (Extrinsic):  ${time_value:.4f} per unit")
    
    # Greeks
    print("\n" + "-" * 70)
    print("OPTION GREEKS")
    print("-" * 70)
    
    greeks = calculate_greeks(futures_price, strike_price, time_to_expiry, 
                              risk_free_rate, volatility)
    
    print(f"\n  Delta (Δ):                {greeks['delta']:.4f}")
    print(f"    → Option price change per $1 change in futures price")
    
    print(f"\n  Gamma (Γ):                {greeks['gamma']:.6f}")
    print(f"    → Delta change per $1 change in futures price")
    
    print(f"\n  Vega (ν):                ${greeks['vega']:.4f}")
    print(f"    → Option price change per 1% change in volatility")
    
    print(f"\n  Theta (Θ):               ${greeks['theta']:.4f} per day")
    print(f"    → Option value decay per day (time decay)")
    
    print(f"\n  Rho (ρ):                 ${greeks['rho']:.4f}")
    print(f"    → Option price change per 1% change in interest rate")
    
    # Position Greeks
    print("\n  Position Greeks (per contract):")
    print(f"    Delta:   ${greeks['delta'] * contract_size:>8.2f}")
    print(f"    Gamma:   ${greeks['gamma'] * contract_size:>8.4f}")
    print(f"    Vega:    ${greeks['vega'] * contract_size:>8.2f}")
    print(f"    Theta:   ${greeks['theta'] * contract_size:>8.2f} per day")
    
    # Sensitivity Analysis - Strike Price
    print("\n" + "-" * 70)
    print("SENSITIVITY ANALYSIS")
    print("Option Price vs. Strike Price")
    print("-" * 70)
    
    print(f"\n  {option_type.upper()} Option Price at Different Strike Prices:")
    print("\n  Strike    Option Price    Intrinsic    Time Value    Delta")
    print("  " + "-" * 60)
    
    strikes = [60, 65, 70, 75, 80, 85, 90]
    for k in strikes:
        if option_type == "call":
            opt = black_76_call(futures_price, k, time_to_expiry, risk_free_rate, volatility)
            intr = max(futures_price - k, 0)
        else:
            opt = black_76_put(futures_price, k, time_to_expiry, risk_free_rate, volatility)
            intr = max(k - futures_price, 0)
        
        tv = opt - intr
        g = calculate_greeks(futures_price, k, time_to_expiry, risk_free_rate, volatility)
        
        print(f"  ${k:>5}      ${opt:>7.4f}       ${intr:>7.4f}      ${tv:>7.4f}      {g['delta']:>7.4f}")
    
    # Volatility Sensitivity
    print("\n" + "-" * 70)
    print("VOLATILITY SENSITIVITY")
    print("-" * 70)
    
    print(f"\n  {option_type.upper()} Price at Different Volatility Levels:")
    print("\n  Volatility    Option Price    Change")
    print("  " + "-" * 40)
    
    base_price = option_price
    for vol in [0.15, 0.20, 0.25, 0.30, 0.35, 0.40]:
        if option_type == "call":
            opt = black_76_call(futures_price, strike_price, time_to_expiry, risk_free_rate, vol)
        else:
            opt = black_76_put(futures_price, strike_price, time_to_expiry, risk_free_rate, vol)
        
        change = opt - base_price
        marker = " ← Base" if vol == 0.25 else ""
        print(f"  {vol:>5.0%}         ${opt:>7.4f}       ${change:>+7.4f}{marker}")
    
    # Break-even analysis
    print("\n" + "-" * 70)
    print("BREAK-EVEN ANALYSIS")
    print("-" * 70)
    
    # Calculate break-even at expiration
    if option_type == "call":
        break_even = strike_price + option_price
    else:
        break_even = strike_price - option_price
    
    print(f"\n  Break-even at expiration:")
    print(f"    Call:  ${strike_price:.2f} + ${option_price:.2f} = ${break_even:.2f}")
    print(f"    Put:   ${strike_price:.2f} - ${option_price:.2f} = ${break_even:.2f}")
    
    # Probability analysis (simplified)
    prob_itm = norm_cdf(-greeks['d2']) if option_type == "call" else norm_cdf(greeks['d2'])
    print(f"\n  Probability of expiring In-The-Money:  {prob_itm:.1%}")
    
    print("\n" + "=" * 70)
    
    return {
        'option_price': option_price,
        'greeks': greeks,
        'intrinsic': intrinsic,
        'time_value': time_value
    }

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    results = run_options_analysis()
