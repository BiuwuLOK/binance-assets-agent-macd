# trade_logic.py
import time

def execute_trade(client, asset_info):
    bars = get_bars(client, asset_info['asset'])
    should_buy = bars['MACD'][-1] > 0 and bars['Pct Change 30m'][-1] > 0
    should_sell = bars['MACD'][-1] < 0 and bars['Pct Change 30m'][-1] < 0
    print(f"Asset: {asset_info['asset']} / Is Long: {asset_info['is_long']} / Should Buy: {should_buy} / Should Sell: {should_sell}")
    if not asset_info['is_long'] and should_buy:
        print(f"We are buying {asset_info['order_size']} {asset_info['asset']}")
        order = client.order_market_buy(symbol=f"{asset_info['asset']}USDT", quantity=asset_info['order_size'])
        asset_info['is_long'] = True
    elif asset_info['is_long'] and should_sell:
        print(f"We are selling {asset_info['order_size']} {asset_info['asset']}")
        order = client.order_market_sell(symbol=f"{asset_info['asset']}USDT", quantity=asset_info['order_size'])
        asset_info['is_long'] = False

def run_trading_bot(client, assets):
    while True:
        for asset_info in assets:
            execute_trade(client, asset_info)
        print('Iteration ended')
        print(assets)
        print("*" * 20)
        time.sleep(10)  # Pause for 10 seconds before the next iteration
