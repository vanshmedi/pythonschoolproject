# Virtual Stock Trading Game

## Introduction
A command-line game where users simulate buying and selling virtual stocks. The goal is to maximize profits through stock trading while prices fluctuate daily.

## Features
- **Login/Signup**: Create an account or log in.
- **Stock Trading**: Buy and sell virtual stocks.
- **Price Simulation**: Stock prices change daily.
- **Portfolio Management**: Track owned stocks and potential gains/losses.
- **Balance Tracking**: Check available funds.
- **Logout**: Exit the game.

## Files
- `users.txt`: Stores user credentials.
- `stonksdata.csv`: Contains stock data (name, lowest price, highest price, current price).
- `user_stocks.csv`: Stores owned stock information.

## Gameplay
1. **Start**: Begin with Rs. 2500.
2. **Main Menu**:  
   - View stock info, buy/sell stocks, check balance, view portfolio, update prices, log out.
3. **Stock Price Simulation**: Prices fluctuate with daily changes.

## Main Functions
- `signup()`: Create a new account.
- `login()`: Log in with existing credentials.
- `add_current_price()`: Set random current prices for stocks.
- `update_previous_prices()`: Simulate the next trading day.
- `trade_stock()`: Buy/sell stocks and update the balance.
- `display_portfolio()`: Show owned stocks and their values.
- `display_stock_info()`: View all stock info with price changes.

## Running the Game
1. Clone the repository and run the script.
2. Login or signup.
3. Trade stocks, view your portfolio, and simulate stock price changes.

## Requirements
- Python 3.x
- `stonksdata.csv` and `user_stocks.csv` for stock and user data.

Enjoy your virtual stock trading experience!
