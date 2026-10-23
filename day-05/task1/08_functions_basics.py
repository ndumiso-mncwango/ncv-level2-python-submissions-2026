def place_order(item):
    print(f"Order placed: your order is {item}")
def calculate_total(item):
    base_price = 25.5
    totalPrice = (base_price + len(item)) * 1.15
    return totalPrice

def get_order():
    print("Preparing order")
    return "Collect your order"

myFood = input("What would you like: ")

place_order(myFood)

print(get_order())

orderTotal = calculate_total(myFood)
print(f"Your order costs: R{orderTotal:.2f}")