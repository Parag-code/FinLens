import pandas as pd
import numpy as np

def detect_anomalies(df):
    df = df.copy()
    df['z_score'] = (df['Close'] - df['Close'].rolling(window=7).mean()) / df['Close'].rolling(window=7).std()
    df['Volume_z'] = (df['Volume'] - df['Volume'].rolling(window=7).mean()) / df['Volume'].rolling(window=7).std()
    df['anomaly'] = (abs(df['z_score']) > 1.5) | (df['Volume_z'] > 1.5)
    return df[df['anomaly'] == True]