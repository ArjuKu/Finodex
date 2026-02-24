# Banking - Pricing Models

Essential pricing models used in banking for loans, deposits, and interest rate products.

---

## 1. Net Interest Margin (NIM)

### Definition
NIM measures the difference between interest income generated and interest paid to lenders, relative to the amount of interest-earning assets.

### Formula
```
NIM = (Interest Income - Interest Expense) / Interest-Earning Assets

Or equivalently:
NIM = (Net Interest Income) / Interest-Earning Assets
```

### Example Calculation
| Component | Value |
|-----------|-------|
| Interest Income | $500M |
| Interest Expense | $250M |
| Net Interest Income | $250M |
| Interest-Earning Assets | $10,000M |
| **NIM** | **2.50%** |

### Benchmark NIM Ranges
- **Traditional Banks**: 2.5% - 4.0%
- **Investment Banks**: 1.0% - 2.0%
- **Credit Unions**: 3.0% - 5.0%

### Components of NIM
1. **Interest Rate Spread**: Difference between lending and borrowing rates
2. **Volume Effect**: Impact of asset/liability quantities
3. **Mix Effect**: Composition of earning assets

---

## 2. Loan Pricing Model

### Cost-Plus Pricing
```
Loan Rate = Cost of Funds + Operating Costs + Risk Premium + Target Spread
```

| Component | Typical Range |
|-----------|---------------|
| Cost of Funds | 2.0% - 4.0% |
| Operating Costs | 1.5% - 3.0% |
| Risk Premium (Credit Risk) | 1.0% - 5.0% |
| Target Spread | 0.5% - 2.0% |

### Market-Based Pricing
```
Loan Rate = Base Rate (Prime/SOFR) + Credit Spread
```

### Pricing Example
| Component | Value |
|-----------|-------|
| Base Rate (SOFR) | 5.30% |
| Credit Spread (AAA) | 0.50% |
| Loan Rate | **5.80%** |

| Component | Value |
|-----------|-------|
| Base Rate (SOFR) | 5.30% |
| Credit Spread (BBB) | 2% |
| Loan Rate | **7.50.80%** |

---

## 3. Risk-Based### Overview
Pricing loans Pricing

 based on the borrower's credit risk profile.

### Risk Matrix
| Credit Score | Risk Grade | Spread Addition |
|--------------|------------|------------------|
| 750+ | Prime | +0.00% |
| 700-749 | Near Prime | +0.50% |
| 650-699 | Subprime | +1.50% |
| 600-649 | Deep Subprime | +3.00% |
| <600 | High Risk | +5.00%+ |

### Expected Loss Model
```
Expected Loss = Probability of Default (PD) × Exposure at Default (EAD) × Loss Given Default (LGD)

Pricing Adjustment = Expected Loss + Risk Premium
```

### Example
| Parameter | Value |
|-----------|-------|
| PD | 2.0% |
| EAD | $1,000,000 |
| LGD | 40% |
| Expected Loss | $8,000 |
| Required Risk Premium | **0.80%** |

---

## 4. Deposit Pricing

### Types of Deposits & Typical Rates
| Deposit Type | Typical Rate Range |
|--------------|-------------------|
| Checking Accounts | 0.01% - 0.10% |
| Savings Accounts | 0.10% - 2.00% |
| Money Market | 0.50% - 3.00% |
| CDs (1-Year) | 3.00% - 5.00% |
| CDs (5-Year) | 3.50% - 5.50% |

### Deposit Beta
Measures how much of rate changes are passed through to depositors.
```
Deposit Beta = % Change in Deposit Rates / % Change in Market Rates

Typical Range: 0.20 - 0.60
```

---

## 5. Funds Transfer Pricing (FTP)

### Definition
FTP allocates interest income/expense to business units based on asset/liability maturities.

### FTP Rate Calculation
```
FTP Rate = Market Rate + Liquidity Premium + Option Cost
```

### Example - Loan FTP
| Component | Rate |
|-----------|------|
| Market Rate (SOFR) | 5.30% |
| Liquidity Premium | 0.20% |
| FTP Rate | **5.50%** |

### FTP for Deposit
| Component | Rate |
|-----------|------|
| Market Rate (SOFR) | 5.30% |
| Liquidity Premium | -0.30% (benefit) |
| FTP Rate | **5.00%** |

---

## 6. Basel Framework & Capital Pricing

### Capital Requirements
| Ratio | Requirement | Purpose |
|-------|-------------|---------|
| CET1 | 4.5% minimum | Core equity |
| Capital Conservation Buffer | 2.5% | Systemic risk |
| Countercyclical Buffer | 0-2.5% | Economic cycle |
| **Total CET1** | **7.0% - 10.5%** | |

### Risk-Weighted Assets (RWA)
```
RWA = Σ (Assets × Risk Weight)

Risk Weights:
- Government Bonds: 0%
- Residential Mortgage: 50%
- Corporate Loans: 100%
- Consumer Loans: 100%
```

### Pricing for Capital
```
Required Return on Capital = Risk-Free Rate + (Beta × Market Risk Premium) + Capital Cost

Where Capital Cost accounts for regulatory capital requirements
```

---

## 7. Interest Rate Risk in Banking Book (IRRBB)

### Duration Gap Analysis
```
Duration Gap = Duration of Assets - (Assets/Equity) × Duration of Liabilities

Economic Value Change = -Duration Gap × ΔInterest Rate × Assets
```

### Interest Rate Sensitivity
| Rate Scenario | Impact on NIM | Impact on Value |
|---------------|---------------|------------------|
| Rates +100 bps | +15-25% | -5-10% |
| Rates -100 bps | -15-25% | +5-10% |

---

## 8. Pricing Model Example - Commercial Loan

### Input Parameters
| Parameter | Value |
|-----------|-------|
| Loan Amount | $10,000,000 |
| Maturity | 5 years |
| Credit Rating | BBB |
| PD (1-year) | 0.5% |
| LGD | 40% |
| Cost of Funds | 5.00% |
| Operating Cost | 0.75% |
| Target ROE | 12% |
| Tax Rate | 21% |

### Pricing Calculation
| Component | Calculation | Rate |
|-----------|-------------|------|
| Cost of Funds | | 5.00% |
| Operating Costs | | 0.75% |
| Credit Costs | 0.5% × 40% × 5 | 1.00% |
| Target ROE | 12% × (1-21%) | 9.48% |
| **All-in Rate** | | **16.23%** |

### Alternative: Market Pricing
| Component | Rate |
|-----------|------|
| 5-Year Treasury | 4.50% |
| BBB Spread | 2.25% |
| **Market Rate** | **6.75%** |

---

## Sources

- McKinsey & Company - "Banking on Interest Rates"
- Investopedia - "Net Interest Margin"
- BIS - "Principles for Effective Risk Data Aggregation"
- CFA Institute - "Financial Markets and Institutions"

---

## Notes

*Add your own pricing models and observations*
