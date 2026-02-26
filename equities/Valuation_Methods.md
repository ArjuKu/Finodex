# Equities - Valuation Methods

**Objective:** Finding the "Intrinsic Value" of a stock to decide if it's a Buy, Hold, or Sell.

---

## Table of Contents
1. [The "Lemonade Stand" Metaphor](#the-lemonade-stand-metaphor)
2. [The Equity Research Dictionary](#the-equity-research-dictionary)
3. [Method 1: P/E Ratio](#method-1-pe-ratio)
4. [Method 2: Equity DCF](#method-2-equity-dcf)
5. [Summary](#summary)

---

## 1. The "Lemonade Stand" Metaphor
Imagine you want to buy a lemonade stand.
- If the stand makes **$100 profit per year**, and you pay **$1,000** for it, it will take you **10 years** to earn back your money.
- In the stock market, this is called the **P/E Ratio** (Price-to-Earnings).

**The Goal:** Find stocks that are **worth more than the price** the market is asking.

---

## 2. The Equity Research Dictionary
- **Intrinsic Value**: What the stock is *actually* worth (based on fundamentals).
- **Market Price**: The current price on the stock exchange.
- **Margin of Safety**: Buying a stock for less than its intrinsic value.
- **EPS (Earnings Per Share)**: The company's profit divided by every single share.
- **FCFE (Free Cash Flow to Equity)**: The cash flow available to shareholders.

---

## 3. Method 1: P/E Ratio
"How many years of profit does it take to pay back my investment?"

```
P/E Ratio = Stock Price ÷ Earnings Per Share (EPS)
```

- **High P/E**: Investors expect high future growth (or the stock is overpriced!).
- **Low P/E**: The company is struggling (or it's a bargain!).

---

## 4. Method 2: Equity DCF (FCFE Model)
A dollar today is worth more than a dollar tomorrow. We forecast the cash for shareholders (FCFE) and bring it back to today's value.

```
Intrinsic Value = Σ [FCFE_t ÷ (1 + r)^t]
```
*(r = Cost of Equity)*

**Python Tool**: [Run Equity_DCF.py](./Python/Equity_DCF.py)

---

## 5. Summary
Equity Research is about finding a **Margin of Safety**.
1. Use the P/E ratio to see how expensive the stock is.
2. Use DCF to find the "True Value" (Intrinsic Value).
3. Only buy if the Intrinsic Value is **significantly higher** than the Market Price.
