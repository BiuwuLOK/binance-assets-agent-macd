# data_fetcher.py
import pandas as pd
from binance.client import Client

def get_bars(client, asset='ETH'):
    bars = client.get_historical_klines(f"{asset}USDT", Client.KLINE_INTERVAL_1MINUTE, start_str="1 hour ago UTC")
    df = pd.DataFrame(bars, columns=[
        "Open time", "Open", "High", "Low", "Close", "Volume", "Close time",
        "Quote asset volume", "Number of trades", "Taker buy base asset volume",
        "Taker buy quote asset volume", "Ignore"]
    )
    df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
    df.set_index('Open time', inplace=True)
    df = df.iloc[:, :5]
    df.dropna(inplace=True)  # Remove NaN values
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df
