from coffeecup import MENU, calculate_total, apply_discount

print("☕ Welcome to DevOps Coffee Shop ☕")
print("Available Coffees:")

for coffee, price in MENU.items():
    print(f"{coffee} - ₹{price}")

item = input("Enter coffee name: ").lower()
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount % (0 if none): "))

try:
    total = calculate_total(item, quantity)
    final_amount = apply_discount(total, discount)
    print(f"Total Bill: ₹{final_amount}")
except ValueError as e:
    print("Error:", e)