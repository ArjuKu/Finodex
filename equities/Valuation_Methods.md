# Equities - Valuation Methods

**Objective:** Finding the "Intrinsic Value" of a stock to decide if it's a Buy, Hold, or Sell.

---

## Table of Contents

1. [The "Lemonade Stand" Metaphor](#the-lemonade-stand-metaphor)
2. [The Equity Research Dictionary](#the-equity-research-dictionary)
3. [Method 1 - P/E Ratio (Relative Valuation)](#method-1---pe-ratio-relative-valuation)
4. [Method 2 - DCF (Discounted Cash Flow)](#method-2---dcf-discounted-cash-flow)
5. [Method 3 - Dividend Discount Model](#method-3---dividend-discount-model)
6. [Method 4 - Sum-of-the-Parts (SOTP)](#method-4---sum-of-the-parts-sotp)
7. [Sensitivity Analysis](#sensitivity-analysis)
8. [Final Recap](#final-recap)

---

## 1. The "Lemonade Stand" Metaphor

Imagine you want to buy a lemonade stand.

- If the stand makes **$100 profit per year**, and you pay **$1,000** for it, it will take you **10 years** to earn back your money.
- In the stock market, this is called the **P/E Ratio** (Price-to-Earnings).
- A researcher asks: "Is this stand worth $1,000, or is it really worth $800 because there's a new coffee shop opening nearby?"

**The Goal:** Find stocks that are **worth more than the price** the market is asking.

> **💡 Analyst Note:** In Equities, we call this the **"Margin of Safety"**—the difference between Intrinsic Value and Market Price. Benjamin Graham, the father of value investing, compared it to buying a $100 bill for $70.

---

## 2. The Equity Research Dictionary
Before we look at the math, let's define the terms:
- **Intrinsic Value**: What the stock is *actually* worth (based on fundamentals), not what it's trading for today.
- **Market Price**: The current price on the stock exchange (driven by emotions, news, and supply/demand).
- **Margin of Safety**: Buying a stock for less than its intrinsic value. It's like buying a $100 bill for $70.
- **EPS (Earnings Per Share)**: The company's profit divided by every single share.
- **EBITDA**: "Profit before the boring stuff." (Interest, Taxes, Depreciation, Amortization).
- **FCFF (Free Cash Flow to Firm)**: Cash available to ALL investors (debt + equity).
- **FCFE (Free Cash Flow to Equity)**: Cash available to shareholders AFTER debt payments.

---

## 3. Method 1: P/E Ratio (Relative Valuation)

### The Concept
"How many years of profit does it take to pay back my investment?"

### Formula
```
P/E Ratio = Stock Price ÷ Earnings Per Share (EPS)

Where:
- Stock Price = Current market price per share
- EPS = Net Income ÷ Shares Outstanding
```

### Example
| Company | Stock Price | Net Income | Shares | EPS | P/E |
|---------|-------------|------------|--------|-----|-----|
| Tech A | $50 | $100M | 50M | $2.00 | 25x |
| Utility B | $40 | $200M | 50M | $4.00 | 10x |

**Interpretation:**
- Tech A at 25x P/E means: "It takes 25 years of profits to pay back my investment"
- Utility B at 10x P/E means: "It takes 10 years of profits to pay back my investment"

### Types of P/E
| Type | Formula | Best For |
|------|---------|----------|
| Trailing P/E | Price ÷ Last 12 months EPS | Historical view |
| Forward P/E | Price ÷ Next 12 months EPS | Growth stocks |
| PEG Ratio | P/E ÷ Expected Growth Rate | Growth comparison |

### When to Use
- Companies with stable, predictable earnings
- Quick comparison within an industry
- When DCF inputs are uncertain

---

### 📊 Multiples Deep-Dive: Which One to Use?

| Multiple | Formula | Best For | Why It Works |
|---------|---------|----------|--------------|
| **P/E** | Price ÷ EPS | Mature, profitable companies | Earnings are the "final score" of a business. |
| **Forward P/E** | Price ÷ Next Year EPS | Growth stocks | Based on future earnings, not past. |
| **PEG** | P/E ÷ Growth Rate | Comparing growth stocks | Normalizes P/E for high growth. |
| **P/S** | Price ÷ Revenue | High-growth tech, retail | Revenue is harder to manipulate than earnings. |
| **P/B** | Price ÷ Book Value | Banks, financial institutions | Book value is tangible; earnings are volatile for banks. |
| **EV/EBITDA** | EV ÷ EBITDA | Manufacturing, industrials | Removes effects of capital structure and accounting. |

> **💡 Analyst Note (CFA Curriculum):** P/E is most reliable when applied to companies with stable capital structures and positive earnings. For high-growth tech companies, P/S or PEG ratios are more appropriate because earnings may be negative or volatile.

---

## 4. Method 2 - DCF (Discounted Cash Flow)

### The Concept

A dollar today is worth more than a dollar tomorrow. We forecast future cash flows and bring them back to today's value.

### FCFF vs. FCFE: Which One to Use?

| Metric | FCFF (Free Cash Flow to Firm) | FCFE (Free Cash Flow to Equity) |
|--------|-------------------------------|--------------------------------|
| **Definition** | Cash available to ALL investors (debt + equity) | Cash available to SHAREHOLDERS only |
| **Use Case** | Investment Banking (Valuing the whole company) | Equity Research (Valuing the stock) |
| **Starting Point** | EBIT × (1 - Tax Rate) | Net Income |
| **Formula** | NOPAT + D&A - CapEx - ΔNWC | Net Income + D&A - CapEx - ΔNWC + Net Borrowing |

> **💡 Analyst Note:** In Equity Research, we typically use **FCFE** because we're buying stock, not the entire company. However, the **FCFF** approach (used in IB) is also valid—it gives you Enterprise Value, which you then subtract Net Debt to get Equity Value.

### Formula (Simplified)
```
Intrinsic Value = Σ [CF_t ÷ (1 + r)^t] + Terminal Value

Where:
- CF_t = Cash flow in period t
- r = Discount rate (Cost of Equity for FCFE, WACC for FCFF)
- t = Time period
```

### Step-by-Step DCF Process

#### Step 1: Project Revenue and Expenses
| Year | Revenue | Growth | COGS | OpEx | EBIT |
|------|---------|--------|------|------|------|
| 1 | $10,000M | 10% | -$6,000 | -$2,000 | $2,000 |
| 2 | $11,000M | 10% | -$6,600 | -$2,200 | $2,200 |
| 3 | $12,100M | 10% | -$7,260 | -$2,420 | $2,420 |
| 4 | $13,310M | 10% | -$7,986 | -$2,662 | $2,662 |
| 5 | $14,641M | 10% | -$8,785 | -$2,928 | $2,928 |

#### Step 2: Calculate NOPAT (Net Operating Profit After Tax)
```
NOPAT = EBIT × (1 - Tax Rate)

Example: Year 1 NOPAT = $2,000M × (1 - 0.21) = $1,580M
```

#### Step 3: Calculate Free Cash Flow (FCFF)
```
FCFF = NOPAT + D&A - CapEx - Change in NWC
```

| Year | NOPAT | +D&A | -CapEx | -ΔNWC | = FCFF |
|------|-------|------|--------|-------|--------|
| 1 | $1,580 | $500 | -$600 | -$200 | $1,280 |
| 2 | $1,738 | $550 | -$660 | -$220 | $1,408 |
| 3 | $1,912 | $605 | -$726 | -$242 | $1,549 |
| 4 | $2,103 | $666 | -$799 | -$266 | $1,704 |
| 5 | $2,313 | $732 | -$878 | -$293 | $1,874 |

#### Step 4: Calculate Terminal Value
**Method A: Gordon Growth**
```
Terminal Value = FCFF_5 × (1 + g) ÷ (r - g)

Where:
- g = Terminal growth rate (typically 2-3%)
- r = WACC

Example: $1,874 × 1.03 ÷ (0.096 - 0.03) = $29,393M
```

**Method B: Exit Multiple**
```
Terminal Value = EBITDA_5 × Comparable Multiple

Example: $3,660M × 8.0x = $29,280M
```

#### Step 5: Discount All Cash Flows to Present Value
```
PV = FCFF ÷ (1 + WACC)^t

Example Year 1: $1,280 ÷ 1.096^1 = $1,168M
```

| Year | FCFF | Discount Factor (9.6%) | Present Value |
|------|------|----------------------|---------------|
| 1 | $1,280 | 0.912 | $1,167 |
| 2 | $1,408 | 0.832 | $1,172 |
| 3 | $1,549 | 0.759 | $1,176 |
| 4 | $1,704 | 0.693 | $1,181 |
| 5 | $1,874 | 0.632 | $1,185 |
| **Sum (1-5)** | | | **$5,881** |
| Terminal Value | $29,393 | 0.632 | $18,569 |
| **Enterprise Value** | | | **$24,450** |

#### Step 6: Calculate Equity Value
```
Equity Value = Enterprise Value - Net Debt

Example: $24,450M - $2,000M = $22,450M
Implied Share Price = $22,450M ÷ 500M shares = $44.90
```

---

## 5. Method 3: Dividend Discount Model (DDM)

### The Concept
For companies that pay dividends, we can value them based on expected future dividend payments.

### Gordon Growth Model (Constant Growth)
```
P_0 = D_1 ÷ (r - g)

Where:
- P_0 = Current stock price
- D_1 = Expected dividend next year
- r = Required rate of return (Cost of Equity)
- g = Dividend growth rate (constant)
```

### Example
| Input | Value |
|-------|-------|
| Dividend (D_0) | $2.00 |
| Growth Rate (g) | 5% |
| Required Return (r) | 10% |
| D_1 (Next Year) | $2.10 |

**Calculation:**
```
P_0 = $2.10 ÷ (0.10 - 0.05) = $42.00
```

### Two-Stage DDM

For companies with high initial growth that eventually stabilize:

```
P_0 = Σ [D_0 × (1+g_s)^t ÷ (1+r)^t] + D_n × (1+g_L) ÷ ((r - g_L) × (1+r)^n)
```

---

### 📊 DDM Worked Example: Two-Stage Model

A company pays $2.00 dividend today, grows at 15% for 5 years, then settles at 5% forever. Required return is 10%.

| Year | Dividend Growth | Dividend | PV Factor (10%) | PV of Dividend |
|------|----------------|----------|-----------------|----------------|
| 1 | 15% | $2.30 | 0.909 | $2.09 |
| 2 | 15% | $2.65 | 0.826 | $2.19 |
| 3 | 15% | $3.04 | 0.751 | $2.28 |
| 4 | 15% | $3.50 | 0.683 | $2.39 |
| 5 | 15% | $4.02 | 0.621 | $2.50 |
| **PV (High Growth)** | | | | **$11.45** |

**Terminal Value (Year 5):**
```
D_6 = $4.02 × 1.05 = $4.22
Terminal Value = $4.22 ÷ (0.10 - 0.05) = $84.40
PV of Terminal = $84.40 × 0.621 = $52.41
```

**Total Intrinsic Value:**
```
P_0 = $11.45 + $52.41 = $63.86
```

> **💡 Analyst Note:** The Two-Stage DDM is commonly used for companies in transition—e.g., a tech company shifting from high-growth startup to mature stable growth.

---

## 6. Method 4: Sum-of-the-Parts (SOTP)

### The Concept
Value each business segment separately, then sum them up. Best for conglomerates.

### Example - Conglomerate
| Segment | Valuation Method | Value |
|---------|-----------------|-------|
| Tech Division | DCF | $50B |
| Retail Division | Comps | $30B |
| Real Estate | Asset-based | $10B |
| Corporate Overhead | - | ($2B) |
| **Total Enterprise Value** | | **$88B** |

---

## 7. Sensitivity Analysis
The researcher doesn't just guess one price. They create a "What If" table:

| Stock Price | If WACC is 8.6% | 9.6% | 10.6% |
|-------------|-----------------|------|--------|
| Terminal g = 2.0% | $62.50 | $50.20 | $41.80 |
| Terminal g = 3.0% | $74.47 | $57.30 | $46.20 |
| Terminal g = 4.0% | $91.20 | $67.50 | $52.40 |

If the stock is trading at $50 but your analysis shows it's worth $67 in the worst case, **don't buy it**.

---

### 📊 Buy/Hold/Sell: The Analyst Recommendation Matrix

| Upside vs. Current Price | Recommendation | Rationale |
|-------------------------|----------------|-----------|
| > +20% | **STRONG BUY** | Significant margin of safety |
| +10% to +20% | **BUY** | Solid upside, acceptable risk |
| 0% to +10% | **HOLD** | Fair value; no obvious bargain |
| -10% to 0% | **UNDERPERFORM / SELL** | Trading above intrinsic value |
| < -10% | **STRONG SELL** | Significant overvaluation |

> **💡 Analyst Note:** Different Wall Street houses use different naming conventions. Some use "Buy/Sell/Hold," others use "Outperform/Neutral/Underperform." The math is the same: **Upside = (Intrinsic Value ÷ Current Price) - 1**.

---

## Final Recap

🏃 **Executive Summary:**

1. **P/E Ratio:** "Time to payback." Compare within industry; use Forward P/E for growth stocks.
2. **DCF:** Discount future cash flows (FCFE or FCFF) to find Intrinsic Value.
3. **DDM:** For dividend-paying companies; use Two-Stage for high-growth phase.
4. **Margin of Safety:** Only buy if Intrinsic Value > Market Price by > 20%.

**High Retention Recap:** Think of buying a stock like buying a lemonade stand. Calculate the P/E to see how many years it takes to pay you back, use the DCF to forecast future cash and bring it to today's dollars, and only buy if you're getting a deal (Margin of Safety).

**Python Tool**: [Run Equity_DCF.py](./Python/Equity_DCF.py)

---

## Outlook & The Real World

### What We Didn't Cover

- **Fama-French 3-Factor Model:** Explains returns using Size (SMB), Value (HML), and Market (MKT) factors.
- **Reverse DCF:** Finding the growth rate "implied" by the current stock price.
- **Earnings Power Value (EPV):** A simplified DCF using normalized earnings instead of forecasting.

### Recommended Next Steps

- **CFA Level I:** Study "Equity Valuation" and "Discounted Cash Flow" sections.
- **Practice:** Use Yahoo Finance to pull real multiples for companies you follow.
- **Read:** *Security Analysis* by Benjamin Graham and David Dodd—the classic text on intrinsic value.

---

*Last updated: 2026 | Built for learning and interview prep*
