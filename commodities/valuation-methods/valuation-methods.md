# Commodities - Valuation Methods

Comprehensive guide to valuing commodity assets and companies.

---

## 1. Commodity Companies Overview

### Types of Commodity Companies
| Type | Examples | Valuation Focus |
|------|----------|-----------------|
| Oil & Gas (E&P) | Exxon, Chevron | Reserves, production, FCF |
| Mining | BHP, Rio Tinto | Resources, grades, costs |
| Agriculture | Archer Daniels, Cargill | Land, crops, margins |
| Metals & Mining | Freeport, Newmont | Production, grades, AISC |

### Key Differences from Other Industries
- Commodity prices highly volatile
- Geopolitical risks significant
- Production costs critical
- Reserve valuation complex
- Regulatory/environmental costs

---

## 2. Net Asset Value (NAV) Valuation

### Overview
NAV values a commodity company based on the present value of its reserves and resources.

### Formula
```
NAV = Σ [Reserves × (Price - Cost) × Recovery Factor] / (1 + r)^t
```

### Steps for NAV Calculation
1. **Estimate Reserves**: Proven + Probable (2P)
2. **Forecast Production**: Based on reserves and decline curves
3. **Project Prices**: Long-term commodity price forecasts
4. **Estimate Costs**: Operating costs, CAPEX, decommissioning
5. **Discount Cash Flows**: Apply appropriate discount rate
6. **Add Other Assets**: Non-producing assets, cash

### Example - Oil Company NAV
| Component | Calculation | Value ($M) |
|-----------|------------|------------|
| Year 1-5 Production | 50M boe × $50/boe | 2,500 |
| Year 6-10 Production | 40M boe × $45/boe | 1,800 |
| Year 11-20 Production | 25M boe × $40/boe | 1, Value |000 |
| Terminal 10M boe × $35/175 | 200 |
| Total Undiscounted CF | | 5,500 |
| PV Factor (10%) | | 0.65 |
| **Net Present Value** | | **3,575** |

---

## 3. Resource-Based Valuation

### For Mining Companies
| Category | Description | Confidence |
|----------|-------------|------------|
| Measured | Highest confidence | 90% |
| Indicated | Good confidence | 50-90% |
| Inferred | Low confidence | 10-50% |

### Valuation Approaches
| Method | Formula | Best For |
|--------|---------|----------|
| EV/Resource | Value / oz or tonne | Early-stage |
| EV/Production | Value / annual output | Production stage |
| DCF | Discounted cash flows | All stages |

### Example - Gold Mining
| Metric | Company A | Company B |
|--------|-----------|----------|
| Gold Reserves (Moz) | 50 | 30 |
| Market Cap ($M) | $10,000 | $6,000 |
| EV/oz | $200 | $200 |
| Annual Production (Moz) | 2.0 | 1.5 |
| EV/Production | $5,000/oz | $4,000/oz |

---

## 4. Comparable Company Analysis (Comps)

### Key Multiples for Commodities
| Multiple | Formula | Use |
|----------|---------|-----|
| EV/2P Reserves | Enterprise Value / Proven+Probable | E&P Companies |
| EV/Production | Enterprise Value / Annual Output | All Commodity |
| EV/EBITDA | Enterprise Value / EBITDA | Cash Flow |
| P/NAV | Price / Net Asset Value | NAV-based |
| FCF Yield | FCF / Market Cap | Income Focus |

### Commodity Comps Example
| Company | EV/2P | EV/EBITDA | P/NAV | AISC |
|---------|-------|-----------|-------|------|
| Company A | $12/boe | 6x | 1.2x | $35/boe |
| Company B | $10/boe | 5x | 1.0x | $40/boe |
| Company C | $15/boe | 8x | 1.5x | $30/boe |
| **Median** | **$12/boe** | **6x** | **1.2x** | **$35/boe** |

---

## 5. Discounted Cash Flow (DCF)

### Special Considerations for Commodities
- **Price Forecasting**: Use long-term consensus prices
- **Cost Inflation**: Labor, materials, energy costs
- **Reserve Replacement**: Critical for sustainment
- **Decommissioning Costs**: End-of-life obligations
- **Geopolitical Risk**: Country risk premium

### DCF Steps
1. Forecast production profile
2. Project commodity prices
3. Estimate operating costs
4. Calculate CAPEX requirements
5. Determine working capital needs
6. Apply appropriate discount rate
7. Calculate terminal value

