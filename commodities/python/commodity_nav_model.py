"""
Commodity Company NAV/DCF Model
===============================
Values oil & gas or mining companies using NAV (Net Asset Value) methodology.

USAGE:
------
1. Modify the INPUTS with the commodity company's data
2. Run the script
3. Review NAV breakdown and valuation

This model uses a simplified DCF approach tailored for commodity companies,
accounting for reserves, production profiles, and commodity prices.
"""

import pandas as pd
import numpy as np

# =============================================================================
# INPUTS - Modify these values for your commodity company
# =============================================================================

# Company Information
company_name = "OilCo Inc."
current_stock_price = 18.50       # Current share price ($)
shares_outstanding = 100            # Shares outstanding (millions)

# Reserve Data (for oil/gas use "boe" - barrels of oil equivalent)
reserves_1p = 150                  # Proven reserves (MMboe)
reserves_2p = 225                  # Proven + Probable (MMboe)

# Production Profile
initial_production = 20             # Initial annual production (MMboe)
decline_rate = 0.04                # Annual production decline (4%)

# Price Assumptions
current_commodity_price = 75        # Current oil price ($/bbl)
long_term_price = 65                # Long-term oil price ($/bbl)
price_escalation = 0.02            # Annual price escalation (2%)

# Cost Assumptions
operating_cost_per_unit = 28       # Operating cost per boe ($)
transport_cost_per_unit = 5        # Transport cost per boe ($)
total_cost_per_unit = operating_cost_per_unit + transport_cost_per_unit

capex_annual = 200                 # Annual capital expenditure ($M)

# Corporate Costs
corporate_overhead = 30            # Annual corporate overhead ($M)
net_debt = 800                    # Net debt ($M)

# Valuation Parameters
discount_rate = 0.10              # Discount rate (WACC)
terminal_growth = 0.02            # Terminal growth rate (2%)

# =============================================================================
# CALCULATION ENGINE
# =============================================================================

def project_production_valuation(years=10):
    """Project production and calculate cash flows"""
    
    projections = []
    
    for year in range(1, years + 1):
        # Production with decline
        production = initial_production * ((1 - decline_rate) ** (year - 1))
        
        # Price with escalation
        if year <= 3:
            # Near-term prices
            price = current_commodity_price * ((1 + price_escalation) ** (year - 1))
        else:
            # Transition to long-term
            price = long_term_price
        
        # Revenue
        revenue = production * price
        
        # Operating costs
        opex = production * total_cost_per_unit
        
        # EBITDA
        ebitda = revenue - opex
        
        # CAPEX
        capex = capex_annual * ((1 - 0.05) ** (year - 1))  # Slight decline in capex
        
        # FCF (simplified - ignoring working capital)
        fcf = ebitda - capex - corporate_overhead
        
        # Discount factor
        discount_factor = 1 / ((1 + discount_rate) ** year)
        
        # Present value
        pv = fcf * discount_factor
        
        projections.append({
            'Year': year,
            'Production (MMboe)': production,
            'Price ($/bbl)': price,
            'Revenue ($M)': revenue,
            'Opex ($M)': opex,
            'EBITDA ($M)': ebitda,
            'CAPEX ($M)': capex,
            'FCF ($M)': fcf,
            'Discount Factor': discount_factor,
            'PV ($M)': pv
        })
    
    return pd.DataFrame(projections)

def calculate_terminal_value(final_fcf, g, r):
    """Calculate terminal value using Gordon Growth"""
    return (final_fcf * (1 + g)) / (r - g)

