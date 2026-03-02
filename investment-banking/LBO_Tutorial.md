# Investment Banking - LBO Tutorial

**Objective:** Understanding how Private Equity (PE) firms buy companies using debt to generate outsized returns.

---

## Table of Contents

1. [The "Rental Property Flip" Metaphor](#the-rental-property-flip-metaphor)
2. [The Private Equity Dictionary](#the-private-equity-dictionary)
3. [Sources & Uses: The Architecture of the Deal](#sources--uses-the-architecture-of-the-deal)
4. [The Three Levers of Value Creation](#the-three-levers-of-value-creation)
5. [The LBO Process](#the-lbo-process)
6. [IRR: The Truth Behind the Returns](#irr-the-truth-behind-the-returns)
7. [The Ideal LBO Candidate](#the-ideal-lbo-candidate)
8. [Final Recap](#final-recap)

---

## The "Rental Property Flip" Metaphor

Imagine buying an apartment for **$1,000,000**.

- You use only **$200,000** of your own cash (the **Sponsor Equity**).
- You take an **$800,000** mortgage from a bank (the **Senior Debt**).
- You rent out the apartment. The **rent** (the company's **Free Cash Flow**) pays the mortgage.
- After 5 years, you pay down the mortgage and sell the apartment for **$1,500,000**.

**The Result**: You turned $200k into $900k (4.5x return!) because you used a "mortgage" to buy the asset.

> **💡 Schweser Note (The Leverage Megaphone):** In an LBO, debt is a double-edged sword. It amplifies your returns—both the good and the bad. If the apartment value drops, you still owe the bank $800k. That's why PE firms focus on companies with stable cash flows—they need that "rent" to service the debt.

---

## The Private Equity Dictionary

Before we look at the mechanics, let's define the terms:

- **Leverage:** Using debt (borrowed money) to buy an asset. The more leverage, the less of your own cash you need.

- **Sponsor Equity:** The Private Equity firm's own money put into the deal. This is the "skin in the game."

- **Senior Debt:** The primary loan from banks. It has first claim on the company's assets if things go wrong.

- **Mezzanine Debt:** Higher-interest debt that sits between senior debt and equity. Riskier, so it charges a higher rate.

- **Paydown:** Using the company's cash flow to reduce the principal of the debt over time.

- **IRR (Internal Rate of Return):** The annual compounded return on your equity investment. The most important metric in PE.

- **MoM (Multiple of Money):** How many times your original investment you get back. (e.g., 2.0x = double your money).

- **Exit:** Selling the company (usually after 5-7 years) to realize the return.

---

## Sources & Uses: The Architecture of the Deal

Every LBO starts with a simple question: **"Where is the money coming from, and where is it going?"**

This is called the **Sources & Uses** table. It must always balance—Sources must equal Uses.

### Example - Sources & Uses

| **SOURCES** | $M | | **USES** | $M |
|-------------|----|-|----------|-----|
| Senior Debt | $600 | | Purchase Equity | $800 |
| Mezzanine Debt | $100 | | Refinance Existing Debt | $200 |
| Sponsor Equity | $300 | | Transaction Fees | $30 |
| | | | | |
| **TOTAL SOURCES** | **$1,000** | | **TOTAL USES** | **$1,030** |

*Wait—$1,000 ≠ $1,030! The difference ($30M) is the "Banker Tax" (fees). These must be paid in cash at closing, so the Sponsor often needs to bring more equity or finance the fees into the deal.*

### 💡 Schweser Note (The "Deal Logic")

In practice, the Sources & Uses looks like this:

| **SOURCES** | $M | | **USES** | $M |
|-------------|----|-|----------|-----|
| Senior Debt | $600 | | Purchase Equity | $800 |
| Mezzanine Debt | $100 | | Refinance Existing Debt | $200 |
| Sponsor Equity | $330 | | Transaction Fees | $30 |
| | | | | |
| **TOTAL SOURCES** | **$1,030** | | **TOTAL USES** | **$1,030** |

> **Key Insight:** The "Uses" always drive the "Sources." Once you know the Purchase Price and Fees, you can work backward to figure out how much debt and equity you need to close the deal.

---

## The Three Levers of Value Creation

An LBO generates returns through **three levers**. Think of them like improving your rental property:

| Lever | Property Analogy | Corporate Reality |
|-------|-----------------|-------------------|
| **1. Deleveraging** | Using rent to pay down your mortgage. | Using the company's Free Cash Flow to pay down debt principal. |
| **2. Operational Improvement** | Renovating the kitchen to charge higher rent. | Cutting costs, boosting EBITDA, improving margins. |
| **3. Multiple Expansion** | Selling in a "hotter" neighborhood for a higher price. | Selling the company at a higher EBITDA multiple than you bought it. |

### 💡 Schweser Note (The Return Math)

In a typical LBO:

- **Deleveraging** contributes ~30-40% of the total return.
- **EBITDA Growth** contributes ~30-40% of the total return.
- **Multiple Expansion** contributes ~20-30% of the total return.

*Why?* Because the most predictable lever is paying down debt with cash flow. PE firms can control costs, but they can't control the macro environment for selling at a higher multiple.

---

## The LBO Process

### Step 1: Buy the Company (Entry)

- Use debt (Senior + Mezzanine) and a small amount of sponsor equity.
- The company now has new owners, but also a large debt burden.

### Step 2: Pay Down Debt (Hold Period)

- For 5-7 years, the management team runs the business.
- The company's Free Cash Flow goes primarily to paying down debt.
- Less debt = more equity value remaining.

### Step 3: Sell the Company (Exit)

- Sell to another PE firm, a strategic buyer, or IPO.
- Because debt is lower, the **Equity Value** (what the PE firm keeps) is much higher.

**Python Tool**: [Run LBO_Model.py](./Python/LBO_Model.py)

---

## IRR: The Truth Behind the Returns

**IRR (Internal Rate of Return)** is the most important metric in Private Equity. It answers: **"What is the annual compound growth rate of my money?"**

### The Formula

```
IRR = (Exit Value ÷ Entry Value)^(1/Years) - 1
```

### Example Calculation

| Input | Value |
|-------|-------|
| Equity Invested (Entry) | $100M |
| Equity Received (Exit) | $250M |
| Years Held | 5 years |

**Calculation:**
```
IRR = (250 ÷ 100)^(1/5) - 1
IRR = 2.0^0.2 - 1
IRR = 1.149 - 1
IRR = 14.9% (rounded to 15%)
```

### 💡 Schweser Note (The Time Trap)

In PE, **speed matters more than total profit**.

| Scenario | Total Profit | Years | IRR |
|---------|--------------|-------|-----|
| A | 2x return | 3 years | **26%** |
| B | 3x return | 10 years | **12%** |

> **Key Insight:** Scenario A is the "better" deal in PE, even though you make less total money. Why? Because you can reinvest that money in another deal and compound your returns. A 26% IRR beats a 12% IRR every time in the world of PE.

---

## The Ideal LBO Candidate

Not every company is a good LBO target. PE firms look for:

1.  **Stable, Predictable Cash Flows:** You need "rent" to pay the mortgage. Companies with cyclical or volatile earnings are risky.

2.  **Low CapEx Requirements:** You don't want to spend all your cash on fixing machines. Companies that generate high free cash flow relative to EBITDA are ideal.

3.  **Strong Asset Base:** If the company defaults, the banks want tangible assets (real estate, equipment) to seize.

4.  **Clear "Operational Improvement" Path:** There must be room to cut costs or grow revenue without massive investment.

> **💡 Schweser Note (The "Boring" Business):** The best LBO targets are often "boring" companies—regional banks, packaging companies, utility providers. They generate steady cash, don't need constant innovation, and have tangible assets. Sexy tech companies rarely make good LBO targets because they burn too much cash!

---

## Final Recap

🏃 **Executive Summary:**

1.  **Buy Low with Debt:** Use a "mortgage" (debt) to buy a company with a small down payment (sponsor equity).
2.  **Pay Down the Mortgage:** Use the company's own cash flow to eliminate debt over 5-7 years.
3.  **Sell High:** Exit at a higher valuation, keeping the difference as profit for the PE firm.

**The PE Goal:** Turn $300M of equity into $600M+ by using debt as a lever.

**Python Tool**: [Run LBO_Model.py](./Python/LBO_Model.py) to see how the three levers translate into returns.
