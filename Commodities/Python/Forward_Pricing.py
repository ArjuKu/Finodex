"""
FORWARD PRICING CALCULATOR
==========================
This model calculates the forward (future) price of a commodity 
based on the Cost of Carry model.

HOW TO USE:
-----------
1. Edit the 'INPUTS' section with commodity and market data.
2. Run the script to see the 'Forward Price' and understand contango/backwardation.
"""

def calculate_forward_price():
    # --- INPUTS ---
    print("--- 1. COMMODITY DATA ---")
    commodity = "Crude Oil"
    spot_price = 75.00          # $/barrel today
    
    storage_cost = 2.00         # $/barrel per year
    insurance_cost = 0.50       # $/barrel per year
    financing_rate = 0.05       # 5% annual interest rate
    
    months_forward = 6

    print(f"\nCalculating Forward Price for {commodity}...")
    print(f"Current Spot Price: ${spot_price:.2f}")
    print(f"Delivery in: {months_forward} months")

    # --- COST OF CARRY ---
    annual_carry = storage_cost + insurance_cost + (spot_price * financing_rate)
    monthly_carry = annual_carry / 12
    
    total_cost_of_carry = monthly_carry * months_forward
    forward_price = spot_price + total_cost_of_carry

    print("\n--- 2. COST OF CARRY BREAKDOWN ---")
    print(f"Storage Cost:      ${storage_cost:.2f}/year")
    print(f"Insurance Cost:   ${insurance_cost:.2f}/year")
    print(f"Financing Cost:   ${spot_price * financing_rate:.2f}/year (at {financing_rate*100:.0f}%)")
    print(f"Total Annual Carry: ${annual_carry:.2f}")
    print(f"Carry for {months_forward} months:  ${total_cost_of_carry:.2f}")

    print("\n--- 3. FORWARD PRICING ---")
    print(f"Spot Price:       ${spot_price:.2f}")
    print(f"+ Cost of Carry: +${total_cost_of_carry:.2f}")
    print("-" * 25)
    print(f"FORWARD PRICE:    ${forward_price:.2f}")

    # --- INTERPRETATION ---
    print("\n--- 4. MARKET CONDITIONS ---")
    if forward_price > spot_price:
        print("CONTANGO: Forward > Spot")
        print("The market expects prices to RISE in the future.")
    elif forward_price < spot_price:
        print("BACKWARDATION: Forward < Spot")
        print("The market expects prices to FALL in the future.")
    else:
        print("NORMAL MARKET: Forward = Spot")

    print("\n--- HIGH RETENTION RECAP ---")
    print("1. The Forward Price is the Spot Price plus the 'Cost of Carry' (storage + insurance + interest).")
    print("2. If Forward > Spot, the market is in 'Contango' (expecting higher prices).")
    print("3. If Forward < Spot, the market is in 'Backwardation' (expecting lower prices).")

if __name__ == "__main__":
    calculate_forward_price()
