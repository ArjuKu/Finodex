"""
IPO PRICING - COMPARABLES MODEL
================================
When a company goes public, an investment bank helps set the price. 
This tool calculates an IPO price range based on peer multiples.

HOW TO USE:
-----------
1. Edit the 'INPUTS' section with the target company's earnings and peer multiples.
2. Run the script to see the 'IPO Price Range' and 'IPO Discount'.
"""

def calculate_ipo_pricing():
    # --- INPUTS ---
    print("--- 1. IPO DATA INPUTS ---")
    company_name = "CloudFlow Tech"
    target_earnings = 50.0    # $ in millions (Last 12 Months)
    shares_to_issue = 10.0    # millions of shares to be issued
    
    # Peer Data: (Name, P/E Multiple)
    peers = {
        "Peer A": 25.0,
        "Peer B": 22.0,
        "Peer C": 28.0,
        "Peer D": 24.0
    }
    
    ipo_discount_pct = 0.15   # 15% discount to fair value

    print(f"\nPricing the IPO for {company_name}...")
    
    # --- CALCULATE MEDIAN PE MULTIPLE ---
    multiples = sorted(peers.values())
    n = len(multiples)
    median_pe = (multiples[n//2 - 1] + multiples[n//2]) / 2 if n % 2 == 0 else multiples[n//2]

    print(f"Peer Group Median P/E: {median_pe:.1f}x")

    # --- VALUATION & PRICING ---
    fair_value_equity = target_earnings * median_pe
    fair_price_per_share = fair_value_equity / shares_to_issue
    
    ipo_price_per_share = fair_price_per_share * (1 - ipo_discount_pct)
    ipo_discount_amount = fair_price_per_share - ipo_price_per_share

    print(f"\n--- 2. PRICING SUMMARY ---")
    print(f"Fair Value (Based on Peers): ${fair_value_equity:.1f} M")
    print(f"Fair Price Per Share:        ${fair_price_per_share:.2f}")
    print(f"IPO Discount (15%):         -${ipo_discount_amount:.2f}")
    print("-" * 35)
    print(f"RECOMMENDED IPO PRICE:       ${ipo_price_per_share:.2f}")

    total_proceeds = ipo_price_per_share * shares_to_issue
    print(f"\nEstimated Capital Raised:    ${total_proceeds:.1f} M")

    print("\n--- HIGH RETENTION RECAP ---")
    print("1. We look at what similar companies are 'trading' at (Peer P/E Ratios).")
    print("2. We multiply the target's earnings by that ratio to find its 'Fair Value'.")
    print("3. We subtract a 10-15% discount to make the price attractive to new investors.")

if __name__ == "__main__":
    calculate_ipo_pricing()
