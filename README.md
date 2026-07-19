# 📊 SMCPivotEdge

> **Institutional-Grade Actionable Day Trade & Scalp Levels Engine for NSE India**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-smcpivotedge.pages.dev-00d09c.svg?style=for-the-badge&logo=cloudflare)](https://smcpivotedge.pages.dev/nse-daytrade-pivots?sym=EXICOM) [![Market](https://img.shields.io/badge/Market-NSE%20India-orange.svg?style=for-the-badge&logo=target)](https://www.nseindia.com/) [![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE) [![Stack](https://img.shields.io/badge/Stack-Vanilla%20JS%20%7C%20HTML5%20%7C%20CSS3-blue.svg?style=for-the-badge)](https://developer.mozilla.org/) [![Speed](https://img.shields.io/badge/Performance-Zero%20Dependency-brightgreen.svg?style=for-the-badge)]()

---

**SMCPivotEdge** is an institutional-grade, real-time technical decision engine built specifically for day traders, scalpers, and option buyers in the **National Stock Exchange (NSE) of India**.

The platform synthesizes two powerful trading methodologies into a single zero-latency workspace:
1. **Smart Money Concepts (SMC)**: Tracking institutional liquidity zones, order flow equilibrium channels (**Daily Value Area / DVA**), polarity swaps (broken support floors converting into resistance ceilings), and macro volatility expansion boundaries ($R_4-R_6$ / $S_4-S_6$).
2. **Mathematical Pivot Dynamics**: Multi-model floor pivots (Floor, Central Pivot Range / CPR, Camarilla, Woodie, DeMark, Fibonacci) mapped against multi-timeframe volume metrics.

> **Live Public Testing App**: [**Launch Live SMCPivotEdge Web App ↗**](https://smcpivotedge.pages.dev/nse-daytrade-pivots?sym=EXICOM)  
> *Use the test app for live pivot analysis, intraday sector setup screening, and actionable trade matrices instantly in the browser.*

---

### Core Concept & Execution Philosophy: From Lagging Charts to Actionable Precision

Most conventional charting tools force traders to visually interpret lagging indicators (moving average crossovers, lagging oscillators) during high-stress market hours, leading to **execution hesitation, emotional slippage, and unfavorable Risk-to-Reward ratios**.

**SMCPivotEdge eliminates subjectivity by converting raw exchange ticker data into explicit, pre-calculated trade matrices:**

```text
                               ┌─► Exact Entry Trigger (e.g. Above ₹909.00)
                               ├─► Calculated Stop Loss (SL) (e.g. ₹896.05)
Raw Market Data ──► SMCPivotEdge ┼─► Target 1 (Pivot Point) & Target 2 (R1 Resist)
                               ├─► Mathematical Risk:Reward Ratio (e.g. 1 : 2.77)
                               └─► Automated Strategy Verdict (e.g. NEUTRAL / WAIT)
```

Instead of asking *"Where might the stock go?"*, SMCPivotEdge provides instant execution boundaries:
> **"If CGPOWER breaches ₹909.00, trigger LONG with Stop Loss at ₹896.05 (S2 Support), Target 1 at ₹931.95 (Pivot Point), Target 2 at ₹944.90 (R1 Resistance), yielding a quantified 1 : 2.77 Risk:Reward Ratio."**

## Key Unique Selling Propositions (USPs)

| How It Gives You an Advantage |
| :--- |
| Generates explicit **LONG (Buy)** and **SHORT (Sell)** triggers with exact numeric Stop Losses, Target 1, Target 2, and calculated Risk:Reward ratios. |
| Detects broken support floors (e.g., `S1 Resist (Broken)`) and dynamically re-classifies them as new resistance levels for rally shorting. |
| Instant toggle between **Day Trade Pivots (1D)** for session planning and **Scalp ATR (5M)** for rapid momentum entries. |
| Scans peer stocks in real-time to detect Day High Breakouts (`BO`), Low Breakdowns (`BD`), Volatility Squeezes (`SQZ`), and Volume Trends (`BULL`/`BEAR`). |
| Instant toggle between **Session Range (Micro)** for intraday scalps and **52-Week Range (Macro)** for swing structural levels. |
| Pure client-side Vanilla JS execution across the complete NSE catalog with zero database bottlenecks. |

## Application Interface & Actionable Modules

### Header Overview & Live Sector Setup Scanner
Real-time sector peer setup classification (`BO`, `BD`, `PDC`, `SQZ`, `BULL`, `BEAR`) sorted by turnover liquidity alongside circuit limits, gaps, and 52-week ranges.

![Header & Sector Scanner](https://raw.githubusercontent.com/anoopmaddasseri/SmcPivotEdge/main/screenshots/overview.png)

### Multi-Indicator Technical Verdict Matrix
Evaluates 9 key technical indicators simultaneously and converts them into semantic bias badges (**BULLISH**, **BEARISH**, **HEALTHY**, **RANGING**, **WEAK**).

![Technical Verdict Matrix](https://raw.githubusercontent.com/anoopmaddasseri/SmcPivotEdge/main/screenshots/verdict.png)

- **VWAP (Baseline)**: Volume-weighted institutional anchor point.
- **EMA Trend**: Dynamic exponential moving average alignment.
- **RSI (14)**: Relative Strength Index evaluation.
- **ATR (14)**: Average True Range volatility measure.
- **Supertrend (10,3)**: Trend direction and trailing stop level.
- **MACD (12,26,9)**: Momentum convergence/divergence signal.
- **Bollinger Bands (20)**: Volatility band expansion and compression.
- **ADX (14) & DI Bias**: Trend strength indicator with directional index (`▼ BEARISH DI` / `▲ BULLISH DI`).

### Structural Market Pivots & Polarity Swap Engine
Calculates standard floor pivots alongside **Daily Value Area (DVA)** equilibrium channels and **Macro Extension Blocks** ($R_4 - R_6$ and $S_4 - S_6$) for explosive volatility days.

![Market Structure Pivots](https://raw.githubusercontent.com/anoopmaddasseri/SmcPivotEdge/main/screenshots/pivots.png)

```text
Resist Ext (R4/5/6)  ──►  Macro Breakout Targets (Extreme Volatility Days)
Resistance 3        ──►  Extreme Structural Ceiling
Resistance 2        ──►  Secondary Profit-Taking Target
Resistance 1        ──►  Primary Resistance Hurdle
PIVOT POINT         ──►  Institutional Equilibrium / Structural Bias Line
Daily Value Area    ──►  VWAP Volatility Equilibrium Channel (DVA)
S1 Resist (Broken)  ──►  Polarity Swap: Broken Support Floor becomes Rally Resistance
Support 2 & 3       ──►  Key Bounce Floors
Support Ext (S4/5/6) ──►  Macro Breakdown Extension Targets
```

### Actionable Trade Levels Matrix & Setup Recommendation
Eliminates position-sizing ambiguity by outputting complete trade parameters automatically.

![Actionable Trade Matrix](https://raw.githubusercontent.com/anoopmaddasseri/SmcPivotEdge/main/screenshots/trade_matrix.png)

#### Measurable Trade Output Sample:
- **LONG (Buy) Setup**: Trigger Above `₹909.00` | Stop Loss `₹896.05` | Target 1 `₹931.95` | Target 2 `₹944.90` | **R:R 1 : 2.77**
- **SHORT (Sell) Setup**: Trigger Below `₹896.05` | Stop Loss `₹909.00` | Target 1 `₹873.10` | Target 2 `₹850.15` | **R:R 1 : 3.54**
- **Automated Setup Recommendation**: `NEUTRAL / WAIT` — Synthesizes multi-indicator signals into clear advice (`STRONG BUY`, `BUY ON DIPS`, `SELL ON RALLIES`, `WAIT`).

### Micro vs. Macro Fibonacci Retracements
Calculates precise golden ratio retracement floors and ceilings ($23.6\%$, $38.2\%$, $50.0\%$, $61.8\%$, $78.6\%$).

![Fibonacci Retracements](https://raw.githubusercontent.com/anoopmaddasseri/SmcPivotEdge/main/screenshots/fibonacci.png)

- **Session Range (Micro)**: Derived from the previous completed session's High and Low. Ideal for intraday pullback entries and short-covering targets.
- **52-Week Range (Macro)**: Derived from 52-week extremes. Essential for identifying institutional supply/demand blocks and swing reversals.

## Technical Architecture & Performance

- Built purely with HTML5, Vanilla JavaScript (ES6+), and CSS Custom Properties. No heavy frameworks or bundler overhead.
- Integrated local databases (`nse-all-stocks.js` & `nse-stocks.js`) for instant search auto-completion without network delays.
- Injected inline script engine supporting **Dark Mode** (`#0a0a0a`) and high-contrast **Light Mode** (`#f9fafb`) with `localStorage` persistence.
- Automatically resolves Groww search IDs dynamically via proxy to enable seamless one-click external chart views (`↗`).

## Quick Start & Installation

### Method 1: Local Launch
Clone the repository and open `nse-daytrade-pivots.html` directly in your browser:

```bash
git clone https://github.com/anoopmaddasseri/SmcPivotEdge.git
cd SmcPivotEdge
# Open nse-daytrade-pivots.html in your browser
```

### Method 2: Python Local Proxy (Recommended)
To run with local data proxy support:

```bash
python server.py
```
Then navigate to `http://localhost:8000`.

### Method 3: Serverless Cloudflare Deployment
Deploy the included CORS worker script:

```bash
npx wrangler deploy
```

---

## Summary of Trade Setup Codes

| Code | Setup Name | Technical Condition | Actionable Rule |
| :--- | :--- | :--- | :--- |
| `BO` | **Day High Breakout** | Price within **0.1%** of Day High | Look for momentum continuation above high. |
| `BD` | **Day Low Breakdown** | Price within **0.1%** of Day Low | Look for breakdown acceleration below low. |
| `PDC` | **Testing Yesterday's Close** | Price within **0.15%** of Previous Close | Key reversal or breakout test zone. |
| `SQZ` | **Volatility Squeeze** | Day Range is under **0.8%** | Prepare for an explosive directional move. |
| `BULL` | **Bullish Trend** | Intraday gain $\ge +1.5\%$ | Trend continuation on pullbacks. |
| `BEAR` | **Bearish Trend** | Intraday loss $\le -1.5\%$ | Short on weak bounces. |

---

## Disclaimer

SMCPivotEdge is designed as a technical decision-support system for educational and analytical purposes only. Technical pivots, indicator verdicts, and risk cone projections are mathematical models and do not constitute financial advice. Always practice strict position sizing and risk management when trading Indian stock markets.

---

## License

This project is licensed under the [MIT License](LICENSE).
