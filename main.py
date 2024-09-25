import data
import sandwich_maker
import cashier
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()




def main():
    ###  write the rest of the codes ###
    order = SandwichMachine(resources)
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ")
        if choice == "off":
            quit()
        if choice == "report":
            print(f"Bread: {order.machine_resources['bread']} slice(s)")
            print(f"Ham: {order.machine_resources['ham']} slice(s)")
            print(f"Cheese: {order.machine_resources['cheese']} ounce(s)")
        elif choice == "small" or choice == "medium" or choice == "large":
            sandwich = recipes[choice]

            # I wanted to display the cost of the sandwich being ordered
            print(f"The {choice} sandwich is ${recipes[choice]['cost']}")

            if order.check_resources(sandwich["ingredients"]):
                payment = order.process_coins()
                if order.transaction_result(payment, sandwich["cost"]):
                    order.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()