# Investment Banking - Pricing Models

**Objective:** Setting the "Actual Price Tag" for a transaction.

---

## Table of Contents

1. [The "Luxury Car" Metaphor](#the-luxury-car-metaphor)
2. [Valuation vs. Pricing](#valuation-vs-pricing)
3. [IPO Pricing - The "First Date"](#ipo-pricing---the-first-date)
4. [M&A Pricing - The "Synergy Premium"](#ma-pricing---the-synergy-premium)
5. [Peer Multiples - The "Real Estate Comps"](#peer-multiples---the-real-estate-comps)
6. [Corporate FP&A - The Internal GPS](#corporate-fpanda---the-internal-gps)
7. [Final Recap](#final-recap)

---

## The "Luxury Car" Metaphor

Imagine you want to buy a **vintage Porsche 911**.

- **Valuation**: You open the Kelly Blue Book. It tells you the car is worth $80,000 based on its age, mileage, and condition.
- **Pricing**: You go to the auction. Two collectors start bidding. The final price is $110,000.

> **💡 Schweser Note:** In Investment Banking, **Valuation** is the math (the Blue Book), but **Pricing** is the "auction"—where a willing buyer and seller shake hands. The Price is almost always higher than the Value because of competition, emotion, and strategic value.

---

## Valuation vs. Pricing

| Concept | Definition | Analogy |
|---------|------------|--------|
| **Valuation** | "What is it worth?" (The Math) | Kelly Blue Book |
| **Pricing** | "What will it sell for?" (The Deal) | Auction Price |

> **Key Insight:** A banker builds a valuation model to find a "fair range." But the MD (Managing Director) looks at that range and picks a price that will get the deal done.

---

## IPO Pricing - The "First Date"

When a company goes public (IPO), an investment bank helps set the price for the first day of trading.

### The "IPO Pop" Strategy

Banks **intentionally underprice** the IPO by 10-15%.

> **💡 Schweser Note (The "First Date"):** Think of an IPO like a first date. If you take the investor to an expensive restaurant and the food is mediocre, they leave angry. If the food is amazing, they come back for a second date. Banks price the IPO slightly lower than fair value to ensure the stock "pops" on day one—making the new shareholders feel like they got a deal.

### The Book Building Process

1. The bank "polls the audience" (institutional investors).
2. Investors submit their bids (price + quantity).
3. The bank sets the final price based on demand.

### The Formula

```
IPO Price = Fair Value × (1 - IPO Discount)

Example:
- Fair Value = $50 per share
- IPO Discount = 15%
- IPO Price = $50 × 0.85 = $42.50
```

**Python Tool**: [Run IPO_Pricing.py](./Python/IPO_Pricing.py)

> **🏃 Executive Summary:** IPO Pricing is about **managing expectations**. You intentionally leave money on the table (the "Pop") to ensure a successful launch and happy first-day investors.

---

## M&A Pricing - The "Synergy Premium"

When one company buys another, they don't just pay "fair value." They pay a **Premium**.

### The Formula

```
Purchase Price = Target Equity Value + Control Premium + Synergies
```

### Why Pay More?

> **💡 Schweser Note (The "2 + 2 = 5" Rule):** A buyer might pay $1.2B for a company worth $1.0B because they believe they can:
> - **Cut Costs:** Fire one of two accounting departments (**Cost Synergies**).
> - **Cross-Sell:** Use the target's customers to sell their own products (**Revenue Synergies**).
> 
> This extra value is called the **Synergy Premium**.

### Example

| Item | Value |
|------|-------|
| Standalone Value | $1,000M |
| Control Premium (20%) | $200M |
| Synergies (Expected) | $150M |
| **Total Purchase Price** | **$1,350M** |

---

## Peer Multiples - The "Real Estate Comps"

The most common way to price a company is to look at what similar companies are trading for.

### The "Real Estate" Analogy

You don't value a house in a vacuum. You look at the 4 houses sold on the same street last month.

> **💡 Schweser Note (Ignore the Outlier):** If one neighbor sold their house for 2x the market rate (maybe they were in a hurry), you don't use that as a comp. You use the **Median** to avoid the "Crazy Neighbor" bias.

### The Logic

1. **Select Peers:** Find 5-10 companies in the same industry.
2. **Collect Multiples:** P/E, EV/EBITDA, P/B.
3. **Take the Median:** Ignore the highs and lows.
4. **Apply to Target:** Multiply your target's metrics by the median.

**Python Tool**: [Run IPO_Pricing.py](./Python/IPO_Pricing.py)

---

## Corporate FP&A - The Internal GPS

**Financial Planning & Analysis (FP&A)** is how companies set their own "internal prices"—the budgets and forecasts that guide operations.

### The "GPS" Analogy

- **Valuation** is the destination (Where do we want to go?).
- **Pricing** is the ticket price (What do we charge?).
- **FP&A** is the GPS (How do we get there?).

### Key Concepts

- **Budget vs. Actuals:** Did we hit our revenue targets?
- **Variance Analysis:** Why did we miss (or exceed) expectations?
- **Forecasting:** Updating the budget for the next quarter.

---

## Final Recap

🏃 **Executive Summary:**

1. **Valuation** is the math; **Pricing** is the deal.
2. **IPOs** are priced at a discount to create a "First Day Pop."
3. **M&A** includes a Control Premium + Synergies.
4. **Peer Multiples** use the Median to avoid outlier bias.
5. **FP&A** is the internal compass for the company.

**Python Tool**: [Run IPO_Pricing.py](./Python/IPO_Pricing.py)

---

## Outlook & The Real World

### What We Didn't Cover

- **Dutch Auctions:** Used by Google in 2004—let the market set the price instead of the bank.
- **Direct Listings:** Used by Spotify and Slack—bypass the underwriter entirely.
- **Greenshoe Option:** The bank's safety net to stabilize the stock price after the IPO.

### Recommended Next Steps

- **Read:** *Investment Banking* by Joshua Rosenbaum and Joshua Pearl—the "Bible" of M&A pricing.
- **Practice:** Build your own Comparables table in Excel using real data from Yahoo Finance.

---

*Last updated: 2026 | Built for learning and interview prep*
