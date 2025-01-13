# run.py
import os
import pandas as pd
from binance.client import Client
from .trade_logic import run_trading_bot

def load_assets_from_file(file_path):
    # Construct the full file path
    file_path = os.path.join('data', file_path)

    # Determine file type and read the file accordingly
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.txt'):
        df = pd.read_csv(file_path, sep="\t")
    else:
        raise ValueError("Unsupported file type. Please use .csv or .txt files.")
    
    # Ensure necessary columns are present
    required_columns = {'asset', 'is_long', 'order_size'}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"File must contain columns: {required_columns}")

    # Convert DataFrame to list of dictionaries
    assets = df.to_dict(orient='records')
    return assets

def main():
    api_key = input("Enter your Binance API key: ")
    api_secret = input("Enter your Binance API secret: ")
    client = Client(api_key, api_secret, testnet=True)

    # Ask user if they want to import assets from a file
    use_file = input("Do you want to import assets from a file (yes/no)? ").strip().lower()
    
    if use_file == 'yes':
        file_path = input("Enter the file name (e.g., assets.csv or assets.txt): ").strip()
        assets = load_assets_from_file(file_path)
        print("Assets loaded from file:")
        print(pd.DataFrame(assets))
    else:
        assets = []
        print("Enter the assets, whether they are long or short, and order sizes you want to trade. Type 'done' when you are finished.")
        while True:
            asset = input("Enter asset symbol (e.g., BTC), or 'done' to finish: ").upper()
            if asset == 'DONE':
                break
            is_long = input(f"Is {asset} long (True/False)? ").strip().capitalize()
            order_size = float(input(f"Enter order size for {asset}: "))
            assets.append({'asset': asset, 'is_long': is_long == 'True', 'order_size': order_size})
    
    run_trading_bot(client, assets)

if __name__ == "__main__":
    main()
