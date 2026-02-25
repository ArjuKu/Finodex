# How to Value a Company Using DCF

## What is DCF?

**Discounted Cash Flow (DCF)** is a valuation method that estimates the value of an investment based on its expected future cash flows, adjusted for the time value of money.

**Key Principle:** A dollar today is worth more than a dollar tomorrow because you could invest today's dollar and earn returns.

---

## The DCF Formula

```
Value = Σ (Cash Flow / (1 + Discount Rate)^t) + Terminal Value
```

Where:
- `Cash Flow` = Money the company generates each year
- `Discount Rate` = The return you require (usually WACC)
- `t` = Year number (1, 2, 3, etc.)
- `Terminal Value` = Value after the forecast period

---

## Step-by-Step Process

### Step 1: Forecast Revenue & Expenses

**Revenue Forecasting Methods:**

| Method | How It Works | Best For |
|--------|--------------|----------|
| **Growth Rate** | Revenue × (1 + growth %) | Simple, stable companies |
| **Unit × Price** | Units sold × Price per unit | Physical goods |
| **Market Share** | Total market × Share % | Consumer products |

**Example - Growth Rate Method:**
```
Year 1 Revenue = $10,000M × 1.10 = $11,000M
Year 2 Revenue = $11,000M × 1.10 = $12,100M
```

### Step 2: Calculate EBITDA

```
EBITDA = Revenue - Operating Expenses (excluding D&A)
```

EBITDA measures operating profitability before accounting decisions.

### Step 3: Calculate EBIT

```
EBIT = EBITDA - Depreciation & Amortization
```

### Step 4: Calculate NOPAT (Net Operating Profit After Tax)

```
NOPAT = EBIT × (1 - Tax Rate)
```

This is the true operating cash flow after taxes.

### Step 5: Calculate Free Cash Flow (FCF)

```
FCF = NOPAT + D&A - in Working Capital
```

Where:
- CapEx - Change **D&A** is added back (non-cash expense)
- **CapEx** is capital expenditure (cash outflow)
- **Change in NWC** is additional working capital needed

### Step 6: Discount to Present Value

```
PV of FCF = FCF / (1 + WACC)^year
```

**What is WACC?** See the WACC guide in this folder.

### Step 7: Calculate Terminal Value

Two methods:

**Method A: Gordon Growth (Perpetuity Growth)**
```
Terminal Value = Final Year FCF × (1 + g) / (WACC - g)

Where g = Terminal growth rate (typically 2-3%)
```

**Method B: Exit Multiple**
```
Terminal Value = Final Year EBITDA × Industry Multiple
```

### Step 8: Sum Everything Up

```
Enterprise Value = PV of Forecast FCFs + PV of Terminal Value
```

---

## How to Get the Numbers

### From Financial Statements:

| Item | Where to Find |
|------|---------------|
| Revenue | Income Statement |
| Operating Expenses | Income Statement |
| D&A | Cash Flow Statement |
| CapEx | Cash Flow Statement |
| Change in NWC | Balance Sheet |
| Tax Rate | Income Statement (effective rate) |

### How to Forecast:

**Revenue:**
- Look at historical growth (CAGR)
- Consider industry growth rates
- Check analyst estimates
- Factor in new products/market expansion

**Margins:**
- Assume margins stay constant (simple)
- Assume margins improve (efficiency gains)
- Assume margins decline (competition)

**CapEx:**
- As % of revenue (historical average)
- Maintenance CapEx vs. growth CapEx

---

## Example: Complete DCF Calculation

### Input Assumptions:
- Current Revenue: $10,000M
- Growth Rate: 10%
- EBITDA Margin: 22%
- D&A: 5% of revenue
- CapEx: 6% of revenue
- NWC: 2% of revenue change
- Tax Rate: 21%
- WACC: 9.6%
- Terminal Growth: 3%

### Year 1 Calculation:
```
Revenue = $10,000 × 1.10 = $11,000M
EBITDA = $11,000 × 22% = $2,420M
D&A = $11,000 × 5% = $550M
EBIT = $2,420 - $550 = $1,870M
Tax = $1,870 × 21% = $393M
NOPAT = $1,870 - $393 = $1,477M

FCFE = $1,477 + $550 - $660 - $220 = $1,147M
PV = $1,147 / 1.096 = $1,046M
```

### Terminal Value:
```
Final FCF (Year 5) = $1,874M
Terminal Value = $1,874 × 1.03 / (0.096 - 0.03) = $29,393M
PV of Terminal = $29,393 × 0.632 = $18,569M
```

### Final Valuation:
```
Sum of PV (Years 1-5) = $5,881M
+ PV of Terminal = $18,569M
= Enterprise Value = $24,450M
```

---

## Interpreting Results

### Compare to Current Price:
```
Upside = (Implied Price - Current Price) / Current Price
```

- **Positive upside** = Stock may be undervalued
- **Negative upside** = Stock may be overvalued

### Sensitivity Analysis:
Always test different assumptions:
- WACC: 8% to 12%
- Terminal Growth: 2% to 4%
- Revenue Growth: Base ± 2%

---

## When to Use DCF

✅ **Best for:**
- Companies with predictable cash flows
- Stable, mature businesses
- Asset-heavy companies

❌ **Not ideal for:**
- Startups with no cash flows
- Financial institutions (different structure)
- Commodities/cyclicals (cash flows volatile)

---

## Common Mistakes to Avoid

1. **Using too high terminal growth** - Can't grow faster than GDP forever (use 2-3%)
2. **Ignoring working capital** - Must fund growth in receivables/inventory
3. **Using wrong discount rate** - WACC varies by industry
4. **Double counting** - Don't add back D&A if already accounted for
5. **Forgetting terminal value** - Often 50%+ of value

---

## Sources

- CFA Institute - "Discounted Cash Flow Valuation"
- Corporate Finance Institute
- McKinsey & Company - "Valuation"

---

## Related Models in This Folder

- `equity_dcf_model.py` - Python implementation
- See `../pricing-models/` for WACC calculation guide

## Excel Templates

For professional Excel templates, we recommend:
- [Damodaran's Valuation Spreadsheets](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/spreadsh.htm)
- [Corporate Finance Institute Templates](https://corporatefinanceinstitute.com/resources/templates/excel-modeling/)
