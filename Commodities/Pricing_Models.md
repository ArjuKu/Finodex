# Commodities - Pricing Models

**Objective:** Understanding how commodity prices are determined and traded.

---

## Table of Contents
1. [Spot vs. Futures](#spot-vs-futures)
2. [Method 1: Forward Pricing](#method-1-forward-pricing)
3. [Method 2: Cost of Carry](#method-2-cost-of-carry)
4. [Summary](#summary)

---

## 1. Spot vs. Futures
- **Spot Price**: The price *right now*. "I'll sell you this barrel of oil today for $75."
- **Futures Price**: The price to *promise* to buy/sell at a future date. "I'll sell you this barrel of oil in 6 months for $78."

---

## 2. Method 1: Forward Pricing
The price of a commodity for future delivery is based on today's spot price plus the cost to hold it.

```
Forward Price = Spot Price + Cost of Carry
```

Where Cost of Carry = Storage + Insurance + Financing

**Python Tool**: [Run Forward_Pricing.py](./Python/Forward_Pricing.py)

---

## 3. Method 2: Contango & Backwardation
- **Contango**: Futures prices are *higher* than spot. The market expects prices to rise.
- **Backwardation**: Futures prices are *lower* than spot. The market expects prices to fall.

---

## 4. Summary
Commodity pricing is driven by:
1. Today's spot price.
2. The cost to store and finance the commodity over time.
3. Market expectations for future price movements.
