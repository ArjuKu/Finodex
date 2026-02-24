# Commodities Technical Interview Questions

*Curated from trading firms, Bloomberg, and industry sources*

---

## 1. Explain Contango vs. Backwardation

### Contango (Normal Market)
- Futures prices > Spot prices
- Upward sloping curve
- Caused by: storage costs, financing costs, convenience yield

### Backwardation (Inverted Market)
- Futures prices < Spot prices
- Downward sloping curve
- Caused by: supply shortages, expected price declines

### Visual:
```
Contango:        Backwardation:
Spot ----->     <-----
Price            Price
```

---

## 2. What is the Cost of Carry Model?

### Formula:
```
F = S × e^((r + u - y) × t)

Where:
F = Forward price
S = Spot price
r = Risk-free rate
u = Storage cost
y = Convenience yield
t = Time to maturity
```

### Example:
> "If oil spot is $75, risk-free is 4.5%, storage is 2%, convenience yield is 1%, and time is 1 year: F = 75 × e^((0.045 + 0.02 - 0.01) × 1) = $79.21"

---

## 3. What is Convenience Yield?

> "Convenience yield is the benefit of physically holding a commodity. When supply is tight, the convenience yield increases, which lowers forward prices."

**High convenience yield → Lower forward prices**

---

## 4. What is a Calendar Spread?

### Definition:
Trading the price difference between two different delivery months.

### Example:
> "A trader might buy March oil and sell December oil. If they expect the spread to widen, they're 'widening' the spread. If they expect it to narrow, they're 'narrowing' it."

### Why Trade Spreads:
- Lower margin requirements
- Less directional risk
- Express a view on the curve

---

## 5. How Do You Hedge a Long Physical Position?

### For a Producer (e.g., Oil Company):
| Hedge | Purpose |
|-------|---------|
| Sell Futures | Lock in price |
| Buy Puts | Limit downside |
| Collar | Cap upside, protect downside |

### For a Consumer (e.g., Airline):
| Hedge | Purpose |
|-------|---------|
| Buy Futures | Lock in price |
| Buy Calls | Limit upside cost |
| Collar | Cap cost range |

---

## 6. What is Basis Risk?

> "Basis risk is the risk that the spot price and futures price don't move in lockstep. It's the difference between the hedged asset and the futures contract."

### Example:
> "If you hedge heating oil with crude oil futures, and crude goes up 5% but heating oil only goes up 3%, you have basis risk."

---

## 7. What is Mark-to-Market?

> "Futures are marked to market daily. Your P&L is calculated each day based on the change in settlement price. This is why futures require margin - to cover daily losses."

---

## 8. What are the Greeks for Commodities Options?

| Greek | Definition | For Commodities |
|-------|------------|-----------------|
| Delta | Price change per $1 move in underlying | Changes with forward |
| Gamma | Delta change rate | Important for gamma trading |
| Vega | Sensitivity to volatility | Higher for longer-dated |
| Theta | Time decay | Important for option sellers |

---

## 9. What is the Difference Between Options on Spot vs. Futures?

### Spot Options:
- Settle based on spot price
- More expensive (cost of carry built in)
- Less common in commodities

### Futures Options:
- Settle based on futures price
- Standard in commodities
- Use Black-76 model

---

## 10. What is a Roll Yield?

> "Roll yield is the return earned from rolling a futures contract forward as it approaches expiration."

- **In contango**: Roll yield is negative (you pay more for next contract)
- **In backwardation**: Roll yield is positive (you receive more for next contract)

---

## 11. How Do You Value a Commodity Company?

### Methods:
1. **NAV/DCF** - Project cash flows from reserves
2. **EV/Reserves** - Value per barrel/ounce
3. **EV/Production** - Value per unit of production

### Key Metrics:
| Metric | Formula |
|--------|---------|
| Reserve Life | Reserves / Annual Production |
| F&D Cost | Finding & Development cost per barrel |
| AISC | All-in sustaining cost per ounce/pound |

---

## 12. What Drives Commodity Prices?

### Energy (Oil/Gas):
- OPEC+ decisions
- US shale production
- Inventory levels
- Geopolitics
- Economic growth

### Metals:
- China demand (construction, EV)
- Supply/disruption
- Dollar strength
- Interest rates

### Agriculture:
- Weather/harvest
- Exports
- Biofuel demand
- Government policy

---

## 13. What is a Butterfly Spread?

### Structure:
Buy 1 near-month, Sell 2 mid-month, Buy 1 far-month

### Purpose:
Profit from a specific view on the curve shape without directional exposure.

---

## 📝 Your Turn - Add Technical Questions

*Contributors: Add real interview questions and answers here*

### [Your Name] - Question
> **Q:** [ADD QUESTION]
>
> **A:** [ADD ANSWER]

---

## Sources

- Bloomberg
- CME Group
- TradingView
- Investopedia

---

## Related

- [Interview Guide](./interview-guide/) - Behavioral questions
- [Downloads](./downloads/) - Print-friendly PDFs
