from datetime import datetime

from src import CATEGORIES, DATE_FORMAT, PLOTS
from src.logger import logger


def get_date(message):
    input_date = input(message)

    try:
        date = datetime.strptime(input_date, DATE_FORMAT)
        return date.strftime(DATE_FORMAT)
    except ValueError:
        logger.error(f"Invalid date format: {input_date}")
        return get_date()
    
def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return amount
    except ValueError as e:
        print(e)
        logger.error(f"Invalid amount format: {e.message}")
        return get_amount()


def get_category():
    category = input("Enter the category (income or expense): ").lower()
    if category in CATEGORIES:
        return category

    logger.error(f"Invalid category value. Please enter Income or Expense.")
    return get_category()


def get_description():
    return input("Enter a description (optional): ")

def get_type_plot():
    type = input("Enter the plot type (Pie or Line): ").lower()
    if type in PLOTS:
        return type

    logger.error(f"Invalid type value. Please enter one of these values {PLOTS}")
    return get_type_plot()