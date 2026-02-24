# Equities - Valuation Methods

Comprehensive guide to equity valuation techniques and methodologies.

---

## 1. Discounted Cash Flow (DCF)

### Overview
DCF values a company by calculating the present value of projected future cash flows.

### Types of Cash Flow
| Cash Flow Type | Formula | Use Case |
|----------------|---------|----------|
| FCFF (Free Cash Flow to Firm) | CFO - CapEx | Enterprise Value |
| FCFE (Free Cash Flow to Equity) | FCFF - Net Borrowing | Equity Value |

### Formula
```
Intrinsic Value = Σ (CF_t / (1 + r)^t) + Terminal Value

Where:
CF_t = Cash flow in period t
r = Discount rate (WACC for FCFF, Cost of Equity for FCFE)
t = Time period
```

### DCF Steps
1. Project revenue and expenses (5-10 years)
2. Calculate unlevered free cash flow
3. Determine discount rate (WACC)
4. Calculate terminal value
5. Sum present values

### Terminal Value Methods
| Method | Formula |
|--------|---------|
| Gordon Growth | TV = FCF_n × (1+g) / (r-g) |
| Exit Multiple | TV = EBITDA_n × Multiple |

---

## 2. Dividend Discount Model (DDM)

### Overview
Values a stock based on expected future dividend payments.

### Gordon Growth Model (Zero Growth)
```
P_0 = D / r

Where:
P_0 = Current price
D = Annual dividend (constant)
r = Required rate of return
```

### Gordon Growth Model (Constant Growth)
```
P_0 = D_1 / (r - g)

Where:
D_1 = Dividend next year
r = Required return
g = Dividend growth rate (constant)
```

### Two-Stage DDM
```
P_0 = Σ (D_0 × (1+g_s)^t / (1+r)^t) + D_n × (1+g_L) / ((r - g_L) × (1+r)^n)

Where:
g_s = Short-term growth rate
g_L = Long-term growth rate
n = Years of high growth
```

### When to Use DDM
- Dividend-paying companies
- Stable, mature businesses
- Utilities, REITs, banks
- Companies with predictable cash flows

---

## 3. Comparable Company Analysis (Comps)

### Overview
Value a company using multiples from similar publicly traded companies.

### Key Multiples
| Multiple | Formula | Best For |
|----------|---------|----------|
| P/E | Price / EPS | Growth companies |
| EV/EBITDA | Enterprise Value / EBITDA | Capital-intensive |
| P/B | Price / Book Value | Financial institutions |
| P/S | Price / Revenue | High growth, pre-profit |
| EV/Revenue | Enterprise Value / Revenue | SaaS, tech |

### Trading Comps Example
| Company | Market Cap | EV | Revenue | EBITDA | P/E | EV/EBITDA | P/S |
|---------|------------|-----|---------|--------|-----|-----------|-----|
| Company A | 100B | 110B | 50B | 15B | 20x | 7.3x | 2.0x |
| Company B | 80B | 85B | 40B | 12B | 18x | 7.1x | 2.0x |
| Company C | 60B | 65B | 30B | 8B | 15x | 8.1x | 2.0x |
| **Median** | | | | | **18x** | **7.3x** | **2.0x** |

### Steps for Comps
1. Select peer group (industry, size, growth)
2. Gather financial metrics
3. Calculate relevant multiples
4. Apply median/mean to target company
5. Adjust for differences (growth, leverage, size)

---

## 4. Precedent Transactions

### Overview
Value a company based on prices paid in similar M&A transactions.

### Key Multiples from Transactions
| Multiple | Description |
|----------|-------------|
| LTM P/E | Price / Last 12 months EPS |
| NTM P/E | Price / Next 12 months EPS |
| EV/EBITDA | Enterprise Value / EBITDA |
| EV/Revenue | Enterprise Value / Revenue |
| P/B | Price / Book Value |

### Transaction Comps Example
| Acquirer | Target | Date | EV | EV/EBITDA | Premium |
|----------|--------|------|-----|-----------|---------|
| Buyer A | Target X | 2023 | 15B | 12x | 25% |
| Buyer B | Target Y | 2023 | 10B | 11x | 20% |
| Buyer C | Target Z | 2024 | 8B | 10x | 15% |
| **Median** | | | | **11x** | **20%** |

### Key Considerations
- Historical transactions may be dated
- Synergies affect valuations
- Premiums vary by deal type
- Control premium typically 20-40%

