# Commodities - Pricing Models

**Objective:** Understanding how commodity prices are determined, traded, and managed from a trader/broker perspective.

---

## Table of Contents

1. [The "Warehouse Trap"](#the-warehouse-trap)
2. [Spot vs. Futures](#spot-vs-futures)
3. [Method 1 - Forward Pricing (Cost of Carry)](#method-1---forward-pricing-cost-of-carry)
4. [Method 2 - Contango vs. Backwardation](#method-2---contango-vs-backwardation)
5. [Method 3 - Basis & Spread Trading](#method-3---basis--spread-trading)
6. [Convenience Yield](#convenience-yield)
7. [Final Recap](#final-recap)

---

## The "Warehouse Trap"

Unlike a stock (which lives in a computer), a barrel of oil takes up physical space. It must be stored in a tank, guarded against theft, and insured against leakage.

> **💡 Trader's Note:** If you buy 1 million barrels of oil, you can't just "hold it" in your brokerage account. You need a physical warehouse or pipeline. This creates the **Cost of Carry**—the heartbeat of commodity pricing.

---

## Spot vs. Futures

| Concept | Definition | Example |
|---------|------------|---------|
| **Spot Price** | The price *right now* for immediate delivery. | "I'll sell you this barrel of oil today for $75." |
| **Futures Price** | The price to *promise* to buy/sell at a future date. | "I'll sell you this barrel of oil in 6 months for $78." |

> **Key Difference:** Spot is a **physical** transaction (hand over the barrel now). Futures is a **paper** contract (promise to hand over the barrel later).

---

## Method 1 - Forward Pricing (Cost of Carry)

### The Concept

The price of a commodity for future delivery is based on today's spot price **plus** the cost to hold it.

### Formula

```
Forward Price = Spot Price + Cost of Carry

Where:
Cost of Carry = Storage Cost + Insurance Cost + Financing Cost
```

### 📊 Worked Example: Oil Forward Pricing

| Input | Value |
|-------|-------|
| Current Spot Price | $75.00/barrel |
| Storage Cost (annual) | $2.00/barrel |
| Insurance (annual) | $0.50/barrel |
| Financing Rate | 5% |
| Financing Cost | $75 × 5% = $3.75/barrel |
| **Total Annual Carry** | **$6.25/barrel** |

**6-Month Forward Price Calculation:**
```
Forward Price = Spot + (Carry × Time)
Forward Price = $75.00 + ($6.25 × 0.5 years)
Forward Price = $75.00 + $3.125
Forward Price = $78.125
```

> **💡 Math Insight:** If you can buy oil at $75, store it for 6 months for $3.125, and sell a futures contract at $78.125, you make a **risk-free arbitrage profit** (ignoring transaction costs). This is called **"Cash and Carry."**

---

## Method 2 - Contango vs. Backwardation

The relationship between spot and futures prices creates the "curve."

### Contango (The "Normal" Market)

| Condition | Description |
|-----------|-------------|
| **Definition** | Futures prices are *higher* than spot. The curve slopes **upward**. |
| **Why?** | High storage costs, high interest rates, or market expects higher future prices. |
| **Trader Action** | "Cash and Carry" – Buy physical, store, sell futures. |

**Visual:**
```
Spot:    $75
3-Month: $78
6-Month: $81
12-Month: $85
```

### Backwardation (The "Inverted" Market)

| Condition | Description |
|-----------|-------------|
| **Definition** | Futures prices are *lower* than spot. The curve slopes **downward**. |
| **Why?** | Short-term scarcity (war, shortage) or high immediate demand. |
| **Trader Action** | "Reverse Cash and Carry" – Borrow physical, sell now, buy futures to return. |

**Visual:**
```
Spot:    $85
3-Month: $82
6-Month: $79
12-Month: $76
```

### 💡 Real-World Case: April 2020 Negative Oil

In April 2020, WTI crude oil went to **-$37/barrel**. Why?

1. **COVID-19 crashed demand** – No one was driving.
2. **Storage was full** – The "warehouse" (Cushing, OK) had no room.
3. **Futures expiry** – Traders holding physical oil had to pay someone to take it.

> **Trader's Lesson:** In commodities, if you can't store the physical, the price can crash to zero—or negative.

---

## Method 3 - Basis & Spread Trading

### The Concept

The **Basis** is the difference between the physical price and the futures price at a specific location.

### Formula

```
Basis = Local Cash Price - Futures Price
```

### 📊 Worked Example: Houston vs. Cushing

| Location | Price | Futures (NYMEX) | Basis |
|----------|-------|-----------------|-------|
| Cushing (Oklahoma) | $75.00 | $75.50 | -$0.50 |
| Houston (Gulf Coast) | $78.00 | $75.50 | **+$2.50** |

> **💡 Trader's Note:** The Houston price is higher because it's **closer to the export terminal**. As a trader, you profit from the **location spread**—buy at Cushing, sell at Houston.

### Types of Spreads

| Spread Type | What It Measures | Example |
|-------------|------------------|---------|
| **Calendar Spread** | Time difference (July vs. Dec) | Buy July / Sell Dec |
| **Location Spread** | Geographic difference | Buy Cushing / Sell Houston |
| **Quality Spread** | Grade difference | Buy Brent / Sell WTI |

---

## Convenience Yield

### The Concept

The **Convenience Yield** is the hidden benefit of physically holding the commodity. It's the "power" you get from having the physical in your possession.

### Formula

```
Convenience Yield = Risk-Free Rate + Storage Cost - Forward Price + Spot Price
```

### Why It Matters

If a refinery has immediate access to physical oil (high convenience yield), they are willing to pay more for spot—even if futures are cheaper.

> **💡 Trader's Note:** During a crisis (e.g., a hurricane hitting the Gulf), the convenience yield spikes. Refineries **need** the physical now, so they bid up the spot price regardless of the futures price.

---

## Final Recap

🏃 **Executive Summary:**

1. **Cost of Carry**: The price to store and finance the physical.
2. **Contango**: Futures > Spot. (Normal market, upward curve).
3. **Backwardation**: Futures < Spot. (Scarcity, inverted curve).
4. **Basis**: The local price vs. the futures price.
5. **Spreads**: Betting on the difference between time, location, or quality.

> **💡 The Golden Rule:** In commodities, **you trade the spread, not the absolute price.** A trader doesn't care if oil is $75 or $85—they care if the July/December spread will widen or narrow.

**Python Tool**: [Run Forward_Pricing.py](./Python/Forward_Pricing.py)

---

## Outlook & The Real World

### What We Didn't Cover

- **Options on Futures**: The right (but not obligation) to buy/sell at a strike.
- **Swaps**: Customized contracts to lock in prices.
- **Margin & Collateral**: How traders post cash/gold to cover positions.

### The "Green Metals" Boom

- **Copper**: The new oil. Used in EVs, wiring, renewable energy.
- **Lithium**: Battery metal. Prices have spiked 10x in 5 years.
- **Nickel**: Stainless steel and batteries.

> **Future Watch:** As the world decarbonizes, the "Soft Commodities" (Lithium, Copper) will behave more like "Hard Commodities" (Oil, Gold).

### Recommended Next Steps

- **Watch:** CME Group's daily commodity reports.
- **Read:** * commodity Trading* by Michael D. Mover – Advanced strategies.
- **Practice:** Track the "Gold Basis" in your local market.

---

*Last updated: 2026 | Built for learning and interview prep*
