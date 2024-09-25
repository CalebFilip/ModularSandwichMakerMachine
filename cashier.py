class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        return (int(input("How many whole dollars? ")) * 1 +
                int(input("How many half dollars? ")) * .5 +
                int(input("How many quarters? ")) * .25 +
                int(input("How many nickles? ")) * .05)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            if cost - coins == 0:
                return True
            else:
                print(f"Your change is ${coins - cost}")
                return True
        else:
            print(f"Insufficient funds.")
            return False