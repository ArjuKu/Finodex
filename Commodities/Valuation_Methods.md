# Commodities - Valuation Methods

**Objective:** Valuing the physical commodity itself—not the company that owns it.

---

## Table of Contents
1. [The "Gold in the Ground" Metaphor](#the-gold-in-the-ground-metaphor)
2. [The Commodity Dictionary](#the-commodity-dictionary)
3. [Method 1: Spot Value](#method-1-spot-value)
4. [Method 2: Resource NAV](#method-2-resource-nav)
5. [Method 3: Reserve Classification](#method-3-reserve-classification)
6. [Nuance: Cost of Carry](#nuance-cost-of-carry)
7. [Nuance: Grade & Quality](#nuance-grade--quality)
8. [Book Recommendations](#book-recommendations)
9. [Summary](#summary)

---

## 1. The "Gold in the Ground" Metaphor
Imagine you find a gold nugget in a creek.
- **Spot Price**: The value of the nugget if you pull it out right now and sell it at the jewelry store.
- **Futures Price**: The promise to sell that nugget to someone in 6 months. The price is different because:
  - You have to store it (storage cost).
  - You could have invested that money elsewhere (interest cost).
  - The gold might lose purity if it sits too long (risk).

In commodities, we don't just value the company; we value the **actual pile of metal/oil/grain** in the ground or in storage.

---

## 2. The Commodity Dictionary
- **Spot Price**: The price of the commodity *right now* (today).
- **Futures Price**: The price to buy/sell the commodity at a *future date*.
- **In-Situ Value**: The value of the resource while it's still in the ground (before extraction).
- **Grade**: How "pure" the resource is. (Gold ore with 10 grams/tonne is worth more than 1 gram/tonne).
- **Reserve**: The amount of commodity that can be extracted profitably.
- **AISC (All-In Sustaining Cost)**: Total cost to extract and process one unit of commodity.
- **Cost of Carry**: The total cost to hold the commodity over time (Storage + Insurance + Interest).

---

## 3. Method 1: Spot Value

### The Concept
"What is this pile of gold worth if I sell it today?"

### Formula
```
Spot Value = Quantity × Current Spot Price
```

### Example
You have 100 ounces of gold. Gold is trading at $2,000/oz.
```
Spot Value = 100 × $2,000 = $200,000
```

### For Oil
You have 10,000 barrels of crude oil. Oil is trading at $75/barrel.
```
Spot Value = 10,000 × $75 = $750,000
```

---

## 4. Method 2: Resource NAV (Net Asset Value)

### The Concept
"What is this gold mine worth if I extract everything?"

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
**Input Assumptions:**
| Item | Value |
|------|-------|
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
| Value per Reserve | $356.30 |

**Python Tool**: [Run Resource_NAV.py](./Python/Resource_NAV.py)

---

## 5. Method 3: Reserve Classification

### Oil & Gas Classifications
| Category | Definition | Probability |
|----------|------------|--------------|
| 1P (Proven) | Commercial certainty to extract | 90% |
| 2P (Proven + Probable) | Economic certainty | 50% |
| 3P (Proven + Probable + Possible) | Low confidence | 10% |

### Mining Classifications
| Category | Description | Confidence |
|----------|-------------|------------|
| Measured | Highest confidence | 90% |
| Indicated | Good confidence | 50-90% |
| Inferred | Low confidence | 10-50% |

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

## 6. Nuance: Cost of Carry

*(Note: This is slightly more complex, but critically important in real commodity markets!)*

When you agree to sell oil 6 months from now, the price isn't just today's spot price. It's adjusted for:

### Components of Cost of Carry
1. **Storage Cost**: Oil takes up space in a tank.
2. **Insurance**: The oil could leak, burn, or be stolen.
3. **Financing Cost**: The seller had to buy the oil with money (that could have earned interest elsewhere).

### Formula
```
Futures Price = Spot Price + Cost of Carry

Where:
Cost of Carry = Storage + Insurance + Financing
```

### Example - Oil Forward Pricing
| Item | Value |
|------|-------|
| Current Spot Price | $75.00/barrel |
| Storage Cost (annual) | $2.00/barrel |
| Insurance (annual) | $0.50/barrel |
| Financing Rate | 5% |
| Financing Cost | $75 × 5% = $3.75/barrel |
| Total Annual Carry | $6.25/barrel |
| **6-Month Forward Price** | **$75 + $3.125 = $78.125** |

### Contango vs. Backwardation
- **Contango**: Futures prices are *higher* than spot. The market expects prices to rise.
- **Backwardation**: Futures prices are *lower* than spot. The market expects prices to fall.

**Python Tool**: [Run Forward_Pricing.py](./Python/Forward_Pricing.py)

---

## 7. Nuance: Grade & Quality
Not all commodities are created equal.

### The Gold Example
| Grade | Description | Value Impact |
|-------|------------|--------------|
| High Grade (10 g/t) | Rich ore, profitable to mine | High value |
| Low Grade (1 g/t) | Poor ore, may cost more to extract than worth | Low/No value |

### The Oil Example
| Type | Description | Price Impact |
|------|------------|--------------|
| Brent Crude | High quality, easy to refine | Premium price |
| Heavy Crude | Low quality, expensive to process | Discounted price |

**Key Insight:** A mine with 100 tonnes of low-grade ore might be worth *less* than a mine with 10 tonnes of high-grade ore.

---

## 8. Book Recommendations
To understand commodities, hedging, and pricing in greater depth:

1. **"Hot Commodities" by Jim Rogers** - A beginner-friendly classic on commodity markets.
2. **"Commodities Demystified" by Trafigura** - Straight from one of the world's biggest trading houses.
3. **"The Economics of the Commodities Market"** - For understanding how commodity prices interact with global markets.

---

## 9. Summary
Commodity valuation is about the **physical good**, not the company.
1. **Spot Value**: What's it worth today?
2. **Resource NAV**: What's the whole deposit worth if we extract it?
3. **Cost of Carry**: Why does the future price differ from today's price?
4. **Grade**: More isn't always better—quality matters!

**High Retention Recap:** Think of commodities like a warehouse. The Spot Price is what's on the shelf today. The Futures Price is what you'll pay to have it delivered next year (plus storage and interest). And just like gold, not all "ore" is worth mining—grade matters!

**Python Tool**: [Run Resource_NAV.py](./Python/Resource_NAV.py)
