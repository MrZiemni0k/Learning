MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1300,
    "milk": 1200,
    "coffee": 200,
    "money": 0
}
order = True

def ask_customer():
    
    while True:
        order = input("What would you like?"
                      " (espresso/cappuccino/latte) ").lower()
        if order == 'report':
            print(f"Water:  {resources['water']} ml")
            print(f"Milk:   {resources['milk']} ml")
            print(f"Coffee: {resources['coffee']} ml")
            print(f"Money:  ${resources['money']} ")
            return order
        elif order == 'off':
            order = False
            return order
        elif order not in MENU.keys():
            print("I am a machine. I do not understand. Please repeat.")
        else:
            return order

def check_resources(coffee_type):
    global resources
    trigger_stock = resources.copy()
    coffee_info = MENU[coffee_type]['ingredients']
    for x in coffee_info:
        trigger_stock[x] -= coffee_info[x]
        if coffee_info[x] >= resources[x]:
            print(f"Sorry there is not enough {x}. Money refunded.")
            return False
    print(f"Test {resources}")
    print(f"Test2 {trigger_stock}")
    resources = trigger_stock
    return True
    
def input_money():
    print("Please insert coins")
    quarters = int(input("How many quarters ($0.25)? "))
    dimes = int(input("How many dimes ($0.1)? "))
    nickles = int(input("How many nickles ($0.05)? "))
    cents = int(input("How many cents? ($0.01)"))
    amount = (0.25*quarters +
              0.10*dimes +
              0.05*nickles +
              0.01*cents
              )
    print("Total paid ${:.2f}".format(amount))
    return amount
             
while order:
    order = ask_customer()
    if order not in ['report',False]:
        income = input_money()
        if income > MENU[order]["cost"]:
            change = income - MENU[order]["cost"]
            income = MENU[order]["cost"]
            if change:
                print("Here's your change: ${:.2f}".format(change))
            if check_resources(order):
                resources["money"] += income
        else:
            print("Sorry that's not enough money. Money refunded.")
            