"""
RESOURCE NAV MODEL (Net Asset Value)
====================================
This model values a commodity deposit (e.g., a gold mine) by calculating 
the present value of extracting all resources.

HOW TO USE:
-----------
1. Edit the 'INPUTS' section with the resource deposit data.
2. Run the script to see the 'Net Asset Value' (NAV) of the deposit.
"""

def calculate_resource_nav():
    # --- INPUTS ---
    print("--- 1. RESOURCE DEPOSIT DATA ---")
    # REPLACE WITH THE DEPOSIT/COMMODITY YOU ARE EVALUATING
    deposit_name = "[ENTER DEPOSIT NAME]"
    commodity = "[ENTER COMMODITY TYPE]"
    
    total_reserves = 1000000  # ounces of gold
    grade = 5.0               # grams per tonne (simplified)
    
    spot_price = 2000         # $/oz current spot price
    long_term_price = 1800   # $/oz (conservative long-term forecast)
    aisc = 1200              # All-In Sustaining Cost ($/oz)
    
    annual_production = 100000  # ounces per year
    mine_life = 10              # years
    
    discount_rate = 0.10  # 10% required return

    print(f"\nValuing {deposit_name} ({commodity})...")
    print(f"Total Reserves: {total_reserves:,} oz")
    print(f"Long-term Price: ${long_term_price}/oz | AISC: ${aisc}/oz")

    # --- ANNUAL CASH FLOW ---
    print("\n--- 2. ANNUAL CASH FLOW PROJECTION ($M) ---")
    print(f"{'Year':<6} | {'Production':<12} | {'Revenue':<12} | {'Cost':<12} | {'CF':<12} | {'PV':<12}")
    print("-" * 75)

    total_pv = 0
    
    for year in range(1, mine_life + 1):
        revenue = annual_production * long_term_price / 1000000
        cost = annual_production * aisc / 1000000
        cash_flow = revenue - cost
        pv = cash_flow / ((1 + discount_rate) ** year)
        total_pv += pv
        
        print(f"{year:<6} | {annual_production:<12,} | ${revenue:<11.2f}M | ${cost:<11.2f}M | ${cash_flow:<11.2f}M | ${pv:<11.2f}M")

    # --- VALUATION SUMMARY ---
    print("\n--- 3. VALUATION SUMMARY ---")
    print(f"Present Value (NAV):          ${total_pv:.1f} M")
    print(f"Value per Ounce:              ${total_pv * 1000000 / total_reserves:.2f}/oz")

    print("\n--- HIGH RETENTION RECAP ---")
    print("1. We calculate how much profit (Revenue - Cost) the mine makes each year.")
    print("2. We bring all future cash flows back to today's dollars (Present Value).")
    print("3. The total is the 'NAV' - what this pile of gold in the ground is worth today.")

if __name__ == "__main__":
    calculate_resource_nav()
