# Banking - Valuation Methods

Comprehensive guide to valuing financial institutions and banks.

---

## 1. Discounted Cash Flow (DCF) for Banks

### Overview
DCF values a bank by discounting projected future cash flows to present value. For banks, we use **Free Cash Flow to Equity (FCFE)** since banks have unique capital structures.

### Formula
```
FCFE = Net Income + Depreciation - Capital Expenditures - Change in Working Capital + Net Borrowing

Intrinsic Value = Σ (FCFE_t / (1 + r)^t)
```
Where:
- r = Cost of Equity (derived from CAPM)
- t = time period

### Key Differences from Corporate DCF
- Banks have minimal CAPEX
- Working capital is different (deposits, loans)
- Regulatory capital requirements matter

### Example Calculation
| Year | Net Income | Depreciation | CapEx | Change NW | FCFE |
|------|-----------|--------------|-------|-----------|------|
| 1 | 100 | 20 | (10) | (5) | 105 |
| 2 | 110 | 22 | (12) | (5) | 115 |
| 3 | 120 | 24 | (14) | (5) | 125 |

---

## 2. Dividend Discount Model (DDM)

### Overview
Banks typically pay consistent dividends. DDM values a bank based on expected future dividend payments.

### Gordon Growth Model (Single Stage)
```
P_0 = D_1 / (r - g)

Where:
P_0 = Current stock price
D_1 = Expected dividend next year
r = Required rate of return (cost of equity)
g = Dividend growth rate
```

### Two-Stage DDM
```
P_0 = Σ (D_0 × (1+g_s)^t / (1+r)^t) + (D_n × (1+g_L)) / ((r - g_L) × (1+r)^n)

Where:
g_s = Short-term growth rate (high)
g_L = Long-term sustainable growth rate
n = Number of years in high-growth phase
```

### When to Use DDM
- Banks with stable, predictable dividends
- Mature banking sector
- Focus on income investors

---

## 3. Relative Valuation (Comps)

### Key Multiples for Banks

| Multiple | Formula | Typical Range |
|----------|---------|---------------|
| Price-to-Earnings (P/E) | Share Price / EPS | 8-15x |
| Price-to-Book (P/B) | Share Price / Book Value per Share | 0.8-2.0x |
| Price-to-Tangible Book | Price / Tangible Book | 1.0-2.5x |
| Dividend Yield | Annual Dividend / Price | 2-5% |

### Example Comps Table
| Bank | Ticker | P/E | P/B | ROE | Dividend Yield |
|------|--------|-----|-----|-----|----------------|
| JPMorgan | JPM | 10.5x | 1.4x | 15% | 2.5% |
| Bank of America | BAC | 9.2x | 1.1x | 12% | 2.8% |
| Wells Fargo | WFC | 11.0x | 1.2x | 10% | 3.2% |

---

## 4. Residual Income Valuation

### Overview
Values a bank based on residual earnings (profits above the required return on book value).

### Formula
```
Residual Income = Net Income - (Equity × Cost of Equity)

Intrinsic Value = Book Value + Σ (Residual Income_t / (1+r)^t)
```

### Example
- Book Value per Share: $25
- Cost of Equity: 10%
- Expected ROE: 12%
- Net Income per Share: $3.00

Residual Income = $3.00 - ($25 × 10%) = $3.00 - $2.50 = $0.50

---

## 5. Key Metrics for Bank Valuation

### Profitability Metrics
- **ROE (Return on Equity)**: Net Income / Shareholder's Equity
- **ROA (Return on Assets)**: Net Income / Total Assets
- **Net Interest Margin (NIM)**: (Interest Income - Interest Expense) / Interest-Earning Assets

### Asset Quality
- **Non-Performing Loan (NPL) Ratio**: NPLs / Total Loans
- **Loan Loss Reserve Ratio**: Reserve / Total Loans

### Capital Adequacy
- **CET1 Ratio**: Common Equity Tier 1 / Risk-Weighted Assets
- **Tier 1 Capital Ratio**: Tier 1 Capital / Risk-Weighted Assets
- **Capital Adequacy Ratio (CAR)**: Total Capital / Risk-Weighted Assets

---

## 6. Step-by-Step Bank Valuation Example

### Example: Regional Bank XYZ

**Step 1: Gather Financial Data**
- Current Stock Price: $45
- Book Value per Share: $30
- EPS: $4.50
- Dividend per Share: $2.00
- Net Income: $450M
- Total Equity: $3,000M

**Step 2: Calculate Key Metrics**
- P/E = $45 / $4.50 = 10.0x
- P/B = $45 / $30 = 1.5x
- Dividend Yield = $2.00 / $45 = 4.4%
- ROE = $450M / $3,000M = 15%

**Step 3: Apply Valuation Methods**
| Method | Intrinsic Value | vs Current Price |
|--------|-----------------|------------------|
| DDM (g=3%, r=10%) | $48.57 | +8% |
| P/B (1.3x) | $39.00 | -13% |
| P/E (11x) | $49.50 | +10% |

---

## Sources

- CFA Institute - "Discounted Dividend Valuation"
- Investopedia - "How to Value a Bank Stock"
- Corporate Finance Institute - "Bank Valuation Methods"
- McKinsey & Company - "Valuing Financial Institutions"

---

## Notes

*Add your own observations and analysis here*
