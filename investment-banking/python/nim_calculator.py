"""
================================================================================
NET INTEREST MARGIN (NIM) CALCULATOR - TEMPLATE
================================================================================

What this does:
    Calculates Net Interest Margin for a bank.
    NIM = (Interest Income - Interest Expense) / Interest-Earning Assets

USAGE:
    1. Modify the INPUTS section below with your bank's data
    2. Run: python nim_calculator.py
    3. Review NIM breakdown and rate sensitivity analysis

INPUTS TO MODIFY:
    - earning_assets: Amount of interest-earning assets ($ millions)
    - interest_income: Total interest income ($ millions)
    - interest_expense: Total interest expense ($ millions)
    - rates: Interest rates for different asset/liability types

For help: See BANK_VALUATION_TUTORIAL.md
================================================================================
"""

# =============================================================================
# SECTION 1: INPUTS - Change these values for your bank
# =============================================================================

# Interest-Earning Assets ($ millions)
cash_equivalents = 500
investment_securities = 2000
loans_commercial = 5000
loans_residential = 3000
loans_consumer = 1500
other_earning_assets = 500

# Calculate total earning assets
total_earning_assets = (cash_equivalents + investment_securities + 
                        loans_commercial + loans_residential + 
                        loans_consumer + other_earning_assets)

# Interest-Bearing Liabilities ($ millions)
demand_deposits = 2000
savings_deposits = 3000
time_deposits = 3500
short_term_borrowings = 1500
long_term_debt = 2000

total_liabilities = (demand_deposits + savings_deposits + 
                     time_deposits + short_term_borrowings + 
                     long_term_debt)

# Interest Rates (annual, as decimals - e.g., 0.05 = 5%)
rates = {
    'cash': 0.045,        # Cash equivalent yield (4.5%)
    'securities': 0.042,   # Investment securities yield (4.2%)
    'commercial_loans': 0.065,   # Commercial loan rate (6.5%)
    'residential_loans': 0.060,  # Residential loan rate (6.0%)
    'consumer_loans': 0.085,     # Consumer loan rate (8.5%)
    'demand_deposits': 0.005,    # Demand deposit rate (0.5%)
    'savings_deposits': 0.025,   # Savings account rate (2.5%)
    'time_deposits': 0.045,      # Time deposit rate (4.5%)
    'short_term_borrow': 0.055,  # Short-term borrowing rate (5.5%)
    'long_term_debt': 0.050       # Long-term debt rate (5.0%)
}

# =============================================================================
# SECTION 2: CALCULATION ENGINE
# =============================================================================

def calculate_interest_income():
    """Calculate total interest income from each asset category"""
    income = {
        'Cash': cash_equivalents * rates['cash'],
        'Securities': investment_securities * rates['securities'],
        'Commercial Loans': loans_commercial * rates['commercial_loans'],
        'Residential Loans': loans_residential * rates['residential_loans'],
        'Consumer Loans': loans_consumer * rates['consumer_loans'],
        'Other': other_earning_assets * rates.get('cash', 0.05)
    }
    return income

def calculate_interest_expense():
    """Calculate total interest expense from each liability category"""
    expense = {
        'Demand Deposits': demand_deposits * rates['demand_deposits'],
        'Savings Deposits': savings_deposits * rates['savings_deposits'],
        'Time Deposits': time_deposits * rates['time_deposits'],
        'Short-term Borrowings': short_term_borrowings * rates['short_term_borrow'],
        'Long-term Debt': long_term_debt * rates['long_term_debt']
    }
    return expense

def calculate_nim():
    """
    Calculate Net Interest Margin
    
    Formula: NIM = (Interest Income - Interest Expense) / Interest-Earning Assets
    
    This measures the spread the bank earns on its lending vs. funding costs.
    """
    income = calculate_interest_income()
    expense = calculate_interest_expense()
    
    total_income = sum(income.values())
    total_expense = sum(expense.values())
    
    net_interest_income = total_income - total_expense
    nim = net_interest_income / total_earning_assets
    
    return nim, net_interest_income, income, expense

# =============================================================================
# SECTION 3: MAIN EXECUTION
# =============================================================================

def run_analysis():
    """Run the NIM analysis"""
    
    print("=" * 70)
    print("NET INTEREST MARGIN (NIM) CALCULATOR")
    print("=" * 70)
    
    # Get NIM and components
    nim, nii, income_dict, expense_dict = calculate_nim()
    
    total_income = sum(income_dict.values())
    total_expense = sum(expense_dict.values())
    
    # Display Interest Income Breakdown
    print("\n>>> INTEREST INCOME BREAKDOWN")
    print("-" * 50)
    for item, amount in income_dict.items():
        pct = (amount / total_income * 100) if total_income > 0 else 0
        print(f"    {item:<20} ${amount:>8,.1f}M  ({pct:>5.1f}%)")
    print(f"    {'TOTAL':<20} ${total_income:>8,.1f}M")
    
    # Display Interest Expense Breakdown
    print("\n>>> INTEREST EXPENSE BREAKDOWN")
    print("-" * 50)
    for item, amount in expense_dict.items():
        pct = (amount / total_expense * 100) if total_expense > 0 else 0
        print(f"    {item:<20} ${amount:>8,.1f}M  ({pct:>5.1f}%)")
    print(f"    {'TOTAL':<20} ${total_expense:>8,.1f}M")
    
    # Display NIM Summary
    print("\n>>> NIM SUMMARY")
    print("-" * 50)
    print(f"    Total Interest Income:    ${total_income:,.1f}M")
    print(f"    Total Interest Expense:  ${total_expense:,.1f}M")
    print(f"    Net Interest Income:     ${nii:,.1f}M")
    print(f"    Total Earning Assets:    ${total_earning_assets:,.1f}M")
    print(f"\n    >>> NET INTEREST MARGIN: {nim:.2%}")
    
    # Calculate key metrics
    avg_asset_yield = total_income / total_earning_assets
    avg_liability_cost = total_expense / total_liabilities
    interest_spread = avg_asset_yield - avg_liability_cost
    
    print("\n>>> ADDITIONAL METRICS")
    print("-" * 50)
    print(f"    Average Asset Yield:      {avg_asset_yield:.2%}")
    print(f"    Average Liability Cost:   {avg_liability_cost:.2%}")
    print(f"    Interest Spread:         {interest_spread:.2%}")
    
    # Rate Sensitivity
    print("\n>>> RATE SENSITIVITY")
    print("-" * 50)
    print("    If interest rates change by:")
    print("    Rate Change    New NIM    Impact")
    print("    -----------    -------    ------")
    
    # Simple sensitivity: NIM changes roughly 0.35% for every 1% rate change
    base_nim = nim
    for change in [-200, -100, -50, 0, 50, 100, 200]:
        change_pct = change / 10000  # Convert bps to decimal
        new_nim = base_nim + (change_pct * 0.35)
        impact = new_nim - base_nim
        print(f"    {change:+5} bps      {new_nim:.2%}     {impact:+.2%}")
    
    print("\n" + "=" * 70)
    print("MODIFIED INPUTS TO RUN FOR DIFFERENT BANKS")
    
    return nim

# =============================================================================
# RUN THE MODEL
# =============================================================================

if __name__ == "__main__":
    print("\nRunning NIM Calculator...")
    print("To modify: Change values in the INPUTS section\n")
    result = run_analysis()
