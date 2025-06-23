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
