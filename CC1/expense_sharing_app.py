from color import Color, Fore

class ExpenseSharingApp:
    def __init__(self) -> None:
        self.roommates = []

    def get_roommates(self) -> None:
        num = int(input(Fore.LIGHTMAGENTA_EX + "Enter number of roommates: " + Fore.RESET))
        for i in range(1, num + 1):
            self.roommates.append(input(f"Enter roommate - {i} Name: ").capitalize())

    def show_expenses(self, expenses: dict) -> None:
        max_name_length = max(len(name) for name in self.roommates)
        max_amount_length = len("Amount to be Paid")

        print(Fore.LIGHTYELLOW_EX + Color.UNDERLINE + "\nSplitted Amount Bill" + Color.END + Fore.RESET)
        
        print(f"\n\t {'Name':<{max_name_length}} \t\t {'Amount to be Paid':<{max_name_length}}")
        print("\t" + "-" * (max_name_length + max_amount_length + 20))
        for roommate, amount in expenses.items():
            print(f"\t {roommate:<{max_name_length}} \t\t ₹ {amount:<{max_name_length}}")

    def split_bills(self, total_amount: float) -> dict:
        if total_amount <= 0:
            exit(Fore.RED + "Exited with code 0: Amount Can't be Negative" + Fore.RESET)

        amount_per_person = total_amount / len(self.roommates)
        amount_per_person = round(amount_per_person, 2)

        expenses = {roommate: amount_per_person for roommate in self.roommates}
        return expenses

    def track_payments(self, expenses: dict) -> None:
        paid_list = []

        while True:
            paid_name = input(Fore.LIGHTMAGENTA_EX + "\nPress 0 to Exit or Enter your name if you paid: " + Fore.RESET).capitalize()

            if paid_name == '0':
                break

            if paid_name not in self.roommates:
                print(Fore.RED + "Invalid User Name!!!" + Fore.RESET)
            else:
                paid_list.append(paid_name)

            if sorted(self.roommates) == sorted(paid_list):
                break

        unpaid_list = list(set(self.roommates) - set(paid_list))
        expenses = {roommate: expenses[roommate] for roommate in unpaid_list}

        self.show_expenses(expenses)
