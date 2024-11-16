import random
import matplotlib.pyplot as plt

# Constants
AVERAGE_PRICE = 600
PRICE_DROP_THRESHOLD = 0.20
CRITICAL_STOCK_LEVEL = 10
DEFAULT_ORDER_QUANTITY = 10
STOCK_REPLENISH_QUANTITY = 15

# Initial values
current_stock = 20
prices = []
stock_levels = []

# Simulate price function
def simulate_price():
    return random.randint(AVERAGE_PRICE - 100, AVERAGE_PRICE + 100)

# Update stock based on order
def update_stock(order_quantity):
    global current_stock
    current_stock += order_quantity

# Make decision on ordering
def make_decision(current_price):
    global current_stock
    order_quantity = 0

    if current_price <= AVERAGE_PRICE * (1 - PRICE_DROP_THRESHOLD) and current_stock > CRITICAL_STOCK_LEVEL:
        order_quantity = STOCK_REPLENISH_QUANTITY
    elif current_stock < CRITICAL_STOCK_LEVEL:
        order_quantity = DEFAULT_ORDER_QUANTITY

    update_stock(order_quantity)
    return order_quantity

# Run the agent over multiple steps
def run_agent(simulation_steps=30):
    for _ in range(simulation_steps):
        current_price = simulate_price()
        order_quantity = make_decision(current_price)

        prices.append(current_price)
        stock_levels.append(current_stock)

        print(f"Price: {current_price} BDT, Stock: {current_stock} units, Ordered: {order_quantity} units")

# Plot the results
def plot_results():
    plt.figure(figsize=(10, 5))

    plt.subplot(2, 1, 1)
    plt.plot(prices, color='blue')
    plt.title('Smartphone Price Over Time')
    plt.ylabel('Price (BDT)')

    plt.subplot(2, 1, 2)
    plt.plot(stock_levels, color='green')
    plt.title('Smartphone Stock Levels Over Time')
    plt.ylabel('Stock Level (units)')
    plt.xlabel('Time Step')

    plt.tight_layout()
    plt.show()

# Run and visualize
run_agent()
plot_results()