def run_nav_valuation():
    """Main NAV valuation function"""
    
    print("=" * 70)
    print(f"COMMODITY COMPANY NAV MODEL: {company_name}")
    print("=" * 70)
    
    # Display inputs
    print("\n" + "-" * 70)
    print("INPUT PARAMETERS")
    print("-" * 70)
    
    print(f"\n  Reserve Data:")
    print(f"    Proven (1P):           {reserves_1p} MMboe")
    print(f"    Proven + Probable (2P): {reserves_2p} MMboe")
    print(f"    Reserve Life:          {reserves_2p / initial_production:.1f} years")
    
    print(f"\n  Production:")
    print(f"    Initial Production:    {initial_production} MMboe/year")
    print(f"    Decline Rate:          {decline_rate:.1%}")
    
    print(f"\n  Pricing:")
    print(f"    Current Price:         ${current_commodity_price}/bbl")
    print(f"    Long-term Price:       ${long_term_price}/bbl")
    print(f"    Price Escalation:      {price_escalation:.1%}")
    
    print(f"\n  Costs:")
    print(f"    Operating Cost:        ${operating_cost_per_unit}/boe")
    print(f"    Transport Cost:        ${transport_cost_per_unit}/boe")
    print(f"    Total Unit Cost:       ${total_cost_per_unit}/boe")
    print(f"    Annual CAPEX:          ${capex_annual}M")
    print(f"    Corporate Overhead:    ${corporate_overhead}M/year")
    
    print(f"\n  Valuation:")
    print(f"    Discount Rate (WACC): {discount_rate:.1%}")
    print(f"    Terminal Growth:      {terminal_growth:.1%}")
    
    # Project cash flows
    print("\n" + "-" * 70)
    print("CASH FLOW PROJECTIONS")
    print("-" * 70)
    
    df = project_production_valuation(years=10)
    
    print(f"\n  Year  Prod    Price    Revenue   Opex    EBITDA   CAPEX    FCF      PV")
    print(f"       (MMboe) ($/bbl)  ($M)      ($M)    ($M)     ($M)    ($M)     ($M)")
    print("  " + "-" * 80)
    
    for _, row in df.iterrows():
        print(f"    {int(row['Year']):>2}   {row['Production (MMboe)']:>5.1f}   ${row['Price ($/bbl)']:>5.0f}   ${row['Revenue ($M)']:>6.0f}  ${row['Opex ($M)']:>5.0f}  ${row['EBITDA ($M)']:>6.0f}  ${row['CAPEX ($M)']:>5.0f}  ${row['FCF ($M)']:>5.0f}  ${row['PV ($M)']:>6.0f}")
    
    # Sum of PV
    sum_pv = df['PV ($M)'].sum()
    
    print("  " + "-" * 80)
    print(f"  Sum PV (Years 1-10):                           ${sum_pv:>6.0f}M")
    
    # Terminal Value
    print("\n" + "-" * 70)
    print("TERMINAL VALUE")
    print("-" * 70)
    
    final_fcf = df.iloc[-1]['FCF ($M)']
    final_df = df.iloc[-1]['Discount Factor']
    
    tv = calculate_terminal_value(final_fcf, terminal_growth, discount_rate)
    pv_tv = tv * final_df
    
    print(f"\n  Final Year FCF:         ${final_fcf:.0f}M")
    print(f"  Terminal Value:         ${tv:.0f}M")
    print(f"  PV of Terminal Value:  ${pv_tv:.0f}M")
    
    # NAV Calculation
    print("\n" + "-" * 70)
    print("NET ASSET VALUE (NAV) CALCULATION")
    print("-" * 70)
    
    print(f"\n  PV of Cash Flows (Yrs 1-10):  ${sum_pv:,.0f}M")
    print(f"  PV of Terminal Value:        ${pv_tv:,.0f}M")
    print(f"  Total Enterprise Value:      ${sum_pv + pv_tv:,.0f}M")
    print(f"  Less: Net Debt:             ${net_debt:,.0f}M")
    print(f"  Equity Value:               ${sum_pv + pv_tv - net_debt:,.0f}M")
    
    # Per share
    equity_value = sum_pv + pv_tv - net_debt
    implied_price = equity_value / shares_outstanding
    upside = (implied_price - current_stock_price) / current_stock_price
    
    print(f"\n  Shares Outstanding:        {shares_outstanding}M")
    print(f"  Implied Share Price:       ${implied_price:.2f}")
    print(f"  Current Share Price:       ${current_stock_price:.2f}")
    print(f"  Upside/(Downside):         {upside:+.1%}")
    
    # Metrics
    print("\n" + "-" * 70)
    print("KEY VALUATION METRICS")
    print("-" * 70)
    
    total_ev = sum_pv + pv_tv
    total_2p = reserves_2p
    
    ev_2p = total_ev / total_2p
    ev_production = total_ev / initial_production
    
    print(f"\n  Total Enterprise Value:     ${total_ev:,.0f}M")
    print(f"  EV/2P Reserves:            ${ev_2p:.2f}/boe")
    print(f"  EV/Annual Production:      ${ev_production:.2f}/boe")
    
    # Price sensitivity
    print("\n" + "-" * 70)
    print("SENSITIVITY ANALYSIS")
    print("Implied Price vs. Long-term Price & Discount Rate")
    print("-" * 70)
    
    sensitivities = []
    
    for lt_price in [55, 60, 65, 70, 75]:
        for disc_rate in [0.08, 0.09, 0.10, 0.11, 0.12]:
            # Recalculate with different assumptions
            df_new = []
            for year in range(1, 11):
                production = initial_production * ((1 - decline_rate) ** (year - 1))
                if year <= 3:
                    price = current_commodity_price * ((1 + price_escalation) ** (year - 1))
                else:
                    price = lt_price
                
                revenue = production * price
                opex = production * total_cost_per_unit
                ebitda = revenue - opex
                capex = capex_annual * ((1 - 0.05) ** (year - 1))
                fcf = ebitda - capex - corporate_overhead
                discount_factor = 1 / ((1 + disc_rate) ** year)
                pv = fcf * discount_factor
                df_new.append(pv)
            
            sum_pv_new = sum(df_new)
            final_fcf_new = df_new[-1] * (1 + terminal_growth) * (1 + disc_rate) / (disc_rate - terminal_growth)
            final_df_new = 1 / ((1 + disc_rate) ** 10)
            pv_tv_new = final_fcf_new * final_df_new
            
            ev_new = sum_pv_new + pv_tv_new
            equity_new = ev_new - net_debt
            price_new = equity_new / shares_outstanding
            
            sensitivities.append({
                'Long-term Price': lt_price,
                'Discount Rate': disc_rate,
                'Implied Price': price_new
            })
    
    sens_df = pd.DataFrame(sensitivities)
    pivot = sens_df.pivot(index='Long-term Price', columns='Discount Rate', values='Implied Price')
    print("\n" + pivot.round(2).to_string())
    
    # Break-even analysis
    print("\n" + "-" * 70)
    print("BREAK-EVEN ANALYSIS")
    print("-" * 70)
    
    # Find price needed for current stock price
    target_equity = current_stock_price * shares_outstanding + net_debt
    
    print(f"\n  Target Enterprise Value:   ${target_equity:,.0f}M")
    print(f"  Required PV of FCFs:       ${target_equity - pv_tv:,.0f}M")
    print(f"\n  This implies a break-even long-term price of approximately: ${long_term_price}M")
    
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
    results = run_nav_valuation()
