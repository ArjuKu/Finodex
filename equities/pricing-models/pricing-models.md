# Equities - Pricing Models

Core models for determining the required return on equity and cost of capital.

---

## 1. Capital Asset Pricing Model (CAPM)

### Overview
CAPM describes the relationship between systematic risk and expected return for assets, particularly equities.

### Formula
```
Re = Rf + β × (Rm - Rf)

Where:
Re = Expected return on equity (required return)
Rf = Risk-free rate
β = Beta (systematic risk)
Rm = Expected return on market
(Rm - Rf) = Market Risk Premium (MRP)
```

### Components
| Component | Description | Typical Source |
|-----------|-------------|----------------|
| Risk-Free Rate (Rf) | Return on zero-risk asset | 10-Year Treasury |
| Beta (β) | Measure of systematic risk | Regression vs index |
| Market Risk Premium | Additional return for market risk | Historical (5-7%) |

### Beta Interpretation
| Beta | Interpretation |
|------|---------------|
| β = 0 | No systematic risk |
| β < 1 | Less volatile than market |
| β = 1 | Same volatility as market |
| β > 1 | More volatile than market |
| β < 0 | Negative correlation to market |

### Example Calculation
| Parameter | Value |
|-----------|-------|
| Risk-Free Rate | 4.50% |
| Market Return | 10.00% |
| Market Risk Premium | 5.50% |
| Beta | 1.25 |
| **Expected Return** | **11.38%** |

### Limitations of CAPM
- Assumes single-factor model
- Risk-free rate may not exist
- Beta may be unstable
- May not explain all returns

---

## 2. Weighted Average Cost of Capital (WACC)

### Overview
WACC represents the average cost of capital from all sources (debt and equity).

### Formula
```
WACC = (E/V × Re) + (D/V × Rd × (1-T))

Where:
E = Market value of equity
D = Market value of debt
V = E + D (total capital)
Re = Cost of equity
Rd = Cost of debt
T = Corporate tax rate
```

### Expanded Formula (with Preferred Stock)
```
WACC = (E/V × Re) + (P/V × Rp) + (D/V × Rd × (1-T))

Where:
P = Market value of preferred stock
Rp = Cost of preferred stock
```

### Example Calculation
| Component | Value | Weight | Cost | Weighted Cost |
|-----------|-------|--------|------|---------------|
| Equity | $75M | 75% | 12% | 9.00% |
| Debt | $25M | 25% | 6% | 4.50% × (1-21%) = 3.56% |
| **WACC** | | | | **12.56%** |

### WACC Usage
- Discount rate for FCFF
- Hurdle rate for capital projects
- Performance benchmark
- Valuation (DCF)

---

## 3. Beta Calculation

### Definition
Beta measures a stock's volatility relative to the overall market.

### Formula (Regression)
```
β = Cov(Ri, Rm) / Var(Rm)

Where:
Ri = Return on stock
Rm = Return on market
```

### Beta Types
| Type | Description | Formula |
|------|-------------|---------|
| Levered Beta | Reflects business + financial risk | βL = βU × [1 + (1-T) × D/E] |
| Unlevered Beta | Business risk only | βU = βL / [1 + (1-T) × D/E] |

### Example - Unlevering and Relevering
| Input | Value |
|-------|-------|
| Industry Unlevered Beta | 1.00 |
| Industry D/E Ratio | 0.50 |
| Target Company D/E Ratio | 1.00 |
| Tax Rate | 21% |

**Step 1: Relever Beta**
```
βL = 1.00 × [1 + (1-0.21) × 1.00]
βL = 1.00 × 1.79
βL = 1.79
```

### Beta Estimation Methods
1. **Historical Regression** - Calculate from price data
2. **Bottom-up Beta** - Industry beta + capital structure
3. **Pure-play Method** - Use comparable company betas

---

## 4. Gordon Growth Model (Dividend Pricing)

### Overview
Values a stock based on expected future dividends growing at a constant rate.

### Formula
```
P_0 = D_1 / (r - g)

Where:
P_0 = Current stock price
D_1 = Dividend next year
r = Required return
g = Dividend growth rate
```

