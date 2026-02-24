"""
Comparable Company Analysis (Comps)
==================================
Analyzes a company using comparable public company multiples.

USAGE:
------
1. Modify the INPUTS with your target company's data
2. Modify the peer_data with comparable companies
3. Run the script to see valuation range
"""

import pandas as pd
import numpy as np

# =============================================================================
# INPUTS - Target Company Data
# =============================================================================

target_company = "Target Company"

# Target company metrics (modify with actual data)
target = {
    'revenue': 10000,          # Revenue ($M)
    'ebitda': 2200,           # EBITDA ($M)
    'ebit': 1800,             # EBIT ($M)
    'net_income': 1200,       # Net Income ($M)
    'book_value': 8000,        # Book Value ($M)
    'shares_outstanding': 500, # Shares (M)
    'stock_price': 45.00,      # Current stock price ($)
    'net_debt': 2000,          # Net Debt ($M)
    'dividend_yield': 0.0      # Dividend yield
}

# =============================================================================
# PEER COMPANY DATA - Add your comparables here
# =============================================================================

# Peer company data (modify with actual data)
peer_data = [
    {'company': 'Company A', 'ticker': 'COMPA', 'sector': 'Tech',
     'market_cap': 25000, 'enterprise_value': 27000, 'revenue': 15000, 
     'ebitda': 3000, 'ebit': 2400, 'net_income': 1800, 'book_value': 12000,
     'pe': 14.0, 'ev_ebitda': 9.0, 'ev_revenue': 1.8, 'pb': 2.1, 'ps': 1.7},
    
    {'company': 'Company B', 'ticker': 'COMPB', 'sector': 'Tech',
     'market_cap': 18000, 'enterprise_value': 19000, 'revenue': 12000,
     'ebitda': 2400, 'ebit': 1900, 'net_income': 1400, 'book_value': 9000,
     'pe': 12.9, 'ev_ebitda': 7.9, 'ev_revenue': 1.6, 'pb': 2.0, 'ps': 1.5},
    
    {'company': 'Company C', 'ticker': 'COMPC', 'sector': 'Tech',
     'market_cap': 30000, 'enterprise_value': 32000, 'revenue': 20000,
     'ebitda': 4000, 'ebit': 3200, 'net_income': 2400, 'book_value': 16000,
     'pe': 12.5, 'ev_ebitda': 8.0, 'ev_revenue': 1.6, 'pb': 1.9, 'ps': 1.5},
    
    {'company': 'Company D', 'ticker': 'COMPD', 'sector': 'Tech',
     'market_cap': 15000, 'enterprise_value': 16500, 'revenue': 9000,
     'ebitda': 1800, 'ebit': 1400, 'net_income': 1000, 'book_value': 7000,
     'pe': 15.0, 'ev_ebitda': 9.2, 'ev_revenue': 1.8, 'pb': 2.1, 'ps': 1.7},
    
    {'company': 'Company E', 'ticker': 'COMPE', 'sector': 'Tech',
     'market_cap': 22000, 'enterprise_value': 24000, 'revenue': 14000,
     'ebitda': 2800, 'ebit': 2200, 'net_income': 1600, 'book_value': 11000,
     'pe': 13.8, 'ev_ebitda': 8.6, 'ev_revenue': 1.7, 'pb': 2.0, 'ps': 1.6},
]

# =============================================================================
# CALCULATION ENGINE
# =============================================================================

