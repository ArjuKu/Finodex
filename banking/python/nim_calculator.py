"""
Net Interest Margin (NIM) Calculator
====================================
Calculates and analyzes Net Interest Margin for banks.

USAGE:
------
1. Modify the INPUTS section with your bank's data
2. Run the script
3. Review NIM breakdown and rate sensitivity analysis

NIM = (Interest Income - Interest Expense) / Interest-Earning Assets
"""

import pandas as pd
import numpy as np

# =============================================================================
# INPUTS - Modify these values for your bank
# =============================================================================

# Interest-Earning Assets (in $ millions)
cash_equivalents = 500
investment_securities = 2000
loans_commercial = 5000
loans_residential = 3000
loans_consumer = 1500
other_earning_assets = 500

total_earning_assets = (cash_equivalents + investment_securities + 
                        loans_commercial + loans_residential + 
                        loans_consumer + other_earning_assets)

# Interest-Bearing Liabilities (in $ millions)
demand_deposits = 2000
savings_deposits = 3000
time_deposits = 3500
short_term_borrowings = 1500
long_term_debt = 2000

total_interest_liabilities = (demand_deposits + savings_deposits + 
                             time_deposits + short_term_borrowings + 
                             long_term_debt)

# Interest Rates (annual rates as decimals)
rates = {
    'cash_equivalents': 0.045,      # 4.5%
    'investment_securities': 0.042,  # 4.2%
    'loans_commercial': 0.065,      # 6.5%
    'loans_residential': 0.060,     # 6.0%
    'loans_consumer': 0.085,       # 8.5%
    'other_earning': 0.050,        # 5.0%
    'demand_deposits': 0.005,      # 0.5%
    'savings_deposits': 0.025,     # 2.5%
    'time_deposits': 0.045,        # 4.5%
    'short_term_borrowings': 0.055, # 5.5%
    'long_term_debt': 0.050        # 5.0%
}

# Rate Change Scenarios (basis points change)
rate_scenarios = [ -200, -100, -50, 0, 50, 100, 200 ]

# =============================================================================
# CALCULATION ENGINE
# =============================================================================

def calculate_interest_income():
    """Calculate total interest income"""
    income = {
        'Cash & Equivalents': cash_equivalents * rates['cash_equivalents'],
        'Investment Securities': investment_securities * rates['investment_securities'],
        'Commercial Loans': loans_commercial * rates['loans_commercial'],
        'Residential Loans': loans_residential * rates['loans_residential'],
        'Consumer Loans': loans_consumer * rates['loans_consumer'],
        'Other Earning Assets': other_earning_assets * rates['other_earning']
    }
    return income

def calculate_interest_expense():
    """Calculate total interest expense"""
    expense = {
        'Demand Deposits': demand_deposits * rates['demand_deposits'],
        'Savings Deposits': savings_deposits * rates['savings_deposits'],
        'Time Deposits': time_deposits * rates['time_deposits'],
        'Short-Term Borrowings': short_term_borrowings * rates['short_term_borrowings'],
        'Long-Term Debt': long_term_debt * rates['long_term_debt']
    }
    return expense

def calculate_nim(interest_income, interest_expense):
    """Calculate Net Interest Margin"""
    net_interest_income = interest_income - interest_expense
    nim = net_interest_income / total_earning_assets
    return nim, net_interest_income

def run_nim_analysis():
    """Main NIM analysis function"""
    
    print("=" * 70)
    print("NET INTEREST MARGIN (NIM) CALCULATOR")
    print("=" * 70)
    
    # Current NIM Calculation
    print("\n" + "-" * 70)
    print("INTEREST INCOME BREAKDOWN")
    print("-" * 70)
    
    income_dict = calculate_interest_income()
    total_income = sum(income_dict.values())
    
    for item, amount in income_dict.items():
        pct = amount / total_income * 100
        print(f"  {item:<25} ${amount:>10,.1f}M  ({pct:>5.1f}%)")
    
    print(f"  {'TOTAL':<25} ${total_income:>10,.1f}M")
    
    print("\n" + "-" * 70)
    print("INTEREST EXPENSE BREAKDOWN")
    print("-" * 70)
    
    expense_dict = calculate_interest_expense()
    total_expense = sum(expense_dict.values())
    
    for item, amount in expense_dict.items():
        pct = amount / total_expense * 100
        print(f"  {item:<25} ${amount:>10,.1f}M  ({pct:>5.1f}%)")
    
    print(f"  {'TOTAL':<25} ${total_expense:>10,.1f}M")
    
    # NIM Summary
    nim, nii = calculate_nim(total_income, total_expense)
    
    print("\n" + "-" * 70)
    print("NIM SUMMARY")
    print("-" * 70)
    print(f"  Total Interest Income:      ${total_income:,.1f}M")
    print(f"  Total Interest Expense:     ${total_expense:,.1f}M")
    print(f"  Net Interest Income:         ${nii:,.1f}M")
    print(f"  Total Earning Assets:        ${total_earning_assets:,.1f}M")
    print(f"\n  NET INTEREST MARGIN:         {nim:.2%}")
    
    # Additional Metrics
    print("\n" + "-" * 70)
    print("ADDITIONAL METRICS")
    print("-" * 70)
    
    # Interest Spread (difference between avg asset yield and liability cost)
    avg_asset_yield = total_income / total_earning_assets
    avg_liability_cost = total_expense / total_interest_liabilities
    interest_spread = avg_asset_yield - avg_liability_cost
    
    print(f"  Average Asset Yield:         {avg_asset_yield:.2%}")
    print(f"  Average Liability Cost:     {avg_liability_cost:.2%}")
    print(f"  Interest Spread:             {interest_spread:.2%}")
    
    # Rate Sensitivity Analysis
    print("\n" + "-" * 70)
    print("RATE SENSITIVITY ANALYSIS")
    print("Impact of Interest Rate Changes on NIM")
    print("-" * 70)
    
    print(f"\n{'Rate Change':<15} {'New NIM':<15} {'Change':<15} {'NII Impact':<15}")
    print("-" * 70)
    
    base_nim = nim
    base_nii = nii
    
    for change in rate_scenarios:
        # Approximate NIM impact (simplified: 0.35% NIM change per 1% rate change)
        nim_change = change * 0.00035  # 35% of basis point change
        new_nim = base_nim + nim_change
        new_nii = new_nim * total_earning_assets
        
        change_str = f"{nim_change:.2%}"
        impact_str = f"${new_nii - base_nii:+,.0f}M"
        
        print(f"  {change:+5} bps      {new_nim:.2%}         {change_str:>10}    {impact_str:>12}")
    
    # Asset-Liability Mix
    print("\n" + "-" * 70)
    print("ASSET-LIABILITY MIX")
    print("-" * 70)
    
    print(f"\n  Earning Assets:              ${total_earning_assets:,.0f}M")
    print(f"  Interest Liabilities:         ${total_interest_liabilities:,.0f}M")
    print(f"  Spread (Assets - Liab):      ${total_earning_assets - total_interest_liabilities:,.0f}M")
    
    # Deposit Breakdown
    total_deposits = demand_deposits + savings_deposits + time_deposits
    print(f"\n  Deposit Mix:")
    print(f"    Demand:    {demand_deposits/total_deposits:>6.1%}  (${demand_deposits:,.0f}M)")
    print(f"    Savings:   {savings_deposits/total_deposits:>6.1%}  (${savings_deposits:,.0f}M)")
    print(f"    Time:      {time_deposits/total_deposits:>6.1%}  (${time_deposits:,.0f}M)")
    
    print("\n" + "=" * 70)

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    run_nim_analysis()
