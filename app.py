import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.timeseries_model import detect_anomalies
from utils.sentiment_model import analyze_sentiment
from utils.fraud_score import compute_fraud_score
from utils.pdf_report import generate_pdf_report
from PIL import Image
import io

st.set_page_config(page_title="FinLens", page_icon="📈")

logo = Image.open("logo.png")
st.image(logo, use_column_width=False, width=250)
st.title("FinLens – Insider Trading & Market Manipulation Detector")
st.markdown("#### Your Lens into Market Integrity")

uploaded_file = st.file_uploader("Upload Stock CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["Date"])
    st.subheader("Stock Data Preview")
    st.dataframe(df.head())

    st.subheader("📈 Price Anomaly Detection")
    anomaly_df = detect_anomalies(df)
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Close"], label="Close Price")
    ax.scatter(anomaly_df["Date"], anomaly_df["Close"], color="red", label="Anomalies")
    ax.legend()
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("📰 Sentiment Analysis (Synthetic)")
    sentiment = analyze_sentiment(df)
    st.info(f"News Sentiment: **{sentiment}**")

    st.subheader("🔐 Fraud Risk Score")
    risk_score = compute_fraud_score(anomaly_df, sentiment)
    st.success(f"Risk Score: **{risk_score:.2f}/100**")

    if st.button("📥 Download PDF Report"):
        pdf_path = generate_pdf_report(df, anomaly_df, sentiment, risk_score)
        with open(pdf_path, "rb") as f:
            st.download_button("Download PDF", f, file_name="finlens_report.pdf")