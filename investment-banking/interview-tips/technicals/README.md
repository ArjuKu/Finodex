# Banking Technical Interview Questions

*Curated from Wall Street Prep, Mergers & Inquisitions, and industry sources*

---

## 1. Walk Me Through a DCF

**Asked at:** Almost every banking interview

### The Answer Structure:

1. **Start with unlevered free cash flow (FCFF)**
   > "I project a company's free cash flow to the firm, which is cash available to all capital providers."

2. **Forecast period (typically 5 years)**
   > "I forecast revenues based on growth assumptions, then project EBITDA, subtract D&A to get EBIT, apply taxes to get NOPAT, then add back D&A and subtract CapEx and changes in working capital."

3. **WACC as discount rate**
   > "I discount using the weighted average cost of capital, which weighs the cost of equity and cost of debt."

4. **Terminal value**
   > "For terminal value, I use the Gordon Growth model, assuming a 2-3% perpetual growth rate, or an exit multiple."

5. **Enterprise to equity value**
   > "I sum the PV of cash flows and terminal value to get enterprise value, then add back cash and subtract debt to get equity value."

---

## 2. What is WACC and How Do You Calculate It?

**Formula:**
```
WACC = (E/V × Re) + (D/V × Rd × (1-T))
```

**Where:**
- E = Market value of equity
- D = Market value of debt
- V = E + D
- Re = Cost of equity (CAPM: Rf + β × MRP)
- Rd = Cost of debt
- T = Tax rate

**Example:**
> "If a company is 70% equity and 30% debt, with a 10% cost of equity, 5% cost of debt, and 25% tax rate, WACC = (0.7 × 10%) + (0.3 × 5% × (1-0.25)) = 7% + 1.125% = 8.125%"

---

## 3. How Do You Value a Bank?

**Key difference from regular companies:**
> "Banks have different capital structures and cash flows. Traditional DCF doesn't work well because interest income/expense dominates and regulatory capital requirements are different."

**Methods for banks:**
1. **Dividend Discount Model (DDM)**
   > "Banks pay consistent dividends, so DDM is common. P0 = D1 / (r - g)"

2. **Price-to-Book (P/B)**
   > "Banks trade on book value. Typical range is 0.8x - 2.0x."

3. **Price-to-Earnings (P/E)**
   > "Similar to other sectors, typically 8x - 15x."

4. **Sum-of-Parts**
   > "For diversified banks, value each business separately."

---

## 4. What is Net Interest Margin (NIM)?

**Formula:**
```
NIM = (Interest Income - Interest Expense) / Interest-Earning Assets
```

**Example:**
> "If a bank earns $500M in interest income, pays $250M in interest expense, and has $10B in earning assets, NIM = ($500M - $250M) / $10B = 2.5%"

---

## 5. Walk Me Through the Three Financial Statements

### Income Statement:
```
Revenue
- COGS
= Gross Profit
- Operating Expenses
= EBIT
- Interest Expense
= EBT
- Taxes
= Net Income
```

### Balance Sheet:
```
Assets = Liabilities + Equity
- Current Assets (Cash, AR, Inventory)
- Fixed Assets (PP&E)
    = Total Assets

- Current Liabilities (AP, Short-term Debt)
- Long-term Debt
    = Total Liabilities
+ Common Stock + Retained Earnings
    = Total Equity
```

### Cash Flow Statement:
```
Net Income
+ Non-cash items (D&A)
- Changes in Working Capital
= Cash from Operations
- CapEx
= Free Cash Flow
+ Financing activities
= Change in Cash
```

---

## 6. What Happens to EBITDA When Revenue Grows 10%?

> "If operating margins remain constant, EBITDA grows 10%. For example, if revenue is $100M with 20% EBITDA margin, and revenue grows to $110M, EBITDA grows to $22M (which is also 10% growth)."

**Key point:** Margins must stay constant for proportional growth.

---

## 7. What is the Difference Between Enterprise Value and Equity Value?

**Enterprise Value (EV):**
- Value of the core business
- = Market Cap + Debt - Cash

**Equity Value:**
- Value available to shareholders
- = EV - Debt + Cash
- Or: Share Price × Shares Outstanding

---

## 8. What is a Levered vs. Unlevered Beta?

| Term | Definition |
|------|------------|
| **Unlevered Beta** | Business risk only (no debt) |
| **Levered Beta** | Business + financial risk |

**Formula:**
```
βL = βU × [1 + (1-T) × D/E]
```

> "A company with more debt has higher levered beta because of financial risk."

---

## 9. Walk Me Through an M&A Accretion/Dilution Analysis

### Steps:
1. **Calculate purchase price** = Target share price × shares outstanding
2. **Determine payment method** (cash vs. stock)
3. **Combine financials** = Buyer + Target
4. **Calculate new EPS** = Combined Net Income / Combined Shares
5. **Accretion/Dilution** = (New EPS / Buyer Old EPS) - 1

### Example:
> "If Buyer trades at 15x P/E and pays 10x P/E for Target, the deal is accretive because Buyer is paying less for Target's earnings than the market pays for Buyer's."

---

## 10. What is a Typical IRR for an LBO?

| Deal Type | IRR Range |
|-----------|-----------|
| Mega-cap LBO | 15-20% |
| Mid-market LBO | 20-25% |
| Distressed/turnaround | 25%+ |

**Key drivers:**
- Purchase price multiple
- Exit multiple
- Debt paydown rate
- EBITDA growth

---

## 📝 Your Turn - Add Technical Questions

*Contributors: Add real interview questions and answers here*

### [Your Name] - Question
> **Q:** [ADD QUESTION HERE]
>
> **A:** [ADD YOUR ANSWER HERE]

### Real Deal Example from [Name]
> **Q:** How would you value a bank with $10B assets, $500M equity, and 1.2% ROE?
>
> **A:** 
> [ADD ANSWER HERE]

---

## Sources

- Wall Street Prep - "The Red Book"
- Mergers & Inquisitions - "400 Questions"
- Breaking Into Wall Street
- iBankingFAQ

---

## Related

- [Interview Guide](./interview-guide/) - Behavioral questions
- [Downloads](./downloads/) - Print-friendly PDFs
