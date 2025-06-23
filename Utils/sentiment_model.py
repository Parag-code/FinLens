import pandas as pd

def analyze_sentiment(df=None):
    # If df is provided, use recent price movement for sentiment
    if df is not None and 'Close' in df.columns and len(df) > 2:
        last_close = df['Close'].iloc[-1]
        prev_close = df['Close'].iloc[-2]
        if last_close > prev_close:
            return "Positive"
        elif last_close < prev_close:
            return "Negative"
        else:
            return "Neutral"
    # Fallback to random for demo
    import random
    sentiments = ["Positive", "Neutral", "Negative"]
    return random.choice(sentiments)