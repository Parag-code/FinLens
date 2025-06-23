def compute_fraud_score(anomaly_df, sentiment):
    anomaly_factor = min(len(anomaly_df) * 10, 70)
    sentiment_factor = {"Positive": 0, "Neutral": 10, "Negative": 30}
    score = anomaly_factor + sentiment_factor.get(sentiment, 10)
    return max(score, 5)