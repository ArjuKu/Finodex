"""
CORPORATE FP&A - BUDGET VS. ACTUAL TRACKER
==========================================
Financial Planning & Analysis (FP&A) is the internal "counting" part of 
a company. This tool helps you track whether you are spending more or 
less than you planned.

HOW TO USE:
-----------
1. Enter your Budgeted amounts in the dictionary below.
2. Enter your Actual amounts.
3. The model calculates the 'Variance' (the difference).
"""

def track_budget():
    # --- INPUTS ---
    print("--- 1. COMPANY BUDGET INPUTS ---")
    company_name = "FutureVentures Ltd."
    
    # Category: (Budgeted, Actual)
    finances = {
        "Marketing": (50000, 52000),
        "Sales Team": (120000, 115000),
        "Office Rent": (30000, 31000),
        "Software Subscriptions": (10000, 15000),
        "Miscellaneous": (5000, 3000)
    }

    print(f"\nAnalyzing {company_name} Budget vs. Actual...")
    print(f"{'Category':<25} | {'Budget':<10} | {'Actual':<10} | {'Variance':<10} | {'% Var':<10}")
    print("-" * 75)

    total_budget = 0
    total_actual = 0

    for category, (budget, actual) in finances.items():
        total_budget += budget
        total_actual += actual
        
        variance = budget - actual
        percent_var = (variance / budget) * 100
        
        print(f"{category:<25} | ${budget:<9} | ${actual:<9} | ${variance:<9} | {percent_var:>8.1f}%")

    total_variance = total_budget - total_actual
    total_percent_var = (total_variance / total_budget) * 100
    
    print("-" * 75)
    print(f"{'TOTAL EXPENSES':<25} | ${total_budget:<9} | ${total_actual:<9} | ${total_variance:<9} | {total_percent_var:>8.1f}%")

    print("\n--- 2. FP&A SUMMARY ---")
    if total_actual > total_budget:
        print(f"Outcome: {company_name} is OVER budget by ${abs(total_variance)}.")
    else:
        print(f"Outcome: {company_name} is UNDER budget by ${abs(total_variance)}.")

    print("\n--- HIGH RETENTION RECAP ---")
    print("1. FP&A is about predicting the future (Budget) and tracking the truth (Actual).")
    print("2. The difference between the two is called a 'Variance'.")
    print("3. By tracking variances, a company knows when they are spending too much.")

if __name__ == "__main__":
    track_budget()