### Commodity Price Forecast Sources
| Source | Description |
|--------|-------------|
| EIA | US government energy forecasts |
| IEA | International Energy Agency |
| World Bank | Commodity price projections |
| Consensus Economics | Analyst consensus |
| Company Guidance | Management forecasts |

---

## 6. Cost Analysis

### Mining Cost Metrics
| Metric | Definition |
|--------|------------|
| C1 Cash Cost | Direct mining + transport |
| AISC | All-In Sustaining Cost |
| Total Cash Cost | C1 + royalties + taxes |
| All-In Cost | Total + exploration + admin |

### Oil & Gas Cost Metrics
| Metric | Definition |
|--------|------------|
| F&D Cost | Finding & Development |
| Operating Cost | LOE per barrel |
| CAPEX | Capital expenditure |
| Production Cost | All operating costs |

### Example - AISC Calculation
| Component | $/oz |
|-----------|------|
| Mining | $600 |
| Processing | $150 |
| Transport | $50 |
| Site Administration | $80 |
| By-product credits | ($50) |
| **C1 Cash Cost** | **$830** |
| Sustaining CAPEX | $120 |
| Exploration | $50 |
| **AISC** | **$1,000** |

---

## 7. Reserve Valuation

### Oil & Gas Classifications
| Category | Definition | Probability |
|----------|------------|------------|
| 1P (Proven) | Commercial certainty | 90% |
| 2P (Proven + Probable) | Economic certainty | 50% |
| 3P (Proven + Probable + Possible) | Low confidence | 10% |

### Reserve Life
```
Reserve Life = Reserves / Annual Production
```

### Example
| Metric | Value |
|--------|-------|
| 2P Reserves | 100 MMboe |
| Annual Production | 10 MMboe |
| Reserve Life | 10 years |

---

## 8. Real Options Valuation

### Overview
Commodity projects have option-like characteristics (delay, expand, abandon).

### Option Types
| Option | Description | Value Driver |
|--------|-------------|--------------|
| Delay | Wait for better prices | Volatility, time |
| Expand | Increase production | Price, demand |
| Abandon | Stop operations | Operating costs |
| Switch | Change inputs/outputs | Price spreads |

### When to Use
- High commodity price volatility
- Large capital commitments
- Long development timelines
- Significant uncertainty

---

## 9. Step-by-Step Example - Oil E&P Company

### Company: OilCo Inc.

**Step 1: Reserve Profile**
| Category | Reserves (MMboe) |
|----------|-----------------|
| Proven (1P) | 150 |
| Probable | 75 |
| **2P Total** | **225** |

**Step 2: Production Forecast**
| Year | Production (MMboe) | Decline |
|------|-------------------|---------|
| 1 | 20 | Base |
| 2 | 19 | 5% |
| 3 | 18 | 5% |
| 4 | 17 | 5% |
| 5 | 16 | 5% |

**Step 3: Price Assumptions**
| Year | Oil Price ($/bbl) |
|------|-------------------|
| 1-2 | $75 (current) |
| 3-5 | $70 (forward) |
| Terminal | $65 (long-term) |

**Step 4: Cash Flow Projection**
| Year | Revenue | OpEx | CAPEX | FCF |
|------|---------|------|-------|-----|
| 1 | $1,500 | $400 | $200 | $900 |
| 2 | $1,425 | $420 | $180 | $825 |
| 3 | $1,260 | $400 | $150 | $710 |
| 4 | $1,190 | $395 | $140 | $655 |
| 5 | $1,120 | $390 | $130 | $600 |

**Step 5: Valuation**
| Component | Value ($M) |
|-----------|------------|
| PV of FCF (Years 1-5) | $3,200 |
| Terminal Value | $2,500 |
| PV of Terminal | $1,500 |
| Enterprise Value | $4,700 |
| Less: Net Debt | ($800) |
| Equity Value | $3,900 |
| Shares Outstanding | 100M |
| **Implied Share Price** | **$39** |

---

## Sources

- CFA Institute - "Natural Resource Valuation"
- Corporate Finance Institute - "Commodity Valuation"
- USGS - Mineral Resources
- EIA - Energy Information Administration
- Mining.com

---

## Notes

*Add your own analysis and observations*
