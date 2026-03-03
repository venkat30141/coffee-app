MENU = {
    "espresso": 100,
    "latte": 150,
    "cappuccino": 180,
    "americano": 120
}

def get_price(item):
    if item not in MENU:
        raise ValueError("Coffee not available")
    return MENU[item]

def calculate_total(item, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    
    price = get_price(item)
    return price * quantity

def apply_discount(total, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid discount")
    
    return total - (total * discount_percent / 100)