def run_comps_analysis():
    """Main comps analysis function"""
    
    print("=" * 70)
    print(f"COMPARABLE COMPANY ANALYSIS: {target_company}")
    print("=" * 70)
    
    # Create peer dataframe
    peers = pd.DataFrame(peer_data)
    
    # Target metrics
    target_ev = target['market_cap'] + target['net_debt']
    
    print("\n" + "-" * 70)
    print("TARGET COMPANY METRICS")
    print("-" * 70)
    print(f"\n  Financials ($M):")
    print(f"    Revenue:            ${target['revenue']:>10,.0f}M")
    print(f"    EBITDA:             ${target['ebitda']:>10,.0f}M")
    print(f"    EBIT:               ${target['ebit']:>10,.0f}M")
    print(f"    Net Income:         ${target['net_income']:>10,.0f}M")
    print(f"    Book Value:         ${target['book_value']:>10,.0f}M")
    print(f"\n  Market Data:")
    print(f"    Stock Price:        ${target['stock_price']:>10,.2f}")
    print(f"    Shares Outstanding: {target['shares_outstanding']:>10,.0f}M")
    print(f"    Market Cap:         ${target['market_cap']:>10,.0f}M")
    print(f"    Net Debt:           ${target['net_debt']:>10,.0f}M")
    print(f"    Enterprise Value:   ${target_ev:>10,.0f}M")
    
    # Calculate target multiples
    target_pe = target['market_cap'] / target['net_income']
    target_ev_ebitda = target_ev / target['ebitda']
    target_ev_revenue = target_ev / target['revenue']
    target_pb = target['market_cap'] / target['book_value']
    target_ps = target['market_cap'] / target['revenue']
    
    print(f"\n  Target Multiples:")
    print(f"    P/E:                {target_pe:>10.1f}x")
    print(f"    EV/EBITDA:          {target_ev_ebitda:>10.1f}x")
    print(f"    EV/Revenue:         {target_ev_revenue:>10.1f}x")
    print(f"    P/B:                {target_pb:>10.1f}x")
    print(f"    P/S:                {target_ps:>10.1f}x")
    
    # Peer multiples
    print("\n" + "-" * 70)
    print("PEER GROUP MULTIPLES")
    print("-" * 70)
    
    # Calculate averages and medians
    metrics = ['pe', 'ev_ebitda', 'ev_revenue', 'pb', 'ps']
    
    print("\n  Company          P/E    EV/EBITDA  EV/Rev    P/B     P/S")
    print("  " + "-" * 65)
    for _, peer in peers.iterrows():
        print(f"  {peer['company']:<15} {peer['pe']:>5.1f}x  {peer['ev_ebitda']:>6.1f}x  {peer['ev_revenue']:>5.2f}x  {peer['pb']:>5.2f}x  {peer['ps']:>5.2f}x")
    
    print("  " + "-" * 65)
    print(f"  {'Mean':<15} {peers['pe'].mean():>5.1f}x  {peers['ev_ebitda'].mean():>6.1f}x  {peers['ev_revenue'].mean():>5.2f}x  {peers['pb'].mean():>5.2f}x  {peers['ps'].mean():>5.2f}x")
    print(f"  {'Median':<15} {peers['pe'].median():>5.1f}x  {peers['ev_ebitda'].median():>6.1f}x  {peers['ev_revenue'].median():>5.2f}x  {peers['pb'].median():>5.2f}x  {peers['ps'].median():>5.2f}x")
    
    # Valuation using multiples
    print("\n" + "-" * 70)
    print("VALUATION USING MULTIPLES")
    print("-" * 70)
    
    # Using median multiples
    median_pe = peers['pe'].median()
    median_ev_ebitda = peers['ev_ebitda'].median()
    median_ev_revenue = peers['ev_revenue'].median()
    median_pb = peers['pb'].median()
    median_ps = peers['ps'].median()
    
    # Calculate implied values
    implied_equity_pe = target['net_income'] * median_pe
    implied_ev_ebitda = target['ebitda'] * median_ev_ebitda
    implied_ev_revenue = target['revenue'] * median_ev_revenue
    implied_equity_pb = target['book_value'] * median_pb
    implied_equity_ps = target['revenue'] * median_ps
    
    # Convert EV to equity
    implied_equity_ev_ebitda = implied_ev_ebitda - target['net_debt']
    implied_equity_ev_revenue = implied_ev_revenue - target['net_debt']
    
    # Per share
    implied_price_pe = implied_equity_pe / target['shares_outstanding']
    implied_price_ev_ebitda = implied_equity_ev_ebitda / target['shares_outstanding']
    implied_price_ev_revenue = implied_equity_ev_revenue / target['shares_outstanding']
    implied_price_pb = implied_equity_pb / target['shares_outstanding']
    implied_price_ps = implied_equity_ps / target['shares_outstanding']
    
    print("\n  Using Median Multiples:")
    print("\n  Method              Multiple    Enterprise Value    Equity Value    Share Price")
    print("  " + "-" * 75)
    print(f"  P/E                 {median_pe:>5.1f}x    ${implied_equity_pe:>10,.0f}M     ${implied_equity_pe:>10,.0f}M    ${implied_price_pe:>8.2f}")
    print(f"  EV/EBITDA           {median_ev_ebitda:>5.1f}x    ${implied_ev_ebitda:>10,.0f}M     ${implied_equity_ev_ebitda:>10,.0f}M    ${implied_price_ev_ebitda:>8.2f}")
    print(f"  EV/Revenue          {median_ev_revenue:>5.2f}x    ${implied_ev_revenue:>10,.0f}M     ${implied_equity_ev_revenue:>10,.0f}M    ${implied_price_ev_revenue:>8.2f}")
    print(f"  P/B                 {median_pb:>5.2f}x    N/A                ${implied_equity_pb:>10,.0f}M    ${implied_price_pb:>8.2f}")
    print(f"  P/S                 {median_ps:>5.2f}x    N/A                ${implied_equity_ps:>10,.0f}M    ${implied_price_ps:>8.2f}")
    
    # Summary
    print("\n" + "-" * 70)
    print("VALUATION SUMMARY")
    print("-" * 70)
    
    implied_prices = [implied_price_pe, implied_price_ev_ebitda, implied_price_ev_revenue, 
                      implied_price_pb, implied_price_ps]
    
    print(f"\n  Current Market Price:     ${target['stock_price']:.2f}")
    print(f"\n  Implied Price Range:")
    print(f"    Lowest:                  ${min(implied_prices):.2f}")
    print(f"    Highest:                 ${max(implied_prices):.2f}")
    print(f"    Average:                 ${np.mean(implied_prices):.2f}")
    print(f"    Median:                  ${np.median(implied_prices):.2f}")
    
    # Compare to current
    median_implied = np.median(implied_prices)
    upside = (median_implied - target['stock_price']) / target['stock_price']
    
    print(f"\n  Median Implied Price:     ${median_implied:.2f}")
    print(f"  Upside/(Downside):        {upside:+.1%}")
    
    # Discount/Premium analysis
    print("\n" + "-" * 70)
    print("DISCOUNT/PREMIUM ANALYSIS")
    print("-" * 70)
    
    print("\n  Target vs. Peer Median Multiples:")
    print(f"\n  {'Metric':<15} {'Target':<12} {'Peer Med':<12} {'Diff':<12} {'Premium/Disc':<15}")
    print(f"  {'-'*65}")
    print(f"  {'P/E':<15} {target_pe:<12.1f} {median_pe:<12.1f} {(target_pe/median_pe - 1):<12.1%} {(target_pe - median_pe):<+12.1f}x")
    print(f"  {'EV/EBITDA':<15} {target_ev_ebitda:<12.1f} {median_ev_ebitda:<12.1f} {(target_ev_ebitda/median_ev_ebitda - 1):<12.1%} {(target_ev_ebitda - median_ev_ebitda):<+12.1f}x")
    print(f"  {'EV/Rev':<15} {target_ev_revenue:<12.2f} {median_ev_revenue:<12.2f} {(target_ev_revenue/median_ev_revenue - 1):<12.1%} {(target_ev_revenue - median_ev_revenue):<+12.2f}x")
    print(f"  {'P/B':<15} {target_pb:<12.2f} {median_pb:<12.2f} {(target_pb/median_pb - 1):<12.1%} {(target_pb - median_pb):<+12.2f}x")
    print(f"  {'P/S':<15} {target_ps:<12.2f} {median_ps:<12.2f} {(target_ps/median_ps - 1):<12.1%} {(target_ps - median_ps):<+12.2f}x")
    
    print("\n  Interpretation:")
    if target_pe < median_pe:
        print(f"    P/E: Trading at {target_pe/median_pe:.0%} of peers (discount)")
    else:
        print(f"    P/E: Trading at {target_pe/median_pe:.0%} of peers (premium)")
    
    print("\n" + "=" * 70)
    
    return {
        'median_implied_price': median_implied,
        'current_price': target['stock_price'],
        'upside': upside
    }

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    results = run_comps_analysis()
