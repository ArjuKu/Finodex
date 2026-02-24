# WACC Explained: Weighted Average Cost of Capital

## What is WACC?

**WACC (Weighted Average Cost of Capital)** is the average rate a company pays to finance its assets. It's the "hurdle rate" - the minimum return investors require.

Think of it as:
- The "price" of capital
- The discount rate used in DCF valuations
- The benchmark for evaluating investments

---

## Why Does WACC Matter?

1. **Valuation:** Used to discount future cash flows in DCF
2. **Investment Decisions:** Projects should earn more than WACC
3. **Performance Measurement:** ROIC should exceed WACC for value creation

---

## The WACC Formula

```
WACC = (E/V × Re) + (D/V × Rd × (1-T))

Where:
E = Market value of equity
D = Market value of debt
V = E + D (total capital)
Re = Cost of equity
Rd = Cost of debt
T = Tax rate
```

---

## Understanding Each Component

### 1. Cost of Equity (Re)

The return equity investors demand. Calculated using **CAPM**:

```
Re = Rf + β × (Rm - Rf)

Where:
Rf = Risk-free rate (usually 10-year Treasury)
β = Beta (systematic risk)
Rm = Expected market return
(Rm - Rf) = Market Risk Premium
```

**Example:**
- Rf = 4.5% (10-year Treasury)
- β = 1.20 (stock is 20% more volatile than market)
- Rm - Rf = 6.0% (historical market risk premium)

```
Re = 4.5% + 1.20 × 6.0% = 11.7%
```

### 2. Cost of Debt (Rd)

The interest rate the company pays on its debt.

**After-tax cost:**
```
Rd(after-tax) = Rd(pre-tax) × (1 - T)
```

**Example:**
- Pre-tax cost = 6.0%
- Tax rate = 21%
- Rd(after-tax) = 6.0% × (1 - 0.21) = 4.74%

### 3. Capital Structure Weights

```
E/V = Market Value of Equity / Total Capital
D/V = Market Value of Debt / Total Capital
```

**Example:**
- Market Cap = $75M
- Net Debt = $25M
- Total Capital = $100M

- E/V = 75/100 = 75%
- D/V = 25/100 = 25%

---

## Complete WACC Calculation Example

### Step 1: Calculate Cost of Equity (CAPM)

| Input | Value |
|-------|-------|
| Risk-Free Rate | 4.5% |
| Beta | 1.20 |
| Market Risk Premium | 6.0% |

```
Re = 4.5% + 1.20 × 6.0% = 11.7%
```

### Step 2: Calculate Cost of Debt

| Input | Value |
|-------|-------|
| Pre-tax Cost of Debt | 6.0% |
| Tax Rate | 21% |

```
Rd(after-tax) = 6.0% × (1 - 0.21) = 4.74%
```

### Step 3: Calculate Weights

| Input | Value |
|-------|-------|
| Market Value of Equity | $75M |
| Market Value of Debt | $25M |
| Total Capital | $100M |

- E/V = 75%
- D/V = 25%

### Step 4: Calculate WACC

```
WACC = (0.75 × 11.7%) + (0.25 × 4.74%)
WACC = 8.78% + 1.19%
WACC = 9.97% ≈ 10%
```

---

## Beta Explained

Beta measures how much a stock moves relative to the market.

| Beta | Interpretation |
|------|----------------|
| 0.5 | Half as volatile as market |
| 1.0 | Same as market |
| 1.5 | 50% more volatile than market |
| 2.0 | Twice as volatile |

### How to Get Beta:
1. **Regression:** Calculate from historical prices vs. market
2. **Industry average:** Use comparable companies
3. **Bloomberg/Reuters:** Market data providers

### Relevering Beta:

If your company has different debt than the industry:

```
βL = βU × [1 + (1-T) × (D/E)]

Where:
βL = Levered beta (with debt)
βU = Unlevered beta (no debt)
D/E = Debt-to-Equity ratio
```

---

## Market Risk Premium (MRP)

The extra return investors expect for holding stocks over risk-free assets.

**Historical MRP (US):**
- Long-term average: 5-7%
- Currently: 5-6%

**How to estimate MRP:**
- Historical returns (1928-2023): ~6%
- Use 5-7% range in models

---

## Typical WACC by Industry

| Industry | Typical WACC | Reason |
|----------|--------------|--------|
| Utilities | 5-7% | Stable, low risk |
| Banks | 8-10% | Higher risk, regulated |
| Manufacturing | 8-12% | Moderate risk |
| Technology | 10-15% | High growth, volatile |
| Biotech | 12-18% | High risk, binary outcomes |

---

## Using WACC in Valuation

### In DCF Analysis:

```
Present Value = FCF / (1 + WACC)^t
```

**Example:**
- Year 1 FCF = $100M
- WACC = 10%
- PV = $100M / 1.10 = $90.9M

### As an Investment Hurdle:

| Metric | Decision |
|--------|----------|
| IRR > WACC | Accept project |
| IRR < WACC | Reject project |
| ROIC > WACC | Value creation |
| ROIC < WACC | Value destruction |

---

## Sensitivity Analysis

Always test how WACC affects valuation:

| WACC | Implied Price |
|------|---------------|
| 8% | $85 |
| 9% | $70 |
| 10% | $58 |
| 11% | $50 |
| 12% | $42 |

Higher WACC = Lower valuation

---

## Common Mistakes

1. **Using book values** - Use market values for weights
2. **Forgetting tax shield** - Always use after-tax cost of debt
3. **Wrong beta** - Ensure beta matches capital structure
4. **Ignoring risk** - Higher risk = higher WACC

---

## Sources

- CFA Institute - "Cost of Capital"
- Corporate Finance Institute
- NYU Stern - Cost of Capital by Sector
- Damodaran Data

---

## Related Files

- `wacc_calculator.csv` - Excel calculator
- `capm_calculator.py` - Python implementation
- `dcf_model.csv` - Uses WACC for DCF
