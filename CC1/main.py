from color import Color, Fore   # Import Color from color.py

from expense_sharing_app import ExpenseSharingApp

if __name__ == "__main__":
    print(Fore.BLUE + Color.BOLD + Color.UNDERLINE + "\n\t\t\t\t\t Expense Tracker App\n" + Color.END + Fore.RESET)

    app = ExpenseSharingApp()

    # Adding Users (Roommates in our case)
    app.get_roommates()

    # Adding and Splitting Bills among Roommates
    total_amount = float(input(Fore.LIGHTMAGENTA_EX + "\nEnter Total Bill Amount: " + Fore.RESET))
    expenses = app.split_bills(total_amount)

    # Tracking Paid & Not Paid Persons
    app.track_payments(expenses)
