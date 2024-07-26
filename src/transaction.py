import csv
from datetime import datetime
import pandas as pd

from src import COLUMNS, CSV_FILE, DATE_FORMAT
from src.helper import get_amount, get_category, get_date, get_description
from src.logger import logger


def read_data():
    try:
        return pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        raise Exception("File not found")
        

def add_transaction(date, amount, category, description) -> None:
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS)
        writer.writerow({
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        })

    logger.info("Transactions added")

def add():
    date = get_date(f"Enter the date in this format {DATE_FORMAT}: ")
    amount = get_amount()
    category = get_category()
    description = get_description()
    add_transaction(date, amount, category, description)

def get_transactions(start_date, end_date):
    dataframe = read_data()
    dataframe["date"] = pd.to_datetime(
        dataframe["date"],
        errors="coerce",
        format=DATE_FORMAT,
    )

    start_date = datetime.strptime(start_date, DATE_FORMAT)
    end_date = datetime.strptime(end_date, DATE_FORMAT)
    
    filtered_data = dataframe.loc[
        (dataframe["date"] >= start_date) & (dataframe["date"] <= end_date)
    ]
    if filtered_data.empty:
        logger.debug("No transactions!")

    else:
        logger.info(f"The transactions made are : \n {filtered_data}")

    return filtered_data

def get_incomes(dataframe):
    return dataframe.loc[dataframe["category"] == "Income"]
    
def get_expenses(dataframe):
    return dataframe.loc[dataframe["category"] == "Expense"]

def get_invests(dataframe):
    return dataframe.loc[dataframe["category"] == "Invest"]

def get_saves(dataframe):
    return dataframe.loc[dataframe["category"] == "Save"]

