# 1. Ask for the coin name
coin = input("Coin name: ")
# 2. Ask for the buy price
buy_price = float(input("buy price: ")) 
# 3. Ask for the quantity
quantity = float(input("quantity: "))
# 4. Ask for the current price
current_price = float(input("current price: "))

# 5. Calculate cost basis
calculated_cost_basis = buy_price * quantity
# 6. Calculate current value
calculated_current_value = current_price * quantity
# 7. Calculate profit/loss in dollars
calculated_profit_loss_dollars = calculated_current_value - calculated_cost_basis

# 8. Calculate profit/loss as a percentage
calculated_profit_loss_percentage = (calculated_profit_loss_dollars / calculated_cost_basis) * 100

# 9. Print the results
print(f"Coin: {coin}")
print(f"Cost basis: ${calculated_cost_basis:.2f}")
print(f"Current value: ${calculated_current_value:.2f}")
print(f"Profit/Loss: ${calculated_profit_loss_dollars:.2f}")
print(f"Profit/Loss Percentage: {calculated_profit_loss_percentage:.2f}%")