# Equities - Pricing Models

**Objective:** Calculating the "Required Rate of Return" and the cost of investing in a stock.

---

## Table of Contents
1. [Pricing vs. Valuation](#pricing-vs-valuation)
2. [Method 1: CAPM](#method-1-capm)
3. [Method 2: WACC](#method-2-wacc)
4. [Summary](#summary)

---

## 1. Pricing vs. Valuation
- **Valuation** is "What is it worth?" (The Math).
- **Pricing** is "How much return do I *require* to take this risk?" (The Market Price of Risk).

---

## 2. Method 1: CAPM (Capital Asset Pricing Model)
How much extra profit do I need to earn for taking a risk on a specific stock?

```
Cost of Equity = Risk-Free Rate + Beta × (Market Risk Premium)
```

- **Risk-Free Rate**: What you'd earn by buying a 10-year US Treasury bond (4-5%).
- **Beta**: How "jumpy" the stock is compared to the whole market.
    - *Beta = 1.0*: Moves exactly with the market.
    - *Beta > 1.0*: More volatile (Risky!).
    - *Beta < 1.0*: Less volatile (Safe!).
- **Market Risk Premium**: The extra return for being in the stock market (usually 5-7%).

**Python Tool**: [Run CAPM_Calculator.py](./Python/CAPM_Calculator.py)

---

## 3. Method 2: WACC (Weighted Average Cost of Capital)
What is the total cost to fund the entire company (both loans and shares)?

```
WACC = [Weight of Equity × Cost of Equity] + [Weight of Debt × Cost of Debt × (1 - Tax Rate)]
```

---

## 4. Summary
Equities pricing is about **risk**.
1. **CAPM** tells us what return we should demand from a stock.
2. **WACC** tells us what it costs the company to exist.
