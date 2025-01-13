# indicators.py
import pandas_ta as ta

def get_macd(data, slow=26, fast=12, signal=9):
    macd = ta.macd(data, slow=slow, fast=fast, signal=signal)
    return macd.iloc[:, -1]
