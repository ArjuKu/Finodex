# Investment Banking - Valuation Methods

**Objective:** Valuing a company for a "Transaction" (M&A, IPO, or Buyout).

---

## Table of Contents
1. [The "House Flip" Metaphor](#the-house-flip-metaphor)
2. [The IB Dictionary](#the-ib-dictionary)
3. [Method 1: Precedent Transactions](#method-1-precedent-transactions)
4. [Method 2: Corporate DCF (Unlevered FCF)](#method-2-corporate-dcf)
5. [Method 3: Accretion/Dilution Analysis](#method-3-accretiondilution-analysis)
6. [Summary](#summary)

---

## 1. The "House Flip" Metaphor
Imagine you want to buy a local pizza shop.
- You don't just want to buy one pizza (a share); you want the **keys to the building**, the ovens, and the brand.
- To do this, you look at what other pizza shops in the city sold for recently.
- You might take out a loan (debt) to buy it, planning to pay back the loan using the pizza shop's daily profits.

In Investment Banking, we aren't just looking for "value"; we are looking for the **Transaction Price**.

---

## 2. The IB Dictionary
Before we look at the math, let's define the terms:
- **Enterprise Value (EV)**: The "Total Price Tag." It's the cost to buy the equity PLUS pay off all the company's debts.
  ```
  EV = Market Cap + Total Debt - Cash
  ```
- **Equity Value**: The market value of all the shares. If you own the equity, you own the "upside."
- **EBITDA**: "Profit before the bankers and accountants touch it." It stands for Earnings Before Interest, Taxes, Depreciation, and Amortization. It shows the raw earning power of the business.
- **Control Premium**: An extra fee (usually 20-30%) paid to convince current owners to give up control.
- **Synergies**: Cost savings. "If I buy your shop, I can fire one of our two accountants because we only need one now."
- **Unlevered FCF**: Cash flow available to ALL investors (debt + equity) before debt payments.

---

## 3. Method 1: Precedent Transactions

### The Concept
"What did the neighbors' businesses sell for?" We look at past M&A deals in the same industry.

### Formula
```
Estimated Transaction Value = Target EBITDA × median Transaction Multiple
```

### The Nuance
You must add the **Control Premium**. If similar companies trade on the stock market at 10x EBITDA, a buyer might pay 13x EBITDA to take over the whole company.

### Example - Precedent Transactions
| Acquirer | Target | Year | EV | EV/EBITDA | Premium |
|----------|--------|------|-----|-----------|---------|
| Buyer A | Company X | 2023 | $15B | 12x | 25% |
| Buyer B | Company Y | 2023 | $10B | 11x | 20% |
| Buyer C | Company Z | 2024 | $8B | 10x | 15% |
| **Median** | | | | **11x** | **20%** |

### Applying to Your Target
| Item | Value |
|------|-------|
| Target EBITDA | $500M |
| Median Multiple | 11x |
| Implied EV | $5,500M |
| Less: Net Debt | ($1,000M) |
| **Implied Equity Value** | **$4,500M** |
| Add: Control Premium (20%) | $900M |
| **Final Purchase Price** | **$5,400M** |

---

## 4. Method 2: Corporate DCF (Unlevered FCF)

### The Concept
How much cash can this business produce for *everyone* (both the people who lent money and the people who own shares)?

### The "IB First" Difference
Bankers use **Unlevered FCF** because it's independent of how the company is funded. It allows us to see how much cash the company makes *before* we decide how much debt to use to buy it.

### Formula
```
Unlevered Free Cash Flow (UFCF) = EBIT × (1 - Tax Rate) + D&A - CapEx - ΔNWC
```

### Step-by-Step DCF for M&A

#### Step 1: Project Revenue and EBIT
| Year | Revenue | Growth | EBIT Margin | EBIT |
|------|---------|--------|-------------|------|
| 1 | $1,000M | 10% | 20% | $200M |
| 2 | $1,100M | 10% | 20% | $220M |
| 3 | $1,210M | 10% | 20% | $242M |
| 4 | $1,331M | 10% | 20% | $266M |
| 5 | $1,464M | 10% | 20% | $293M |

#### Step 2: Calculate NOPAT
```
NOPAT = EBIT × (1 - Tax Rate)
Example: Year 1 NOPAT = $200M × (1 - 0.21) = $158M
```

#### Step 3: Calculate Unlevered FCF
| Year | NOPAT | +D&A | -CapEx | -ΔNWC | = UFCF |
|------|-------|------|--------|-------|--------|
| 1 | $158 | $50 | -$60 | -$20 | $128 |
| 2 | $174 | $55 | -$66 | -$22 | $141 |
| 3 | $191 | $61 | -$73 | -$24 | $155 |
| 4 | $210 | $67 | -$80 | -$27 | $170 |
| 5 | $231 | $73 | -$88 | -$29 | $187 |

#### Step 4: Discount to Present Value (WACC = 10%)
```
PV = UFCF ÷ (1 + WACC)^t
Example Year 1: $128 ÷ 1.10^1 = $116M
```

| Year | UFCF | Discount Factor | PV |
|------|------|-----------------|-----|
| 1 | $128 | 0.909 | $116 |
| 2 | $141 | 0.826 | $116 |
| 3 | $155 | 0.751 | $116 |
| 4 | $170 | 0.683 | $116 |
| 5 | $187 | 0.621 | $116 |
| **Sum (1-5)** | | | **$580** |

#### Step 5: Terminal Value
```
Terminal Value = UFCF_5 × (1 + g) ÷ (WACC - g)
g = 3% (perpetual growth)
TV = $187 × 1.03 ÷ (0.10 - 0.03) = $2,753M
PV of TV = $2,753 ÷ 1.10^5 = $1,709M
```

#### Step 6: Enterprise Value
```
Enterprise Value = PV of FCF + PV of TV
EV = $580M + $1,709M = $2,289M
```

**Python Tool**: [Run Corporate_DCF.py](./Python/Corporate_DCF.py)

---

## 5. Method 3: Accretion/Dilution Analysis

### The Concept
When one company buys another, the most important question for the buyer's shareholders is: **"Does this make my Earnings Per Share (EPS) go up or down?"**

### Formulas
```
Accretion % = (New EPS - Old EPS) ÷ Old EPS

New EPS = Combined Net Income ÷ Combined Shares
```

### Example - Accretion Analysis
| Item | Acquirer (Buyer) | Target | Combined |
|------|------------------|--------|----------|
| Net Income | $500M | $100M | $600M |
| Shares Outstanding | 100M | 50M | 120M |
| EPS | $5.00 | $2.00 | $5.00 |

**Calculation:**
- Buyer EPS before: $5.00
- Combined EPS: $600M ÷ 120M = $5.00
- **Accretion/(Dilution):** 0%

### If EPS Goes Up = Accretive (Good Deal!)
### If EPS Goes Down = Dilutive (Bad Deal!)

---

## 6. Summary
Investment Banking valuation is about finding the **clearing price** for a deal. 
1. We look at what others paid (**Precedents**).
2. We look at the total cash available (**UFCF**).
3. We check if the buyer's shareholders will be happy (**Accretion/Dilution**).

**High Retention Recap:** If you want to buy the whole shop, look at the neighbor's price, make sure the shop makes enough cash to justify the total "Transaction Price Tag," and ensure the deal makes your shareholders richer, not poorer.

**Python Tool**: [Run Corporate_DCF.py](./Python/Corporate_DCF.py)
