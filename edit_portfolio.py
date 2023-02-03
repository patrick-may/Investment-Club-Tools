import json
def create_stock():
    print("Enter Stock Name:")
    name = input()
    print("Enter Stock Ticker:")
    tick = input()
    print("Enter Date of Stock purchase:")
    purchase_date = input()
    print("Enter Stock Purchase Price:")
    purchase_price = float(input())
    print("Enter Number of Corporate Shares: ")
    corp_shares = int(input())
    print("Enter Number of Main Shares: ")
    main_shares = int(input())

    new_stocks = {
        "name": name,
        "ticker": tick,
        "purchase date": purchase_date,
        "purchase price": purchase_price,
        "corporate shares": corp_shares,
        "main shares": main_shares
    }
    serialized_stock = json.dumps(new_stocks, indent=4)

    with open("jenny_portfolio.json", "a") as outfile:
        outfile.write(serialized_stock)
    
def edit_stock():
    pass

def remove_stock():
    pass

def main():
    action_dict = {"1": create_stock, "2": edit_stock, "3" : remove_stock}
    s = """
    Welcome to Porfolio editor. What action would you like to take?\n
    (1) : Input A Stock\n
    (2) : Not Currently Working -- Edit Stock i.e. trim, add, change, etc.\n
    (3) : Not Currently Working -- Remove a Stock """
    action = "1"
    while action in action_dict:
        print(s)
        
        action = input()
        print("your action is", action)

        action_dict[action]()
    
    
if __name__ == "__main__":
    main()