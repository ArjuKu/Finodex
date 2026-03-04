# Equities - Pricing Models

**Objective:** Calculating the "Required Rate of Return" and the cost of investing in a stock.

---

## Table of Contents

1. [The "Voting Machine vs. Weighing Machine"](#the-voting-machine-vs-weighing-machine)
2. [Pricing vs. Valuation](#pricing-vs-valuation)
3. [Method 1 - CAPM (Capital Asset Pricing Model)](#method-1---capm-capital-asset-pricing-model)
4. [Method 2 - WACC (Weighted Average Cost of Capital)](#method-2---wacc-weighted-average-cost-of-capital)
5. [Method 3 - Multi-Factor Models](#method-3---multi-factor-models)
6. [Final Recap](#final-recap)

---

## The "Voting Machine vs. Weighing Machine"

> *"In the short run, the market is a voting machine. In the long run, it's a weighing machine."* — Benjamin Graham

- **Voting Machine (Short Term):** Stock prices move based on emotion, news, and crowd behavior. One day the market "votes" a stock up; the next day, it votes it down.
- **Weighing Machine (Long Term):** Over time, the stock price converges to its intrinsic value—the true worth of the business.

> **💡 Analyst Note:** Your job as an equity researcher is to ignore the "voting" (short-term noise) and focus on the "weighing" (intrinsic value).

---

## Pricing vs. Valuation

| Concept | Definition | Question |
|---------|------------|----------|
| **Valuation** | "What is it worth?" | What is the intrinsic value? |
| **Pricing** | "What return do I require?" | What is the "hurdle rate" for this risk? |

> **Key Insight:** Valuation tells you the **destination** (the fair price). Pricing tells you the **hurdle** (the return you need to justify the risk).

---

## Method 1 - CAPM (Capital Asset Pricing Model)

### The Concept

How much extra profit do I need to earn for taking a risk on a specific stock?

### The Formula

```
Cost of Equity (r_e) = Risk-Free Rate + Beta × (Market Risk Premium)

Where:
- r_e = Required return on equity (the "price" of risk)
- R_f = Risk-free rate (10-year Treasury)
- β (Beta) = Measure of systematic risk
- (R_m - R_f) = Equity Risk Premium (ERP)
```

### 📊 CAPM Walkthrough Example

| Input | Value |
|-------|-------|
| Risk-Free Rate (R_f) | 4.5% |
| Beta (β) | 1.20 |
| Market Risk Premium (R_m - R_f) | 6.0% |

**Calculation:**
```
r_e = 4.5% + 1.20 × 6.0%
r_e = 4.5% + 7.2%
r_e = 11.7%
```

> **💡 Analyst Note:** This 11.7% is your **required return**. If the stock's expected return (based on your DCF) is higher than 11.7%, it's a buy. If lower, it's overvalued.

---

### Beta: The "Risk Dial"

| Beta Value | Interpretation | Example |
|------------|---------------|---------|
| **β = 0.5** | Half as volatile as market | Utility companies |
| **β = 1.0** | Moves with the market | S&P 500 Index |
| **β = 1.5** | 50% more volatile | High-growth tech |
| **β = 2.0** | Double the market volatility | Speculative stocks |

> **💡 CFA Insight:** Beta measures **systematic risk**—the risk that cannot be diversified away. Company-specific risk (e.g., a CEO resigns) is "unsystematic" and can be diversified away by holding 30+ stocks.

---

## Method 2 - WACC (Weighted Average Cost of Capital)

### The Concept

What is the total cost to fund the entire company (both loans and shares)? This is the "hurdle rate" for the entire business.

### The Formula

```
WACC = (E/V) × r_e + (D/V) × r_d × (1 - Tax Rate)

Where:
- E = Market value of equity
- D = Market value of debt
- V = E + D (total firm value)
- r_e = Cost of equity (from CAPM)
- r_d = Cost of debt (interest rate)
- Tax Rate = Corporate tax rate
```

### 📊 WACC Walkthrough Example

| Input | Value |
|-------|-------|
| Market Value of Equity | $800M |
| Market Value of Debt | $200M |
| Total Firm Value (V) | $1,000M |
| Weight of Equity (E/V) | 80% |
| Weight of Debt (D/V) | 20% |
| Cost of Equity (r_e) | 11.7% |
| Cost of Debt (r_d) | 6.0% |
| Tax Rate | 21% |

**Calculation:**
```
WACC = (0.80 × 11.7%) + (0.20 × 6.0% × (1 - 0.21))
WACC = 9.36% + 0.95%
WACC = 10.3%
```

> **💡 Analyst Note:** WACC is used in DCF to discount **FCFF** (Free Cash Flow to Firm). If you're discounting **FCFE** (Equity cash flows), use **Cost of Equity (CAPM)** directly.

---

## Method 3 - Multi-Factor Models

### The "Level 2" View: Fama-French

The CAPM says only "market risk" matters. The **Fama-French 3-Factor Model** says returns are explained by three factors:

| Factor | Definition | What It Captures |
|--------|------------|------------------|
| **MKT** | Market Return | Overall stock market performance |
| **SMB** | Small Minus Big | Small companies outperform large (size premium) |
| **HML** | High Minus Low | Value stocks outperform growth (value premium) |

### The Formula

```
r = R_f + β_MKT × (R_m - R_f) + β_SMB × SMB + β_HML × HML
```

> **💡 Analyst Note:** If you see a stock trading at a "cheap" P/E but it's a small growth stock, part of that "cheapness" might just be the Size and Value premiums—not a true bargain.

---

## Final Recap

🏃 **Executive Summary:**

1. **CAPM** tells you what return to demand for a specific stock based on its Beta.
2. **WACC** tells you the "hurdle rate" for the entire company (debt + equity).
3. **Multi-Factor Models** explain returns using Size, Value, and Market factors.
4. **Pricing** is the hurdle; **Valuation** is the destination.

> **The Golden Rule:** Never buy a stock unless its expected return > required return (from CAPM/WACC).

**Python Tool**: [Run CAPM_Calculator.py](./Python/CAPM_Calculator.py)

---

## Outlook & The Real World

### What We Didn't Cover

- **Build-Up Method:** Adding risk premiums for size, country, and liquidity to CAPM.
- **Cost of Debt (After-Tax):** Using the yield to maturity on existing debt.
- **Target Capital Structure:** How companies decide their optimal debt/equity mix.

### Recommended Next Steps

- **CFA Level I:** Study "Risk and Return" and "Portfolio Management."
- **CFA Level II:** Deep dive into "Equity Valuation" and "Fixed Income."
- **Practice:** Pull Beta and financial data from Bloomberg or Yahoo Finance for real companies.

---

*Last updated: 2026 | Built for learning and interview prep*
