# Commodities - Valuation Methods

**Objective:** Valuing the physical commodity itself—not the company that owns it.

---

## Table of Contents
1. [The "Gold in the Ground" Metaphor](#the-gold-in-the-ground-metaphor)
2. [The Commodity Dictionary](#the-commodity-dictionary)
3. [Method 1: Spot Value](#method-1-spot-value)
4. [Method 2: Resource NAV](#method-2-resource-nav)
5. [Nuance: Cost of Carry](#nuance-cost-of-carry)
6. [Nuance: Grade & Quality](#nuance-grade--quality)
7. [Book Recommendations](#book-recommendations)
8. [Summary](#summary)

---

## 1. The "Gold in the Ground" Metaphor
Imagine you find a gold nugget in a creek.
- **Spot Price**: The value if you pull it out right now and sell it.
- **Futures Price**: The promise to sell it in 6 months. The price is different because of storage cost, interest, and risk.

In commodities, we value the **actual pile of metal/oil/grain** in the ground or in storage.

---

## 2. The Commodity Dictionary
- **Spot Price**: The price *right now* (today).
- **Futures Price**: The price to buy/sell at a *future date*.
- **In-Situ Value**: The value while it's still in the ground (before extraction).
- **Grade**: How "pure" the resource is.
- **Reserve**: The amount that can be extracted profitably.
- **Cost of Carry**: Storage + Insurance + Interest.

---

## 3. Method 1: Spot Value
"What is this pile of gold worth if I sell it today?"

```
Spot Value = Quantity × Current Spot Price
```

---

## 4. Method 2: Resource NAV
"What is this gold mine worth if we extract everything?"

```
Resource NAV = Σ [Annual Production × (Spot Price - Extraction Cost)] ÷ (1 + Discount Rate)
```

**Python Tool**: [Run Resource_NAV.py](./Python/Resource_NAV.py)

---

## 5. Nuance: Cost of Carry
When you agree to sell oil in 6 months, the price includes:
1. **Storage Cost**: Oil takes up space in a tank.
2. **Insurance**: Could leak, burn, or be stolen.
3. **Financing Cost**: Money could have earned interest elsewhere.

```
Futures Price = Spot Price + Cost of Carry
```

---

## 6. Nuance: Grade & Quality
Not all commodities are created equal.
- **Gold Ore at 10 grams/tonne**: High grade. Profitable to mine.
- **Gold Ore at 1 gram/tonne**: Low grade. Might cost more to extract than it's worth!

---

## 7. Book Recommendations
1. **"Hot Commodities" by Jim Rogers** - Beginner-friendly classic.
2. **"Commodities Demystified" by Trafigura** - From a major trading house.
3. **"The Economics of the Markets"** - For understanding price interactions.

---

## 8. Summary
Commodity valuation is about the **physical good**, not the company.
1. **Spot Value**: What's it worth today?
2. **Resource NAV**: What's the whole deposit worth if we extract it?
3. **Cost of Carry**: Why does the future price differ from today's price?
4. **Grade**: More isn't always better—quality matters!
