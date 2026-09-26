# Day 2: Lists and dictionaries — portfolio calculator

# 1. Build a list called portfolio holding 3 positions
portfolio = [
    {"coin": "Bitcoin", "buy_price": 30000, "quantity": 1, "current_price": 35000},
    {"coin": "Ethereum", "buy_price": 2000, "quantity": 5, "current_price": 2500},
    {"coin": "Cardano", "buy_price": 1.2, "quantity": 1000, "current_price": 1.5}
]
# 2. Make each position a dictionary with the same keys as Day 1:
#    coin, buy_price, quantity, current_price
# 3. Print the second coin's name
print(portfolio[1]["coin"])

# 4. Print the first coin's quantity
print(portfolio[0]["quantity"])

# 5. Calculate profit/loss in dollars for position 1
profit_loss_1 = (portfolio[0]["current_price"] - portfolio[0]["buy_price"]) * portfolio[0]["quantity"]

# 6. Do the same for position 2
profit_loss_2 = (portfolio[1]["current_price"] - portfolio[1]["buy_price"]) * portfolio[1]["quantity"]

# 7. Do the same for position 3
profit_loss_3 = (portfolio[2]["current_price"] - portfolio[2]["buy_price"]) * portfolio[2]["quantity"]

# 8. Add the three results to get total portfolio profit/loss
total_profit_loss = profit_loss_1 + profit_loss_2 + profit_loss_3

# 9. Print each coin with its profit/loss, then the total
print(f"{portfolio[0]['coin']}: ${profit_loss_1:.2f}")
print(f"{portfolio[1]['coin']}: ${profit_loss_2:.2f}")
print(f"{portfolio[2]['coin']}: ${profit_loss_3:.2f}")
print(f"Total: ${total_profit_loss:.2f}")