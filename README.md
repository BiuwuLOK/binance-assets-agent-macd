markdown

# Binance Trading Bot

A multi-asset crypto trading bot that uses technical indicators such as MACD to automate trading on Binance. This bot fetches historical data, applies trading logic, and simulates or executes trades on the Binance Testnet.

## Project Structure
```
binance_trading_bot/
├── main_agent/
│   ├── __init__.py
│   ├── __main__.py
│   ├── data_fetcher.py
│   ├── indicators.py
│   ├── trade_logic.py
│   └── run.py
├── data/
│   ├── assets.csv
│   ├── assets.txt
├── README.md
├── setup.py
└── requirements.txt
```

## Features

- Fetches historical 1-minute bars from Binance
- Calculates MACD and percentage price change indicators
- Determines buy/sell signals based on the trading strategy
- Supports multiple assets
- Interactive setup for API keys and asset configurations
- Option to import asset data from .csv or .txt files

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/binance_trading_bot.git
Navigate to the project directory:

bash
cd binance_trading_bot
Install the required dependencies:

bash
pip install -r requirements.txt
Usage
Running the Bot
Ensure you have your Binance API key and secret ready.

Run the bot:

bash
python -m main_agent
Follow the prompts to enter your API information and configure your assets.

Importing Assets from a File
Place your assets.csv or assets.txt file in the data/ directory.

The file should have the following structure:

asset,is_long,order_size
BTC,False,0.0025
LTC,False,100
TRX,False,1000
ETH,False,0.03
BNB,False,0.25
XRP,False,100
Run the bot and choose the option to import assets from the file.

Contributing
Fork the repository.

Create a new branch.

Make your changes and commit them.

Push to the branch.

Create a new Pull Request.

License
This project is licensed under the MIT License.

Acknowledgements
Binance API

pandas

pandas-ta

matplotlib

Contact
For any questions or suggestions, please open an issue or contact me at [your email here].

Thank you for using the Binance Trading Bot! Happy trading! 📈


### Explanation:
1. **Project Structure**: Provides an overview of the project directory.
2. **Features**: Lists the key functionalities of the bot.
3. **Installation**: Step-by-step instructions for setting up the project.
4. **Usage**: Guidelines for running the bot and importing assets from a file.
5. **Contributing**: Instructions for how to contribute to the project.
6. **License**: Information on the project's license.
7. **Acknowledgements**: Credit to the libraries and resources used.
8. **Contact**: Information on how to reach out for questions or suggestions.
```
