# Commodity Forward Pricing Explained

## Spot vs. Forward Prices

### Spot Price
The current price for immediate delivery of a commodity.

**Example:**
- Oil spot price: $75/bbl (today)

### Forward/Futures Price
The price agreed today for delivery at a future date.

**Example:**
- Oil 1-year forward: $79/bbl (delivery in 1 year)

---

## The Cost of Carry Model

Forward prices are determined by the **cost of holding** the commodity:

```
F = S × e^((r + u - y) × t)

Where:
F = Forward price
S = Spot price
r = Risk-free interest rate (cost of financing)
u = Storage cost (as % of spot)
y = Convenience yield (benefit of holding physical)
t = Time to maturity (in years)
```

### Simple Version (no storage, no convenience yield):
```
F = S × e^(r × t)

Example:
S = $75
r = 4.5%
t = 1 year
F = 75 × e^(0.045 × 1) = $78.47
```

---

## Understanding Each Component

### 1. Risk-Free Rate (r)
The cost of borrowing money to buy and hold the commodity.

**Current rates:**
- ~4-5% for USD

### 2. Storage Cost (u)
Cost to store physical commodity.

| Commodity | Typical Storage Cost |
|-----------|---------------------|
| Oil | 1-3% of value/year |
| Gold | 0.5-1% of value/year |
| Copper | 2-4% of value/year |

### 3. Convenience Yield (y)
The benefit of physically holding the commodity.

**High convenience yield when:**
- Supply shortages
- High demand
- Limited storage

**Example:**
- Gold has ~1% convenience yield
- Oil has ~1-2%

---

## Net Carry

```
Net Carry = r + u - y
```

| Market | Typical Net Carry |
|--------|------------------|
| Oil | 3-5% (contango) |
| Gold | 3-4% (contango) |
| Natural Gas | -2 to +2% (varies) |

---

## Contango vs. Backwardation

### Contango (Normal Market)
Forward prices > Spot prices (upward curve)

**Causes:**
- High storage costs
- Low convenience yield
- Normal market (most commodities)

**Example:**
```
Spot: $75
3-month: $76
6-month: $77
12-month: $80
```

### Backwardation (Inverted Market)
Forward prices < Spot prices (downward curve)

**Causes:**
- Supply shortage now
- High convenience yield
- Expected price decline

**Example:**
```
Spot: $75
3-month: $74
6-month: $72
12-month: $70
```

---

## Calculating Forward Prices

### Example: Oil Forward

**Given:**
- Spot: $75/bbl
- Risk-free rate: 4.5%
- Storage: 2%
- Convenience yield: 1%
- Time: 1 year

**Step 1: Net Carry**
```
Net Carry = 4.5% + 2% - 1% = 5.5%
```

**Step 2: Forward Price**
```
F = 75 × e^(0.055 × 1) = $79.21
```

### For Different Maturities:

| Maturity | Calculation | Forward Price |
|----------|-------------|---------------|
| 1 month | 75 × e^(0.055/12) | $75.34 |
| 3 months | 75 × e^(0.055/4) | $76.05 |
| 6 months | 75 × e^(0.055/2) | $77.12 |
| 12 months | 75 × e^(0.055) | $79.21 |

---

## Implied Calculations

### Implied Convenience Yield

If you know forward price, you can solve for convenience yield:

```
y = r + u - ln(F/S) / t

Example:
S = $75
F = $78 (1 year)
r = 4.5%
u = 2%

y = 4.5% + 2% - ln(78/75)/1
y = 6.5% - 3.9%
y = 2.6%
```

### Implied Forward Rate

```
Implied Forward = Spot × e^(net_carry × t)
```

---

## Hedging Implications

### For Producers (Long Physical):
- **Contango:** Sell futures, earn negative roll yield (cost)
- **Backwardation:** Sell futures, earn positive roll yield (benefit)

### For Consumers (Need Physical):
- **Contango:** Buy futures, pay premium
- **Backwardation:** Buy futures, get discount

### Roll Yield:
```
Roll Yield = (F_old - F_new) / F_old

Contango: Negative roll yield
Backwardation: Positive roll yield
```

---

## Real-World Factors

### What Affects Forward Curves:

| Factor | Effect on Forward |
|--------|------------------|
| Interest rates ↑ | Forward ↑ |
| Storage costs ↑ | Forward ↑ |
| Convenience yield ↑ | Forward ↓ |
| Time to delivery ↑ | Forward ↑ |
| Expected spot ↓ | Forward ↓ |

### Seasonality:
- Natural gas: Higher in winter
- Agriculture: Harvest vs. planting
- Refined products: Driving season

---

## Trading Strategies

### Calendar Spreads:
Buy one month, sell another

```
Spread = Near month - Far month

If oil Mar $76, Dec $79
Spread = $76 - $79 = -$3 (contango)
```

### Contango Trade:
- Sell near-month, buy far-month
- Profit from convergence to spot

### Backwardation Trade:
- Buy near-month, sell far-month
- Profit from convergence to spot

---

## Sources

- CFA Institute - "Derivatives"
- CME Group - "Understanding Futures"
- Investopedia

---

## Related Files

- `forward_price_calculator.py` - Python model
- Python models in `/commodities/python/`

## Excel Templates

For professional Excel templates, we recommend:
- [Damodaran's Valuation Spreadsheets](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/spreadsh.htm)
- [CME Group](https://www.cmegroup.com/education/) - Commodity pricing resources
