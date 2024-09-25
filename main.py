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
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ")
        if choice == "off":
            quit()
        if choice == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounce(s)")
        elif choice == "small" or choice == "medium" or choice == "large":
            sandwich = recipes[choice]

            # I wanted to display the cost of the sandwich being sandwich_maker_instanceed
            print(f"The {choice} sandwich is ${recipes[choice]['cost']}")

            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()