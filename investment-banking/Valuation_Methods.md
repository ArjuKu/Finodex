# Investment Banking - Valuation Methods

**Objective:** Valuing a company for a "Transaction" (M&A, IPO, or Buyout).

---

## Table of Contents
1. [The "House Flip" Metaphor](#the-house-flip-metaphor)
2. [The IB Dictionary](#the-ib-dictionary)
3. [Method 1: Precedent Transactions](#method-1-precedent-transactions)
4. [Method 2: Corporate DCF](#method-2-corporate-dcf)
5. [Summary](#summary)

---

## 1. The "House Flip" Metaphor
Imagine you want to buy a local pizza shop.
- You want the **keys to the building**, the ovens, and the brand.
- You look at what other pizza shops in the city sold for recently.
- You might take out a loan (debt) to buy it, planning to pay back the loan using the pizza shop's daily profits.

In Investment Banking, we aren't just looking for "value"; we are looking for the **Transaction Price**.

---

## 2. The IB Dictionary
- **Enterprise Value (EV)**: The "Total Price Tag." It's the cost to buy the equity PLUS pay off all the company's debts.
- **Equity Value**: The market value of all the shares.
- **EBITDA**: "Profit before the bankers and accountants touch it."
- **Control Premium**: An extra fee (usually 20-30%) paid to convince current owners to give up control.
- **Synergies**: Cost savings from combining companies.

---

## 3. Method 1: Precedent Transactions
"What did the neighbors' businesses sell for?" We look at past M&A deals in the same industry.

```
Estimated Transaction Value = Target EBITDA × median Transaction Multiple
```

---

## 4. Method 2: Corporate DCF (Unlevered FCF)
How much cash can this business produce for *everyone* (both debt and equity holders)?

```
Unlevered Free Cash Flow (UFCF) = EBIT × (1 - Tax Rate) + D&A - CapEx - ΔNWC
```

**Python Tool**: [Run Corporate_DCF.py](./Python/Corporate_DCF.py)

---

## 5. Summary
Investment Banking valuation is about finding the **clearing price** for a deal. 
1. Look at what others paid (**Precedents**).
2. Look at the total cash available (**UFCF**).

**High Retention Recap:** If you want to buy the whole shop, look at the neighbor's price and make sure the shop makes enough cash to justify the total "Transaction Price Tag."