### Solving for Required Return
```
r = (D_1 / P_0) + g

Where:
(D_1 / P_0) = Dividend Yield
g = Capital gains yield
```

### Example
| Parameter | Value |
|-----------|-------|
| Current Dividend | $4.00 |
| Dividend Growth Rate | 5% |
| Stock Price | $50.00 |
| Expected Dividend (D1) | $4.20 |
| **Required Return** | **13.40%** |

---

## 5. Cost of Equity - Other Methods

### Build-Up Method
```
Re = Rf + β × MRP + Size Premium + Specific Risk Premium
```

### Empirical CAPM
```
Re = Rf + β × MRP + α (alpha)
```

### Three-Factor Model (Fama-French)
```
Re = Rf + βM × (Rm - Rf) + βS × SMB + βH × HML

Where:
SMB = Small Minus Big (size factor)
HML = High Minus Low (value factor)
```

### Five-Factor Model (Fama-French)
```
Re = Rf + βM × (Rm - Rf) + βS × SMB + βH × HML + βRMW × RMW + βCMA × CMA

Where:
RMW = Robust Minus Weak (profitability)
CMA = Conservative Minus Aggressive (investment)
```

---

## 6. Cost of Debt

### Pre-Tax Cost of Debt
| Method | Description |
|--------|-------------|
| Market Yield | YTM on outstanding debt |
| Credit Rating | Yield based on rating |
| Interest Coverage | Debt rating implied |

### After-Tax Cost of Debt
```
Rd(after-tax) = Rd(pre-tax) × (1 - T)
```

### Example
| Parameter | Value |
|-----------|-------|
| Pre-tax Cost of Debt | 6.0% |
| Tax Rate | 21% |
| **After-tax Cost** | **4.74%** |

---

## 7. WACC Calculator - Step by Step

### Step 1: Determine Capital Structure
| Source | Book Value | Market Value | Weight |
|--------|------------|--------------|--------|
| Equity | $100M | $150M | 75% |
| Debt | $50M | $45M | 25% |

### Step 2: Calculate Cost of Equity (CAPM)
| Parameter | Value |
|-----------|-------|
| Risk-Free Rate | 4.5% |
| Beta | 1.20 |
| Market Risk Premium | 6.0% |
| **Cost of Equity** | **11.7%** |

### Step 3: Calculate Cost of Debt
| Parameter | Value |
|-----------|-------|
| Pre-tax Cost | 5.5% |
| Tax Rate | 21% |
| **After-tax Cost** | **4.35%** |

### Step 4: Calculate WACC
```
WACC = (0.75 × 11.7%) + (0.25 × 4.35%)
WACC = 8.78% + 1.09%
WACC = 9.87%
```

---

## 8. Practical Applications

### When to Use WACC
| Application | WACC Usage |
|-------------|------------|
| DCF Valuation | Discount rate for FCFF |
| Capital Budgeting | Hurdle rate for projects |
| Performance Evaluation | Required ROIC |
| M&A | Discount rate for targets |

### Common WACC Ranges by Industry
| Industry | Typical WACC |
|----------|---------------|
| Utilities | 5-7% |
| Banks | 8-10% |
| Manufacturing | 8-12% |
| Technology | 10-15% |
| Biotech | 12-18% |

---

## 9. WACC Sensitivity Analysis Example

### Inputs
| Parameter | Low | Base | High |
|-----------|-----|------|------|
| Cost of Equity | 9% | 12% | 15% |
| Cost of Debt | 4% | 6% | 8% |
| Equity Weight | 60% | 70% | 80% |
| Tax Rate | 21% | 21% | 21% |

### Results
| Scenario | WACC |
|----------|------|
| Low Case | 7.02% |
| Base Case | 10.14% |
| High Case | 13.58% |

---

## Sources

- CFA Institute - "Cost of Capital"
- Corporate Finance Institute - "WACC Guide"
- Investopedia - "CAPM Explained"
- NYU Stern - "Cost of Capital by Sector"

---

## Notes

*Add your own calculations and observations*
