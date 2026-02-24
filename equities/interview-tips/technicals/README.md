# Equities Technical Interview Questions

*Curated from Wall Street Prep, CFI, and industry sources*

---

## 1. Walk Me Through a DCF

**Core Answer Structure:**

1. **Free Cash Flow to Firm (FCFF)**
   > "I project unlevered free cash flow, which is cash available to all capital providers."

2. **Forecast Period**
   > "I forecast 5 years of revenue growth, apply EBITDA margins, subtract D&A, interest, and taxes to get NOPAT, then add back D&A and subtract CapEx and working capital changes."

3. **Discount Rate (WACC)**
   > "I calculate WACC using the capital structure weights, cost of equity via CAPM, and after-tax cost of debt."

4. **Terminal Value**
   > "I use Gordon Growth (2-3% perpetual growth) or an exit multiple."

5. **Enterprise to Equity**
   > "Sum PV of cash flows + PV of terminal = Enterprise Value. Add cash, subtract debt = Equity Value."

---

## 2. What is WACC?

### Formula:
```
WACC = (E/V × Re) + (D/V × Rd × (1-T))
```

### CAPM (Cost of Equity):
```
Re = Rf + β × (Rm - Rf)
```

### Example:
> "For a company with 80% equity at 12% cost, 20% debt at 5% after-tax, WACC = (0.8 × 12%) + (0.2 × 5%) = 9.6% + 1% = 10.6%"

---

## 3. How Do You Calculate Cost of Equity (CAPM)?

### Components:
- **Rf**: Risk-free rate (10-year Treasury, ~4-5%)
- **β**: Beta (systematic risk)
- **(Rm - Rf)**: Market risk premium (~5-7%)

### Example:
> "If Rf = 4.5%, β = 1.2, and MRP = 6%, then Re = 4.5% + 1.2 × 6% = 11.7%"

---

## 4. What's the Difference Between EV and Equity Value?

| Metric | Formula | What It Represents |
|--------|---------|-------------------|
| **Enterprise Value** | Market Cap + Debt - Cash | Value of operations |
| **Equity Value** | EV - Debt + Cash | Value to shareholders |

> "EV is what it would cost to buy the entire business. Equity value is what shareholders would receive."

---

## 5. Walk Me Through Comps

### Steps:
1. **Select peers** - Similar business model, size, geography
2. **Gather metrics** - Revenue, EBITDA, EPS, book value
3. **Calculate multiples** - P/E, EV/EBITDA, P/B, etc.
4. **Apply to target** - Use median/mean multiples

### Key Multiples:
| Multiple | Formula | Best For |
|----------|---------|----------|
| P/E | Price / EPS | Growth companies |
| EV/EBITDA | EV / EBITDA | Capital-intensive |
| P/B | Price / Book | Financial institutions |
| EV/Revenue | EV / Revenue | Pre-profit |

---

## 6. What is a Levered vs Unlevered Free Cash Flow?

| FCF Type | Definition | Used For |
|----------|------------|----------|
| **Unlevered (FCFF)** | Cash available to all capital providers | Enterprise Value |
| **Levered (FCFE)** | Cash available to equity only | Equity Value |

### Formula:
```
FCFF = EBIT(1-T) + D&A - CapEx - ΔWC
FCFE = FCFF - Net Borrowing + (1-T) × Interest
```

---

## 7. What is Terminal Value and How Do You Calculate It?

### Method 1: Gordon Growth
```
TV = FCF_n × (1+g) / (WACC - g)

g = perpetual growth rate (typically 2-3%)
```

### Method 2: Exit Multiple
```
TV = EBITDA_n × Multiple
```

### Which to use:
- **Gordon Growth**: Steady, mature companies
- **Exit Multiple**: Cyclical companies, when market multiples are stable

---

## 8. What is Beta and How Do You Interpret It?

| Beta | Interpretation |
|------|----------------|
| 0 | No systematic risk |
| <1 | Less volatile than market |
| =1 | Same volatility as market |
| >1 | More volatile than market |

### Relevering Beta:
```
βL = βU × [1 + (1-T) × D/E]
```

---

## 9. What is the Difference Between P/E and EV/EBITDA?

### P/E:
- Includes interest
- Affected by capital structure
- Good for: Financial services, companies with little debt

### EV/EBITDA:
- Excludes interest
- Capital structure neutral
- Good for: Capital-intensive companies, comparables

---

## 10. What is a Good ROE and What Drives It?

### Formula:
```
ROE = Net Income / Shareholder's Equity
```

### DuPont Analysis:
```
ROE = (Net Margin) × (Asset Turnover) × (Financial Leverage)

ROE = NI/Revenue × Revenue/Assets × Assets/Equity
```

**Key drivers:**
- Profit margins
- Asset efficiency
- Debt usage

---

## 11. What Happens to NOPAT if Margins Change?

> "If EBITDA margins stay constant, NOPAT grows proportionally to revenue. If margins expand or compress, NOPAT changes by the margin change multiplied by revenue."

**Example:**
> "If revenue is $100M with 20% EBITDA margin, and margin expands to 25%, NOPAT increases by more than revenue growth."

---

## 12. What is the Time Value of Money?

> "A dollar today is worth more than a dollar in the future because you could invest that dollar and earn a return. This is why we discount future cash flows."

### Formula:
```
PV = FV / (1+r)^n
```

---

## 📝 Your Turn - Add Technical Questions

*Contributors: Add real interview questions and answers here*

### [Your Name] - Question
> **Q:** [ADD QUESTION]
>
> **A:** [ADD ANSWER]

---

## Sources

- Wall Street Prep
- Corporate Finance Institute
- Investopedia

---

## Related

- [Interview Guide](./interview-guide/) - Behavioral questions
- [Downloads](./downloads/) - Print-friendly PDFs
