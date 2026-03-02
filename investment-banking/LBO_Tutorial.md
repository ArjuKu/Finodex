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

---

## 📊 Step-by-Step Paper LBO (The "Workbook" Example)

Here is a complete numerical walkthrough of an LBO. This is the exact type of calculation you'd do on a whiteboard in an interview.

### The Inputs

| Input | Value |
|-------|-------|
| Purchase EV | $1,000M |
| Entry EBITDA | $200M |
| Entry Multiple | 5.0x |
| Debt % | 70% ($700M) |
| Equity % | 30% ($300M) |
| EBITDA Growth | 5% per year |
| Interest Rate | 8% |
| Tax Rate | 21% |
| CapEx % of EBITDA | 25% |
| Exit Multiple | 5.0x (same as entry) |

---

### Year 1: The Math

| Line Item | Calculation | Value ($M) |
|-----------|-------------|-------------|
| **EBITDA** | Year 0 × (1 + 5%) | $210M |
| **Interest** | $700M × 8% | $56M |
| **EBT** | $210M - $56M | $154M |
| **Tax** | $154M × 21% | $32M |
| **Net Income** | $154M - $32M | $122M |
| **CapEx** | $210M × 25% | $53M |
| **Cash for Debt** | $122M + $53M (add back D&A*) | $175M |

*D&A is already "in" EBITDA as a non-cash expense, so we add it back to get real cash.*

---

### Year 1-5: Debt Paydown Schedule

| Year | Beginning Debt | Interest | Cash Paydown | Ending Debt |
|------|----------------|----------|--------------|-------------|
| 1 | $700M | $56M | $175M | $525M |
| 2 | $525M | $42M | $184M | $341M |
| 3 | $341M | $27M | $193M | $148M |
| 4 | $148M | $12M | $203M | $0M* |
| 5 | $0M | $0M | $213M | $0M |

*Note: In Year 4, the debt is fully paid off. Any remaining cash stays in the company as "cash on hand."

---

### Exit: Year 5 Valuation

| Line Item | Calculation | Value ($M) |
|-----------|-------------|-------------|
| Exit EBITDA | $200M × 1.05^5 | $255M |
| Exit EV | $255M × 5.0x | $1,276M |
| Less: Remaining Debt | | $0M |
| **Exit Equity Value** | | **$1,276M** |

---

### The Return: IRR & MoM

| Metric | Calculation | Result |
|--------|-------------|--------|
| Entry Equity | | $300M |
| Exit Equity | | $1,276M |
| **Multiple of Money (MoM)** | $1,276 ÷ $300 | **4.25x** |
| **IRR** | (4.25)^(1/5) - 1 | **33.4%** |

> **💡 Schweser Insight:** A 33% IRR is exceptional. In this example, the majority of the return came from **Deleveraging** (paying off $700M of debt) rather than EBITDA growth or multiple expansion.

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

---

### 📊 Return Attribution: Where Did the Money Come From?

In an LBO, the total gain is broken down into three components. This is a classic interview question.

| Source of Return | Explanation | Example ($M) |
|------------------|-------------|--------------|
| **1. Deleveraging** | Profit from paying down debt. Equity grows faster because debt shrinks. | +$200M |
| **2. EBITDA Growth** | Profit from the business doing better. | +$150M |
| **3. Multiple Expansion** | Profit from selling at a higher multiple than you bought. | +$50M |
| **Total Gain** | | **+$400M** |

#### How to Calculate Attribution

```
Entry Equity = $300M
Exit Equity = $700M (assuming no debt left)
Total Gain = $700M - $300M = $400M

Attribution Math:
- Deleveraging = Entry Debt × (Debt Paydown %)
- EBITDA Growth = Entry EBITDA × Growth Rate × Years
- Multiple Expansion = Exit EBITDA × (Exit Multiple - Entry Multiple)
```

---

### 🧮 IRR Shortcuts (Mental Math)

In interviews, you won't have a calculator. Here's the mental math shortcut:

| MoM (Multiple of Money) | 3 Years | 5 Years | 7 Years |
|-------------------------|---------|---------|---------|
| 1.5x | 14% | 8% | 6% |
| 2.0x | 26% | 15% | 10% |
| 2.5x | 35% | 20% | 14% |
| 3.0x | 44% | 25% | 18% |
| 4.0x | 59% | 33% | 24% |

> **💡 Schweser Note:** The "Rule of 72" for IRR: **72 ÷ Years = Approximate IRR for 2.0x return.**
> - 2x in 5 years → 72 ÷ 5 ≈ 14% IRR ✓

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

---

## Outlook & The Real World

### What We Didn't Cover

Real-world LBO models in investment banks are significantly more complex than what we've built here. A few key concepts you'll encounter in professional settings:

- **Management Rollovers:** Often, the existing management team keeps a portion of their equity in the deal (reinvesting alongside the PE firm) to align incentives.
- **Dividend Recaps:** In some deals, the PE firm takes out additional debt years after the buyout to pay themselves a dividend—extracting cash without selling the company.
- **Complex Debt Structures:** Beyond Senior and Mezzanine debt, you'll see Unitranche (combined loan), PIK (Paid-in-Kind) interest, andcovenant packages that restrict the company from taking certain actions.

### The Complexity Trap

> **💡 Real Talk:** In a live deal, the Excel model isn't 100 rows—it's often 50+ tabs with circular references that require iterative solving. One small change to "Assumptions" can ripple through the entire model.

### Recommended Next Steps

- **Read:** *Barbarians at the Gate* by Bryan Burrough – The definitive story of the RJR Nabisco LBO, showing how deals really get done.
- **Practice:** Explore a professional LBO model template from **Macabacus** or **Wall Street Prep** to see the level of detail professional banks use.
- **Deep Dive:** Study **Dividend Recaps** and **Secondary Buyouts** as the next evolution of the LBO lifecycle.

---

*Last updated: 2026 | Built for learning and interview prep*
