import matplotlib.pyplot as plt
import pandas as pd

from src import CATEGORIES
from src.transaction import get_expenses, get_incomes, get_invests, get_saves


def line_transactions(dataframe):

    incomes = get_incomes(dataframe)
    expenses = get_expenses(dataframe)
    numeric_incomes_columns = incomes.select_dtypes(include='number').columns
    numeric_expenses_columns = expenses.select_dtypes(include='number').columns

    incomes_df = incomes.groupby("date")[numeric_incomes_columns].sum().reset_index()
    descriptions = incomes.groupby("date")['description'].apply(', '.join).reset_index()
    incomes = pd.merge(incomes_df, descriptions, on='date')
    expenses_df = expenses.groupby("date")[numeric_expenses_columns].sum().reset_index()
    descriptions = expenses.groupby("date")['description'].apply(', '.join).reset_index()
    expenses = pd.merge(expenses_df, descriptions, on='date')

    plt.figure(figsize=(10, 5))
    plt.plot(incomes["date"], incomes["amount"], label="Income", color="g")
    plt.plot(expenses["date"], expenses["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()


def pie_transaction(dataframe):
    incomes_df = get_incomes(dataframe)
    expenses_df = get_expenses(dataframe)
    invests_df = get_invests(dataframe)
    saves_df = get_saves(dataframe)

    incomes = incomes_df["amount"].sum()
    expenses = expenses_df["amount"].sum()
    invests = invests_df["amount"].sum()
    saves = saves_df["amount"].sum()

    labels = CATEGORIES
    sizes = [incomes, expenses, invests, saves]

    plt.figure(figsize=(10, 5))
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)
    plt.show()