---

## 5. Residual Income Valuation

### Overview
Values a company based on residual earnings - profits above the required return on equity.

### Formula
```
Residual Income = Net Income - (Equity × Cost of Equity)

V_0 = Book Value + Σ (RI_t / (1+r)^t)

Where:
RI_t = Residual income in period t
r = Cost of equity
```

### Example
| Item | Value |
|------|-------|
| Book Value per Share | $30 |
| Cost of Equity | 10% |
| Expected ROE | 15% |
| EPS | $4.50 |
| Residual Income per Share | $4.50 - ($30 × 10%) = $1.50 |

### When to Use
- Companies with predictable earnings
- Financial institutions
- Asset-heavy businesses
- Value investing

---

## 6. Sum-of-the-Parts (SOTP)

### Overview
Values each business segment separately and sums them up.

### Example - Conglomerate
| Segment | Valuation Method | Value |
|---------|-----------------|-------|
| Division A (Tech) | DCF | $50B |
| Division B (Retail) | Comps | $30B |
| Division C (Real Estate) | Asset-based | $10B |
| **Corporate Overhead** | | ($2B) |
| **Total Enterprise Value** | | **$88B** |

---

## 7. Asset-Based Valuation

### Methods
| Method | Formula |
|--------|---------|
| Book Value | Total Assets - Total Liabilities |
| Liquidation Value | Assets - Liabilities - Liquidation Costs |
| Replacement Cost | Cost to replace assets |

### When to Use
- Holding companies
- Financial institutions
- Distressed companies
- Asset-rich businesses (real estate, natural resources)

---

## 8. Step-by-Step DCF Example

### Company: TechCorp Inc.

**Step 1: Revenue Projections**
| Year | Revenue | Growth |
|------|---------|--------|
| 2024E | $10,000M | 10% |
| 2025E | $11,000M | 10% |
| 2026E | $12,100M | 10% |
| 2027E | $13,310M | 10% |
| 2028E | $14,641M | 10% |

**Step 2: FCFF Projections**
| Year | EBIT | Tax | NOPAT | +D&A | -CapEx | -NWC | FCFF |
|------|------|-----|-------|------|--------|------|------|
| 2024E | 2,000 | 420 | 1,580 | 500 | 600 | 200 | 1,280 |
| 2025E | 2,200 | 462 | 1,738 | 550 | 660 | 220 | 1,408 |
| 2026E | 2,420 | 508 | 1,912 | 605 | 726 | 242 | 1,549 |
| 2027E | 2,662 | 559 | 2,103 | 666 | 799 | 266 | 1,704 |
| 2028E | 2,928 | 615 | 2,313 | 732 | 878 | 293 | 1,874 |

**Step 3: Discount Rate (WACC)**
| Component | Value |
|-----------|-------|
| Cost of Equity | 12% |
| After-tax Cost of Debt | 4% |
| Equity Weight | 70% |
| Debt Weight | 30% |
| **WACC** | **9.6%** |

**Step 4: Present Value**
| Year | FCFF | Discount Factor | PV |
|------|------|-----------------|-----|
| 2024E | 1,280 | 0.912 | 1,167 |
| 2025E | 1,408 | 0.832 | 1,172 |
| 2026E | 1,549 | 0.759 | 1,176 |
| 2027E | 1,704 | 0.693 | 1,181 |
| 2028E | 1,874 | 0.632 | 1,185 |
| **Sum PV** | | | **5,881** |

**Step 5: Terminal Value**
| Method | Value |
|--------|-------|
| Terminal FCFF (2029) | $1,931M |
| Terminal Growth | 3% |
| Terminal Value | $29,393M |
| PV of TV | $18,569M |

**Step 6: Enterprise Value**
| Component | Value |
|-----------|-------|
| PV of FCFF | $5,881M |
| PV of TV | $18,569M |
| Enterprise Value | $24,450M |
| Less: Net Debt | ($2,000M) |
| Equity Value | $22,450M |
| Shares Outstanding | 500M |
| **Implied Share Price** | **$44.90** |

---

## Sources

- CFA Institute - "Discounted Cash Flow Valuation"
- Investopedia - "Equity Valuation Methods"
- Corporate Finance Institute - "Valuation Fundamentals"
- McKinsey & Company - "Valuation"

---

## Notes

*Add your own analysis and observations*
