# Commodities - Pricing Models

Core models for understanding commodity price formation and forwards/futures.

---

## 1. Spot Price vs. Forward Price

### Definitions
| Term | Definition |
|------|------------|
| **Spot Price** | Current market price for immediate delivery |
| **Forward Price** | Price agreed today for future delivery |
| **Future Price** | Exchange-traded forward price |

### Key Relationship
```
Forward Price = Spot Price × e^(r×t)

Where:
r = Risk-free interest rate
t = Time to delivery
```

### Example - Oil Forward
| Input | Value |
|-------|-------|
| Spot Price | $75/bbl |
| Risk-Free Rate | 4.5% |
| Time to Delivery | 1 year |
| **Forward Price** | **$78.47** |

---

## 2. Cost of Carry Model

### Formula
```
F = S × e^((r + u - y) × t)

Where:
F = Forward/Futures price
S = Spot price
r = Risk-free rate
u = Storage cost (as %)
y = Convenience yield
t = Time to maturity
```

### Components
| Component | Description | Typical Impact |
|-----------|-------------|----------------|
| **Storage Cost** | Cost to hold physical commodity | Increases forward |
| **Convenience Yield** | Benefit of physical ownership | Decreases forward |
| **Financing Cost** | Cost of capital | Increases forward |
| **Dividend Yield** | For financial commodities | Decreases forward |

### Example - Gold
| Component | Value |
|-----------|-------|
| Spot Price | $2,000/oz |
| Storage Cost | 1% |
| Convenience Yield | 0.5% |
| Risk-Free Rate | 4.5% |
| Time | 1 year |
| Net Carry Cost | 4.5 + 1 - 0.5 = 5% |
| **Forward Price** | **$2,105** |

---

## 3. Contango vs. Backwardation

### Definitions
| Term | Definition | Visual |
|------|------------|--------|
| **Contango** | Futures prices > spot (upward curve) | / |
| **Backwardation** | Futures prices < spot (downward curve) | \ |

### When Each Occurs
| Market Condition | Contango | Backwardation |
|-----------------|----------|---------------|
| Supply surplus | ✓ | |
| High storage costs | ✓ | |
| Supply shortage | | ✓ |
| Convenience yield high | | ✓ |

### Impact on Hedging
| Scenario | Effect |
|----------|--------|
| Contango (normal) | Roll cost reduces returns |
| Backwardation | Roll yield enhances returns |

---

## 4. Basis Risk

### Definition
The risk that the spot price and futures price don't move together perfectly.

### Formula
```
Basis = Spot Price - Futures Price

Basis Risk = Variation in Basis
```

### Example
| Date | Spot Price | Futures Price | Basis |
|------|------------|---------------|-------|
| Jan 1 | $75.00 | $78.00 | -$3.00 |
| Mar 1 | $72.00 | $73.50 | -$1.50 |
| Mar 31 | $70.00 | $70.00 | $0.00 |

---

## 5. Futures Pricing Examples by Commodity

### Crude Oil (WTI)
| Maturity | Price | vs Spot |
|----------|-------|---------|
| Spot | $75.00 | - |
| 1-Month | $75.25 | +0.3% |
| 3-Month | $76.00 | +1.3% |
| 6-Month | $77.50 | +3.3% |
| 12-Month | $80.00 | +6.7% |

### Natural Gas
| Maturity | Price | vs Spot |
|----------|-------|---------|
| Spot | $3.50 | - |
| 1-Month | $3.45 | -1.4% |
| 3-Month | $3.30 | -5.7% |
| 6-Month | $3.15 | -10% |
| 12-Month | $3.00 | -14% |

### Gold
| Maturity | Price | vs Spot |
|----------|-------|---------|
| Spot | $2,000 | - |
| 1-Month | $2,002 | +0.1% |
| 3-Month | $2,008 | +0.4% |
| 6-Month | $2,020 | +1.0% |
| 12-Month | $2,045 | +2.3% |

---

## 6. Options on Commodities

### Types
| Option | Description |
|--------|-------------|
| **Call** | Right to buy at strike |
| **Put** | Right to sell at strike |
| **Collar** | Long call + short put |
| **Spread** | Buy one, sell another |

### Commodity Option Pricing
Uses similar models to equity options:
- Black-Scholes (for forwards)
- Black 76 (for futures)
- Binomial trees

### Greeks for Commodities
| Greek | Definition | Special Considerations |
|-------|------------|----------------------|
| Delta | Option price change vs underlying | Volatility surface |
| Gamma | Delta change rate | Roll costs |
| Vega | Volatility sensitivity | Term structure |
| Theta | Time decay | Storage costs |
| Rho | Interest rate sensitivity | Cost of carry |

---

## 7. Calendar Spreads

### Definition
Trading the price difference between two different delivery months.

### Formula
```
Spread = Near-month Price - Far-month Price
```

### Uses
- Hedging
- Speculation on shape
- Arbitrage

### Example - Crude Oil
| Spread | Value | Interpretation |
|--------|-------|----------------|
| Mar-Apr | +$0.50 | Slightly in contango |
| Mar-Dec | +$5.00 | Strong contango |

### Roll Yield
```
Roll Yield = (Near Price - Far Price) / Near Price

Positive = Contango (negative roll yield)
Negative = Backwardation (positive roll yield)
```

---

## 8. Convenience Yield

### Definition
The benefit or premium associated with physically holding the commodity.

### Factors
- Scarcity
- Supply disruptions
- Production needs
- Storage availability

### Calculation (from Forward/Spot)
```
y = r - ln(F/S) / t

Where:
y = Convenience yield
r = Risk-free rate
F = Forward price
S = Spot price
t = Time
```

### Example
| Parameter | Value |
|-----------|-------|
| Spot Price | $80 |
| Forward (1yr) | $85 |
| Risk-Free Rate | 4.5% |
| Convenience Yield | 4.5% - ln(85/80) = **1.2%** |

---

## 9. Basis and Hedging

### Hedging Example
A producer wants to lock in price for oil to be produced in 6 months.

| Action | Result |
|--------|--------|
| Sell Futures | Locks forward price |
| If spot rises | Futures loss offsets spot gain |
| If spot falls | Futures gain offsets spot loss |

### Hedge Effectiveness
```
Hedge Effectiveness = (Correlation)^2

High correlation = Effective hedge
Low correlation = Basis risk
```

---

## 10. Price Drivers by Commodity Sector

### Energy
| Commodity | Key Price Drivers |
|-----------|------------------|
| Oil | OPEC, inventories, geopolitics, demand |
| Natural Gas | Weather, storage, LNG exports |
| Coal | China/India demand, regulations |
| Power | Generation mix, demand, transmission |

### Metals
| Commodity | Key Price Drivers |
|-----------|------------------|
| Gold | Real rates, USD, inflation, safe haven |
| Silver | Gold correlation, industrial demand |
| Copper | China construction, EV demand |
| Iron Ore | Chinese steel production |

### Agriculture
| Commodity | Key Price Drivers |
|-----------|------------------|
| Wheat | Weather, exports, inventories |
| Corn | Ethanol demand, weather, exports |
| Soybeans | China demand, weather |
| Coffee | Brazil weather, Brazil supply |

---

## Sources

- CFA Institute - "Derivatives and Commodity Investments"
- Investopedia - "Contango and Backwardation"
- CME Group - "Understanding Commodity Futures"
- EIA - "Energy Information Administration"

---

## Notes

*Add your own calculations and observations*
