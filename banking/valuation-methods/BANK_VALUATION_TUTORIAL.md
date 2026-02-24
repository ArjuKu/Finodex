# How to Value a Bank

## Why Bank Valuation is Different

Banks have unique characteristics that make traditional valuation tricky:

1. **Capital Structure:** Banks are highly leveraged (lots of debt is normal)
2. **Cash Flows:** Interest income/expense dominate
3. **Regulation:** Capital requirements affect operations
4. **Risk:** Credit risk is core to the business

---

## Key Metrics for Banks

### 1. Net Interest Margin (NIM)

The profit banks make on the spread between what they pay for money and what they earn.

```
NIM = (Interest Income - Interest Expense) / Interest-Earning Assets

Example:
Interest Income = $500M
Interest Expense = $250M
Earning Assets = $10,000M
NIM = ($500M - $250M) / $10,000M = 2.5%
```

### 2. Return on Equity (ROE)

```
ROE = Net Income / Shareholder's Equity

Example:
Net Income = $1,000M
Equity = $10,000M
ROE = 10%
```

### 3. Efficiency Ratio

```
Efficiency Ratio = Operating Expenses / Total Revenue

Lower is better (means more efficient)
Typical: 50-70%
```

### 4. Non-Performing Loan (NPL) Ratio

```
NPL Ratio = Non-Performing Loans / Total Loans

Lower is better
Typical: 0.5-2%
```

---

## Bank Valuation Methods

### Method 1: Dividend Discount Model (DDM)

Banks typically pay consistent dividends, making DDM useful.

**Formula:**
```
P0 = D1 / (r - g)

Where:
D1 = Expected dividend next year
r = Required return (cost of equity)
g = Dividend growth rate
```

**Two-Stage DDM (better for banks):**
```
P0 = Σ (D0 × (1+g_high)^t / (1+r)^t) + Dn × (1+g_low) / ((r - g_low) × (1+r)^n)
```

**Example:**
- Current dividend = $2.00
- High growth (5 years) = 8%
- Stable growth = 3%
- Required return = 10%

### Method 2: Discounted Cash Flow (FCFE)

For banks, we use **Free Cash Flow to Equity** instead of FCFF.

**FCFE for Banks:**
```
FCFE = Net Income - Net Borrowing + Changes in Regulatory Capital
```

Simpler version:
```
FCFE = Net Income - Change in Equity (required for growth)
```

**Valuation:**
```
Value = Σ FCFEt / (1 + r)^t + Terminal Value
```

### Method 3: Price-to-Book (P/B)

Common for banks since book value is reliable.

```
P/B = Share Price / Book Value per Share

Typical range: 0.8x - 2.0x
```

**Adjusted P/B (Tangible):**
```
P/TB = Share Price / Tangible Book Value per Share

Excludes goodwill and intangibles
```

### Method 4: Price-to-Earnings (P/E)

```
P/E = Share Price / EPS

Typical range: 8x - 15x
```

---

## Bank-Specific DCF Process

### Step 1: Forecast Net Interest Income

```
Net Interest Income = Earning Assets × NIM
```

Forecast by:
- Growing earning assets
- Projecting NIM (consider rate environment)

### Step 2: Forecast Non-Interest Income

- Fees, trading, etc.
- Typically as % of total revenue

### Step 3: Forecast Operating Expenses

- Efficiency ratio approach: Expenses = Revenue × Efficiency Ratio

### Step 4: Calculate Provision for Credit Losses

```
Provisions = Total Loans × Expected Loss Rate
```

### Step 5: Calculate Net Income

```
Pre-Tax Income = NII + Non-NII - OpEx - Provisions
Tax = Pre-Tax × Tax Rate
Net Income = Pre-Tax - Tax
```

### Step 6: Calculate FCFE

```
FCFE = Net Income - (Required Capital to Maintain ROE)
```

### Step 7: Discount at Cost of Equity

Use CAPM to get required return:

```
Re = Rf + β × MRP
```

For banks:
- Rf: 4-5% (10-year Treasury)
- Beta: Typically 1.0-1.3
- MRP: 5-7%

---

## Key Assumptions for Bank DCF

### Growth Rates:
| Item | Typical Range |
|------|---------------|
| Loan Growth | 3-8% |
| Deposit Growth | 3-7% |
| NIM | 2.0-3.5% |

### Key Ratios:
| Ratio | Good | Bad |
|-------|------|-----|
| ROE | >12% | <8% |
| NIM | >2.5% | <1.5% |
| Efficiency | <55% | >70% |
| CET1 Ratio | >12% | <8% |

---

## Example: Bank DCF

### Input Assumptions:
- Current EPS: $4.50
- Dividend: $2.00
- Book Value: $30
- ROE: 15%
- Cost of Equity: 11%
- Terminal Growth: 3%

### Valuation:

**DDM (Gordon Growth):**
```
P0 = $2.00 × 1.03 / (0.11 - 0.03) = $25.75
```

**P/B (1.3x):**
```
P = $30 × 1.3 = $39
```

**P/E (12x):**
```
P = $4.50 × 12 = $54
```

---

## Regulatory Capital Impact

### Basel Requirements:
- CET1: 4.5% minimum + buffer
- Tier 1: 6%
- Total Capital: 8%

### Impact on Valuation:
- Higher capital requirements = less growth potential
- Higher capital = lower risk = higher valuation
- Must maintain ratios or face restrictions

---

## Sources

- CFA Institute - "Financial Institutions"
- McKinsey - "Bank Valuation"
- Damodaran - "Bank Valuation"

---

## Related Files

- `bank_dcf_model.csv` - Excel DCF template
- `bank_ddm_model.py` - Python DDM model
- `nim_calculator.csv` - NIM calculator
- `bank_comps_data.csv` - Bank comparable data
