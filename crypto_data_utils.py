# COINBUDDY/crypto_data_utils.py
import pandas as pd
import os

def get_price_trend(file_path):
    """Calculate 7-day price trend from CSV file."""
    try:
        df = pd.read_csv(file_path)
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        recent = df.tail(7)
        start = recent.iloc[0]['close']
        end = recent.iloc[-1]['close']
        change_pct = ((end - start) / start) * 100

        if change_pct > 5:
            return "rising"
        elif change_pct < -5:
            return "falling"
        else:
            return "stable"
    except Exception as e:
        print(f"[ERROR] Could not process {file_path}: {e}")
        return "unknown"
