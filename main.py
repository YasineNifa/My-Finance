from src.helper import get_date, get_type_plot
from src.logger import logger
from src.transaction import add, get_transactions
from src.plotter import pie_transaction, line_transactions


FUNCTIONS = {
    "line": line_transactions,
    "pie": pie_transaction,
}

def main():
    while 1:
        print("\n1. New Transaction")
        print("2. View Transaction within a date range")
        print("3. Exit")
        Input = input("Enter your choice (1-3): ")

        if Input == "1":
            add()

        elif Input == "2":
            start_date = get_date("Enter the start date in this format dd-mm-yyyy: ")
            end_date = get_date("Enter the end date in this format dd-mm-yyyy: ")
            df = get_transactions(start_date, end_date)
            if input("Do you want to see a plot? (y/n) ").lower() == "y":
                type = get_type_plot()
                print(f"Type: {type}")
                FUNCTIONS[type](df)

        elif Input == "3":
            print("Exit the application")
            break

        else:
            logger.warning("Invalid input")


if __name__ == "__main__":
    main()