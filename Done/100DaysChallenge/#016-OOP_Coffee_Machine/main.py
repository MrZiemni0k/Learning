from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

_menu = Menu()
my_machine = CoffeeMaker()
my_money = MoneyMachine()
while True:


    order = input(f"What would you like? {_menu.get_items()} ").lower()
    
    if order == 'report':
       my_machine.report() 
       my_money.report()
    elif order == 'off':
        break
    elif order not in _menu.get_items():
        print("Incorect input. This cute coffee machine does not understand")
    else:
        drink = _menu.find_drink(order)
        if my_money.make_payment(drink.cost):
            if my_machine.is_resource_sufficient(drink):
                my_machine.make_coffee(drink)
            else:
                print(f"Sorry, we are out of stock. Money refunded.")
        else:
            print("Sorry that's not enough money. Money refunded.")
 