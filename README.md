# 📈 FinLens – Insider Trading & Market Manipulation Detector

FinLens is a powerful and interactive Streamlit application designed to detect suspicious activities in stock trading. It leverages anomaly detection, sentiment analysis, and fraud scoring to provide a comprehensive assessment of market behavior.

## 🔍 Key Features

- **📥 CSV Upload Support** – Upload historical stock data (with `Date`, `Close`, and `Volume` columns).
- **📈 Price Anomaly Detection** – Identifies abnormal price and volume movements using rolling z-score methods.
- **📰 Sentiment Analysis (Synthetic)** – Simulated news sentiment analysis based on recent stock price changes.
- **🔐 Fraud Risk Scoring** – Calculates a custom fraud score combining anomaly intensity and sentiment.
- **📄 PDF Report Generator** – Instantly generates a downloadable summary report of findings.

---

## 🧠 Behind the Scenes

| Component | Description |
|----------|-------------|
| `timeseries_model.py` | Detects anomalies based on z-scores of price and volume. |
| `sentiment_model.py` | Simulates sentiment analysis using recent price movement trends. |
| `fraud_score.py` | Computes a risk score based on anomalies and sentiment. |
| `pdf_report.py` | Creates a formatted PDF summary report. |

---


## 🛠️ Tech Stack

FinLens is built with a lightweight and fast-performing Python stack:

- **Python** – Core programming language
- **Streamlit** – Interactive UI for real-time web-based dashboards
- **Pandas** – Efficient data processing and manipulation
- **Matplotlib** – Visualization of time series and anomalies
- **FPDF** – Generation of downloadable PDF reports

---

## 💼 Use Cases

FinLens can be used in a variety of financial monitoring and risk analysis applications:

- 🔍 **Insider Trading Detection** – Identify suspicious stock price and volume movements
- 📉 **Market Manipulation Alerts** – Detect coordinated pump-dump schemes or abnormal trades
- 📊 **FinTech & EdTech Demos** – Use as a prototype to showcase data-driven financial insight tools
- 🧠 **Investor Research** – Evaluate company behavior for red flags before making investment decisions
- 🧾 **Regulatory Tools** – Potential add-on for auditing teams to monitor trading behavior

---

## 🙏 Acknowledgment

This project was created as part of a financial AI exploration initiative by **Vaibhav Kumar Srivastav**, a B.Tech student at JECRC University. Inspiration was drawn from current regulatory practices, stock market surveillance systems, and the need for transparent financial tools powered by AI.

Special thanks to:
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [FPDF for Python](https://pyfpdf.readthedocs.io/)
