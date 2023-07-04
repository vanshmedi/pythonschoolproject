import csv
import random

def show_login_menu():
    print("---------- Login/Sign up ----------")
    print("1. Login")
    print("2. Signup")
    print("-----------------------------------")

def signup():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")

    print("New user created successfully")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    with open("users.txt", "r") as file:
        user_data = file.readlines()

    for user in user_data:
        stored_username, stored_password = user.strip().split(",")
        if username == stored_username and password == stored_password:
            print("Login successful")
            return True
    
    print("Invalid username or password")
    return False

def show_menu():
    print("---------- Main Menu ----------")
    print("1. View Stock Information")
    print("2. Buy Stocks")
    print("3. Sell Stocks")
    print("4. Check your Balance")
    print("5. View your Portfolio")
    print("6. Next Day(Updates stick prices)")
    print("7. Log Out")
    print("-------------------------------")

def add_current_price():
    with open('stonksdata.csv', 'r') as file:
        stocks_data = list(csv.reader(file))
        
        for stock in stocks_data[1:]:
            lowest_price = float(stock[1])
            highest_price = float(stock[2])
            current_price = random.uniform(lowest_price, highest_price)
            stock.append(str(round(current_price, 2)))
    
    with open('stonksdata.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(stocks_data)

def update_previous_prices():
    stocks_data = []
    print("Stock data is updated")
    with open('stonksdata.csv', 'r') as file:
        reader = csv.reader(file)
        stocks_data = list(reader)

    for stock in stocks_data[1:]:
        previous_price = float(stock[3])
        growth_percentage = round(random.uniform(-3.0, 3.0), 2)
        updated_price = round(previous_price * (1 + growth_percentage / 100), 2)
        stock[3] = str(updated_price)

    with open('stonksdata.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(stocks_data)

def trade_stock(stock_name, quantity, action, balance):
    user_stocks = []
    with open('user_stocks.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            user_stocks.append(row)
    stocks_data = []
    with open('stonksdata.csv', 'r') as file:
        reader = csv.reader(file)
        stocks_data = list(reader)

    for stock in stocks_data:
        if stock[0] == stock_name:
            current_price = float(stock[3])
            stock_info = None

            for stock_entry in user_stocks:
                if stock_entry[0] == stock_name:
                    stock_info = stock_entry
                    break

            if action == 'buy':
                total_cost = current_price * quantity
                if total_cost <= balance:
                    balance -= total_cost
                    if stock_info:
                        stock_info[1] = str(int(stock_info[1]) + quantity)
                    else:
                        user_stocks.append([stock_name, str(quantity), str(current_price)])
                    print("You bought", quantity, "shares of", stock_name, "at Rs.", current_price, "each.")
                    print("Total cost: Rs.", total_cost)
                else:
                    print("Insufficient funds. Unable to complete the transaction.")

            elif action == 'sell':
                if stock_info and int(stock_info[1]) >= quantity:
                    bought_price = float(stock_info[2])
                    total_gain = (current_price - bought_price) * quantity
                    balance += total_gain+ (bought_price* quantity)
                    stock_info[1] = str(int(stock_info[1]) - quantity)
                    print("You sold", quantity, "shares of", stock_name, "at Rs.", current_price, "each.")
                    print("Total gain: Rs.", total_gain)
                else:
                    print("Insufficient stock quantity. Unable to complete the transaction.")

            break

    file = open('user_stocks.csv', 'w', newline='')
    writer = csv.writer(file)
    writer.writerows(user_stocks)
    file.close()

    return balance

def display_stock_info():
    stocks_data = []

    with open('stonksdata.csv', 'r') as file:
        reader = csv.reader(file)
        stocks_data = list(reader)

    for stock in stocks_data[1:]:
        stock_name = stock[0]
        current_price = stock[3]
        growth_percentage = round(random.uniform(-3.0, 3.0), 2)
        print("Stock:", stock_name)
        print("Current Price: Rs.", current_price)
        print("Growth Percentage: ", growth_percentage, "%")
        print("-------------------------------")
def display_portfolio():
    user_stocks = []

    with open('user_stocks.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            user_stocks.append(row)

    if not user_stocks:
        print("Your portfolio is empty.")
        return

    total_value = 0

    print("---------- Portfolio ----------")
    for stock in user_stocks:
        if len(stock) < 3:
            print("Invalid stock entry:", stock)
            continue

        stock_name = stock[0]
        quantity = int(stock[1])
        bought_price = float(stock[2])

        stocks_data = []

        with open('stonksdata.csv', 'r') as file:
            reader = csv.reader(file)
            stocks_data = list(reader)

        for stock_data in stocks_data[1:]:
            if len(stock_data) < 4:
                print("Invalid stock data:", stock_data)
                continue

            if stock_data[0] == stock_name:
                current_price = float(stock_data[3])
                break
        else:
            print("Stock not found:", stock_name)
            continue

        current_value = current_price * quantity
        total_gain_loss = (current_price - bought_price) * quantity

        print("Stock:", stock_name)
        print("Quantity:", quantity)
        print("Bought Price: Rs.", bought_price)
        print("Current Price: Rs.", current_price)
        print("Current Value: Rs.", current_value)
        print("Gain/Loss: Rs.", total_gain_loss)
        print()

        total_value += current_value

    print("Total Portfolio Value: Rs.", total_value)
    print("-------------------------------")


def main():
    balance = 2500
    while True:
        show_login_menu()
        ch = int(input("Enter the number corresponding to your choice: "))

        if ch == 1:
            if login():
                break
        elif ch == 2:
            signup()

    while True:
        show_menu()
        choice = int(input("Enter the number corresponding to your choice: "))

        if choice == 1:
            add_current_price()
            display_stock_info()
        elif choice == 2:
            stock_name = input("Enter the stock name: ")
            quantity = int(input("Enter the quantity: "))
            balance = trade_stock(stock_name, quantity, 'buy', balance)
        elif choice == 3:
            stock_name = input("Enter the stock name: ")
            quantity = int(input("Enter the quantity: "))
            balance = trade_stock(stock_name, quantity, 'sell', balance)
        elif choice == 4:
            print("Balance: Rs.", balance)
        elif choice == 5:
            display_portfolio()
        elif choice == 6:
            update_previous_prices()
        elif choice == 7:
            print("Logged out successfully!")
            break
print("Welcome to the Virtual Stock Trading Game!")
print("In this game, you can buy and sell virtual stocks to earn profits.")
print("Instructions:")
print("- You start the game with a balance of Rs. 2500.")
print("- You can choose from various options:")
print("  1. Buy Stocks: Buy stocks of your choice.")
print("  2. Sell Stocks: Sell the stocks you own.")
print("  3. Check Balance: View your current balance.")
print("  4. View Stock Information: Get information about available stocks.")
print("  5. View Portfolio: See the stocks you currently own.")
print("  6. Next Day: Simulate the next trading day and update stock prices.")
print("  7. Log Out: Exit the game.")
main()
