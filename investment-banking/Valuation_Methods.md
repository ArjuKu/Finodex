# Investment Banking - Valuation Methods

**Objective:** Valuing a company for a **Transaction** (M&A, IPO, or LBO).

---

## Table of Contents

1. [The "Machine Factory" Metaphor](#1-the-machine-factory-metaphor)
2. [The IB Dictionary](#2-the-ib-dictionary)
3. [Understanding the Discount Rate (WACC & CAPM)](#3-understanding-the-discount-rate-wacc--capm)
4. [Method 1: Precedent Transactions](#4-method-1-precedent-transactions)
5. [Method 2: Corporate DCF (Unlevered FCF)](#5-method-2-corporate-dcf-unlevered-fcf)
6. [Method 3: Accretion/Dilution Analysis](#6-method-3-accretiondilution-analysis)
7. [IB Interview Cheat Sheet](#7-ib-interview-cheat-sheet)
8. [Summary](#8-summary)

---

## 1. The "Machine Factory" Metaphor

Imagine you want to buy a **machine factory**.

- You don't just want to buy one machine; you want the **entire building**, all the machines inside, the brand, the customer list, and the contracts.
- To do this, you take out a **loan** (debt) from a bank and use your own cash (equity) for the rest.
- You plan to pay back the loan using the factory's daily profits from selling widgets.

**The Key Insight:** In Investment Banking, we aren't looking for "fair market value" alone. We're looking for the **Transaction Price**—the price at which a willing buyer and willing seller agree to complete a deal.

---

## 2. The IB Dictionary

Before we look at the math, let's define the terms:

- **Enterprise Value (EV):** The "Total Price Tag." It's the cost to buy the equity PLUS pay off all the company's debts.
  
  ```
  EV = Market Cap + Total Debt - Cash
  ```

- **Equity Value:** The market value of all the shares. If you own the equity, you own the "upside" after all debts are paid.

- **EBITDA:** "Profit before the bankers and accountants touch it." It stands for **E**arnings **B**efore **I**nterest, **T**axes, **D**epreciation, and **A**mortization. It shows the raw earning power of the business.

- **EBIT:** Earnings Before Interest and Taxes. The profit from operations, ignoring how the company is financed.

- **NOPAT:** Net Operating Profit After Tax. The cash flow available to all investors if the company had no debt.

  ```
  NOPAT = EBIT × (1 - Tax Rate)
  ```

- **Unlevered FCF (UFCF):** Cash flow available to ALL investors (debt + equity) before debt payments. Also called **Free Cash Flow to Firm (FCFF)**.

- **Control Premium:** An extra fee (usually 20-30%) paid to convince current owners to give up control of their company.

- **Synergies:** Cost savings or revenue boosts that only happen after the deal closes. *"If I buy your factory, I can fire one of our two accountants because we only need one now."*

- **Net Debt:** Total Debt minus Cash. This is the "debt burden" left after subtracting the cash the company already has.

  ```
  Net Debt = Total Debt - Cash
  ```

---

## 3. Understanding the Discount Rate (WACC & CAPM)

In a DCF, we discount future cash flows back to today's value. But what rate do we use? That's where **WACC** comes in.

### 3.1 What is WACC?

**WACC (Weighted Average Cost of Capital)** is the "hurdle rate"—the return required by both debt and equity investors. Think of it as the "rent" you pay for using other people's money to buy the factory.

> **💡 Schweser Note:** If your factory generates a 7% return but your WACC is 9%, you are effectively destroying value. The WACC is the "Hurdle"—any deal must earn more than this rate to create value for investors.

```
WACC = (E/V) × Ke + (D/V) × Kd × (1 - Tax Rate)

Where:
- E = Market Value of Equity
- D = Market Value of Debt
- V = E + D (Total Value)
- Ke = Cost of Equity (required return for shareholders)
- Kd = Cost of Debt (interest rate on loans)
- Tax Rate = Corporate tax rate
```

### 3.2 Cost of Equity (CAPM)

How do we calculate the return shareholders require? Use the **CAPM Model**:

```
Ke = Rf + β × (Rm - Rf)

Where:
- Rf = Risk-Free Rate (e.g., 10-year Treasury yield, ~4-5%)
- β (Beta) = Measure of the stock's volatility vs. the market
- (Rm - Rf) = Equity Risk Premium (market return minus risk-free, ~5-7%)
```

**Example:**
| Input | Value |
|-------|-------|
| Risk-Free Rate (Rf) | 4.5% |
| Beta (β) | 1.2 |
| Equity Risk Premium | 6.0% |
| **Cost of Equity (Ke)** | **4.5% + 1.2 × 6.0% = 11.7%** |

> **💡 Schweser Note (Beta):** Think of Beta as the factory's "sensitivity dial." A β of 1.2 means: if the market moves 10% up or down, this factory's value is expected to swing 12%. Higher Beta = riskier factory = investors demand a higher return.

### 3.3 Putting It Together: WACC Calculation

| Item | Calculation | Value |
|------|-------------|-------|
| Cost of Equity (Ke) | From CAPM | 11.7% |
| Cost of Debt (Kd) | Interest rate on debt | 6.0% |
| Tax Rate | Corporate tax | 21% |
| Debt/Value Ratio (D/V) | Target capital structure | 40% |
| Equity/Value Ratio (E/V) | Target capital structure | 60% |

**WACC Calculation:**
```
WACC = (0.60 × 11.7%) + (0.40 × 6.0% × (1 - 0.21))
WACC = 7.02% + 1.90%
WACC = 8.92% (rounded to 9.0%)
```

---

## 4. Method 1: Precedent Transactions

### The Concept

**"What did the neighbors' businesses sell for?"** We look at past M&A deals in the same industry and apply those multiples to our target.

### Formula

```
Estimated Transaction Value = Target EBITDA × Median Transaction Multiple
```

### The Nuance

You must add the **Control Premium**. If similar companies trade on the stock market at 10x EBITDA, a buyer might pay 13x EBITDA to take over the whole company (that's the 30% premium).

> **💡 Schweser Note (The "Takeover Tax"):** The stock price you see on Google Finance is for a "Passive Investor"—one tiny slice of the factory. You can't fire the CEO or sell the land with one share. To buy the whole building and change the business, you must pay a "Takeover Tax" (Control Premium) to convince everyone to sell.

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

## 5. Method 2: Corporate DCF (Unlevered FCF)

### The Concept

How much cash can this business produce for *everyone* (both the people who lent money and the people who own shares)?

### The "IB First" Difference

Bankers use **Unlevered FCF** because it's independent of how the company is funded. It allows us to see how much cash the company makes *before* we decide how much debt to use to buy it.

### Core Formula

```
Unlevered Free Cash Flow (UFCF) = NOPAT + D&A - CapEx - ΔNWC
```

Where:
- **NOPAT** = EBIT × (1 - Tax Rate)
- **D&A** = Depreciation & Amortization (non-cash, added back)
- **CapEx** = Capital Expenditures (cash spent on equipment)
- **ΔNWC** = Change in Net Working Capital

> **💡 Schweser Notes (Cash vs. Accounting):**
> - **+ D&A:** "Accounting fiction." Depreciation isn't a real cash outflow—machines just got older on paper. We add it back because the cash is still in the building.
> - **- CapEx:** "The Reality Check." You can't run a factory for free. This is the actual check you write to buy or upgrade equipment.
> - **- ΔNWC:** "The Working Cash Trap." If customers haven't paid their invoices yet (Accounts Receivable), that money is "trapped" and isn't truly "Free" cash yet.

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

There are **two methods** bankers use for Terminal Value:

---

**Method A: Gordon Growth (Perpetuity Growth)**

Assumes the company grows at a constant rate forever.

```
Terminal Value = UFCF_5 × (1 + g) ÷ (WACC - g)

Where:
- g = Perpetual growth rate (typically 2-3%)
- WACC = Discount rate

Example: 
- UFCF_5 = $187M
- g = 3%
- WACC = 10%
- TV = $187 × 1.03 ÷ (0.10 - 0.03) = $2,753M
- PV of TV = $2,753 ÷ 1.10^5 = $1,709M
```

---

**Method B: Exit Multiple (Market Comparables)**

Assumes you sell the company at a multiple similar to public market comparables.

```
Terminal Value = EBITDA_5 × Exit Multiple

Example:
- EBITDA_5 = $366M ($293M EBIT + $73M D&A)
- Exit Multiple = 8.0x
- TV = $366M × 8.0 = $2,928M
- PV of TV = $2,928 ÷ 1.10^5 = $1,819M
```

**Which method do bankers prefer?** For M&A, **Exit Multiple** is often preferred because:
1. It's easier to explain to clients ("We're selling at 8x EBITDA, like the comparables").
2. Perpetual growth rates above 3% are unrealistic for mature businesses.

> **💡 Schweser Note (Theory vs. Practice):**
> - **Gordon Growth:** Treats the factory as a "Forever Asset" that grows at the rate of inflation (2-3%). Useful for stable, mature businesses.
> - **Exit Multiple:** Treats the factory as a "Deal Asset." We're not running it forever—we're planning to sell it to someone else in 5 years based on current market conditions. Bankers prefer this because it's anchored in real-world transaction multiples.

---

#### Step 6: Enterprise Value

```
Enterprise Value = PV of FCF + PV of Terminal Value
EV = $580M + $1,709M = $2,289M (Gordon Growth)
EV = $580M + $1,819M = $2,399M (Exit Multiple)
```

#### Step 7: Bridge to Equity Value

```
Equity Value = Enterprise Value - Net Debt

Example:
- EV = $2,289M
- Less: Net Debt = ($500M)
- Equity Value = $1,789M
- Implied Share Price = Equity Value ÷ Shares Outstanding
```

**Python Tool**: [Run Corporate_DCF.py](./Python/Corporate_DCF.py)

---

## 6. Method 3: Accretion/Dilution Analysis

### The Concept

When one company buys another, the most important question for the buyer's shareholders is: **"Does this make my Earnings Per Share (EPS) go up or down?"**

### Formulas

```
Accretion % = (New EPS - Old EPS) ÷ Old EPS

New EPS = Combined Net Income ÷ Combined Shares Outstanding
```

### Example - Accretion Analysis

| Item | Acquirer (Buyer) | Target | Combined |
|------|------------------|--------|----------|
| Net Income | $500M | $100M | $600M |
| Shares Outstanding | 100M | 50M | 120M (acquirer issues 20M new shares to pay) |
| EPS | $5.00 | $2.00 | $5.00 |

**Calculation:**
- Buyer EPS before: $5.00
- Combined EPS: $600M ÷ 120M = $5.00
- **Accretion/(Dilution):** 0%

> **💡 Schweser Note (The "Pie Slicing" Analogy):** When a buyer issues shares to buy a target, they are creating more "slices" of their own pie. If the target's earnings don't add enough "filling" to compensate for the extra slices, the original shareholders get less per slice (**Dilution**). The goal is always to grow the **EPS** (the size of each slice).

### Interpretation

- **EPS Goes Up** = **Accretive** (Good Deal!)
- **EPS Goes Down** = **Dilutive** (Bad Deal!)

---

## 7. IB Interview Cheat Sheet

Memorize these formulas for technical interviews:

### Cash Flow Formulas

| Formula | Description |
|---------|-------------|
| **FCFF = NOPAT + D&A - CapEx - ΔNWC** | Free Cash Flow to Firm (Unlevered) |
| **NOPAT = EBIT × (1 - Tax Rate)** | Cash flow available to all investors |
| **ΔNWC = Current NWC - Prior NWC** | Change in Net Working Capital |

### Valuation Formulas

| Formula | Description |
|---------|-------------|
| **EV = PV of FCFs + PV of Terminal Value** | Enterprise Value |
| **Equity Value = EV - Net Debt** | Value of shares |
| **Implied Share Price = Equity Value ÷ Shares Outstanding** | Price per share |

### Terminal Value Formulas

| Formula | Description |
|---------|-------------|
| **TV (Gordon Growth) = FCFn × (1+g) ÷ (WACC - g)** | Perpetuity method |
| **TV (Exit Multiple) = EBITDA_n × Multiple** | Multiple method |

### Discount Rate Formulas

| Formula | Description |
|---------|-------------|
| **CAPM: Ke = Rf + β × (Rm - Rf)** | Cost of Equity |
| **WACC = (E/V) × Ke + (D/V) × Kd × (1-t)** | Weighted Average Cost of Capital |

### M&A Premium

| Formula | Description |
|---------|-------------|
| **Purchase Price = Equity Value × (1 + Premium%)** | Total deal value |

---

## 8. Summary

Investment Banking valuation is about finding the **clearing price** for a deal.

1. **Precedent Transactions:** Look at what others paid in similar deals.
2. **Corporate DCF:** Project the cash flows and bring them to today's value.
3. **Accretion/Dilution:** Ensure the buyer's EPS doesn't get diluted.

**High Retention Recap:** If you want to buy the whole factory, look at the neighbor's price, make sure the machines produce enough cash to justify the total "Transaction Price Tag," and ensure the deal makes your shareholders richer, not poorer.

**Python Tool**: [Run Corporate_DCF.py](./Python/Corporate_DCF.py)
