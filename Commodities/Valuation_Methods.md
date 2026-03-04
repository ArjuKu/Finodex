# Commodities - Valuation Methods

**Objective:** Valuing the physical commodity—not the company that owns it—from a trader/operations perspective.

---

## Table of Contents

1. [The "Gold in the Ground" Metaphor](#the-gold-in-the-ground-metaphor)
2. [The Commodity Dictionary](#the-commodity-dictionary)
3. [Method 1 - Spot Value](#method-1---spot-value)
4. [Method 2 - Resource NAV](#method-2---resource-nav)
5. [Method 3 - In-Situ Value](#method-3---in-situ-value)
6. [Grade & Quality Adjustments](#grade--quality-adjustments)
7. [Reserve Classification](#reserve-classification)
8. [Final Recap](#final-recap)

---

## The "Gold in the Ground" Metaphor

Imagine you find a gold nugget in a creek.

- **Spot Price**: The value of the nugget if you pull it out right now and sell it at the jewelry store.
- **Futures Price**: The promise to sell that nugget to someone in 6 months. The price is different because:
  - You have to store it (storage cost).
  - You could have invested that money elsewhere (interest cost).
  - The gold might lose purity if it sits too long (risk).

In commodities trading, we don't just value the company; we value the **actual pile of metal/oil/grain** in the ground or in storage.

> **💡 Trader's Note:** Unlike a stock (which can go up forever), a commodity has a "ceiling"—you can't have negative oil. When warehouses are full, the price can actually go negative (as we saw in April 2020).

---

## The Commodity Dictionary

Before we look at the math, let's define the terms:

- **Spot Price**: The price of the commodity *right now* (today).
- **Futures Price**: The price to buy/sell the commodity at a *future date*.
- **In-Situ Value**: The value of the resource while it's still in the ground (before extraction).
- **Grade**: How "pure" the resource is. (Gold ore with 10 grams/tonne is worth more than 1 gram/tonne).
- **Reserve**: The amount of commodity that can be extracted profitably.
- **AISC (All-In Sustaining Cost)**: Total cost to extract and process one unit of commodity.
- **Cost of Carry**: The total cost to hold the commodity over time (Storage + Insurance + Interest).
- **Contango**: Futures prices are higher than spot. (Market expects prices to rise).
- **Backwardation**: Futures prices are lower than spot. (Market expects prices to fall).

---

## Method 1 - Spot Value

### The Concept

"What is this pile of gold worth if I sell it today?"

### Formula

```
Spot Value = Quantity × Current Spot Price
```

### Example - Gold
You have 100 ounces of gold. Gold is trading at $2,000/oz.
```
Spot Value = 100 × $2,000 = $200,000
```

### Example - Oil
You have 10,000 barrels of crude oil. Oil is trading at $75/barrel.
```
Spot Value = 10,000 × $75 = $750,000
```

---

## Method 2 - Resource NAV

### The Concept

"What is this gold mine worth if we extract everything?"

### Formula

```
Resource NAV = Σ [Annual Production × (Spot Price - AISC)] ÷ (1 + Discount Rate)^t
```

### Simplified Steps
1. **How much gold is in the ground?** (Reserves)
2. **How much does it cost to extract?** (AISC - All-In Sustaining Cost)
3. **What's the gold price?** (Use long-term forecast, not today's spot)
4. **Bring the cash back to today** (Discount rate).

### Example - Gold Mine NAV

| Input | Value |
|-------|-------|
| Total Reserves | 1,000,000 ounces |
| Annual Production | 100,000 ounces/year |
| Mine Life | 10 years |
| Long-term Gold Price | $1,800/oz |
| AISC (Cost to extract) | $1,200/oz |
| Profit per ounce | $600 |
| Discount Rate | 10% |

**Step-by-Step Cash Flow:**

| Year | Production (oz) | Revenue | AISC Cost | Cash Flow | PV (10%) |
|------|-----------------|---------|------------|------------|-----------|
| 1 | 100,000 | $180M | $120M | $60M | $54.5M |
| 2 | 100,000 | $180M | $120M | $60M | $49.6M |
| 3 | 100,000 | $180M | $120M | $60M | $45.1M |
| 4 | 100,000 | $180M | $120M | $60M | $41.0M |
| 5 | 100,000 | $180M | $120M | $60M | $37.3M |
| 6-10 | 500,000 | $900M | $600M | $300M | $128.8M |
| **Total PV** | | | | | **$356.3M** |

**Summary:**

| Item | Value |
|------|-------|
| NAV (Present Value) | $356.3M |
| Value per Ounce | $356/oz |

> **💡 Trader's Note:** If the spot price of gold is $2,000 but your NAV is only $1,500/oz, the mine might not be profitable to operate. As a trader, you care about the **spread** between spot and AISC.

**Python Tool**: [Run Resource_NAV.py](./Python/Resource_NAV.py)

---

## Method 3 - In-Situ Value

### The Concept

What is the resource worth *while it's still in the ground*? This is critical for M&A of mining or oil companies.

### Formula

```
In-Situ Value = Total Resources × Grade × Recovery Rate × Net Smelter Return (NSR)
```

### 📊 In-Situ Worked Example

| Input | Value |
|-------|-------|
| Total Resources | 10,000,000 tonnes |
| Grade | 1.5 grams/tonne (Au) |
| Recovery Rate | 90% (how much gold you actually extract) |
| Gold Price | $2,000/oz |
| Conversion | 1 tonne = 32,150.7 troy ounces |

**Calculation:**
```
Total Gold = 10,000,000 × 1.5 g/t = 15,000 kg = 482,260 oz
Recovered Gold = 482,260 × 90% = 434,034 oz
In-Situ Value = 434,034 × $2,000 = $868M
```

> **💡 Analyst Note:** In-Situ Value is always higher than the "cost to extract" because you're valuing the *option* to mine, not the obligation. If gold prices spike, the option becomes more valuable.

---

## Grade & Quality Adjustments

Not all commodities are created equal. Quality directly impacts price.

### The Gold Example

| Grade | Description | Value Impact |
|-------|------------|--------------|
| High Grade (10 g/t) | Rich ore, profitable to mine | High value |
| Low Grade (1 g/t) | Poor ore, may cost more to extract than worth | Low/No value |

### The Oil Example

| Type | Description | Price Impact |
|------|------------|--------------|
| Brent Crude | High quality, easy to refine | Premium price |
| WTI (West Texas Intermediate) | US benchmark, good quality | Base price |
| Heavy Crude | Low quality, expensive to process | Discounted price |
| Sour Crude (High Sulphur) | High impurities | Large discount |

### 💡 Quality Spread Table

| Quality Metric | Premium / Discount | Example |
|---------------|-------------------|---------|
| Sweet Crude (< 0.5% Sulphur) | +$2 - $5/bbl | Brent premium over WTI |
| Sour Crude (> 2.5% Sulphur) | -$5 - $15/bbl | Heavy discounts |
| High Grade Coffee (Specialty) | +20 - 50% | Ethiopian vs. Robusta |
| Low Grade Copper (< 1% purity) | -10 - 15% | Grade penalties |

> **Key Insight:** A mine with 100 tonnes of low-grade ore might be worth *less* than a mine with 10 tonnes of high-grade ore. **Grade is king.**

---

## Reserve Classification

### Oil & Gas Classifications

| Category | Definition | Probability |
|----------|------------|--------------|
| **1P (Proven)** | Commercial certainty to extract | 90% |
| **2P (Proven + Probable)** | Economic certainty | 50% |
| **3P (Proven + Probable + Possible)** | Low confidence | 10% |

### Mining Classifications

| Category | Description | Confidence |
|----------|-------------|------------|
| **Measured** | Highest confidence | 90% |
| **Indicated** | Good confidence | 50-90% |
| **Inferred** | Low confidence | 10-50% |

### Reserve Life Formula

```
Reserve Life = Reserves ÷ Annual Production
```

### Example

| Item | Value |
|------|-------|
| 2P Reserves | 100 MMboe |
| Annual Production | 10 MMboe |
| Reserve Life | 10 years |

---

## Final Recap

🏃 **Executive Summary:**

1. **Spot Value**: What's it worth today if I sell immediately?
2. **Resource NAV**: What's the whole deposit worth if we extract it profitably?
3. **In-Situ Value**: What's it worth while it's still in the ground (the "option value")?
4. **Grade**: Quality matters—high-grade commands a premium, low-grade commands a discount.

> **💡 Trader's Mantra:** In commodities, **location, quality, and timing are everything**. A barrel of oil in the wrong place at the wrong time is worth nothing.

**Python Tool**: [Run Resource_NAV.py](./Python/Resource_NAV.py)

---

## Outlook & The Real World

### What We Didn't Cover

- **Futures & Forwards**: The "paper" contracts traded on CME/LME.
- **Options on Commodities**: The right (but not obligation) to buy/sell at a strike price.
- **Collateral Management**: How traders post margin and manage counterparty risk.

### Recommended Next Steps

- **Read:** *Hot Commodities* by Jim Rogers – A classic on commodity markets.
- **Practice:** Watch live commodity prices on Bloomberg or TradingView.
- **Course:** CFI's *Commodity Trading* course for intermediate depth.

---

*Last updated: 2026 | Built for learning and interview prep*
