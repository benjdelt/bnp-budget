import csv
import matplotlib.pyplot as plt
import numpy as np


# Constants

FILE_NAME = "./sample-data/BE12345678912345-20211129.csv"
HEADER_DATE = "Date d'exécution"
HEADER_AMOUNT = "Montant"


# Functions

def monthify(datestr):
    """Takes a string representing a date with DD/MM/YYYY format and returns a string containing the 3 letter
        abreviation of the month and the year (e.g.: Nov 2021)
    """
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"
    ]
    split_date = datestr.split("/")
    month = months[int(split_date[1]) - 1]
    return f"{month} {split_date[2]}"


def update_report(report, row):
    """Takes a report dictionary and a row of a CSV file and updates the report with the data from the row
    """
    monthified = monthify(row[HEADER_DATE])
    if monthified not in report:
        report[monthified] = {
            "expense_cents": 0,
            "income_cents": 0,
            "balance_cents": 0
        }
    operation_type = "expense_cents" if row[HEADER_AMOUNT][0] == "-" else "income_cents"
    report[monthified][operation_type] += int(float(row[HEADER_AMOUNT]) * 100)
    expenses = report[monthified]["expense_cents"]
    income = report[monthified]["income_cents"]
    report[monthified]["balance_cents"] = expenses + income
    return report


def find_current_quarter(datestr):
    """Takes a string representing a date with DD/MM/YYYY format and returns a string quarter and the year
        (e.g.: Q3 2021)
    """
    value = ""
    quarters = {
        "Q1": ["Jan", "Feb", "Mar"],
        "Q2": ["Apr", "May", "Jun"],
        "Q3": ["Jul", "Aug", "Sep"],
        "Q4": ["Oct", "Nov", "Dec"]
    }
    for quarter in quarters:
        if datestr[:3] in quarters[quarter]:
            value = quarter
    return f"{value} {datestr[3:]}"


def make_quaterly(report):
    """Takes a monthly report and returns a quarterly report"""
    quarterly = {}
    for line in report:
        current_quarter = find_current_quarter(line)
        if current_quarter not in quarterly:
            quarterly[current_quarter] = {
                "expense_cents": 0,
                "income_cents": 0,
                "balance_cents": 0
            }
        quarterly[current_quarter]["expense_cents"] += report[line]["expense_cents"]
        quarterly[current_quarter]["income_cents"] += report[line]["income_cents"]
        quarterly[current_quarter]["balance_cents"] += report[line]["balance_cents"]
    return quarterly


def format_amount(amount_cents):
    """Takes an int representing an amount in cents and returns a string of the amount in euros. Negative amounts are
        between parentheses.
    """
    amount = amount_cents / 100
    return f"({abs(amount):.2f})" if amount_cents < 0 else f"{amount:.2f}"


def print_report(report):
    """Format and prints a report dictionary to the stdout.
    """
    for line in report:
        income = format_amount(report[line]['income_cents'])
        expenses = format_amount(report[line]['expense_cents'])
        balance = format_amount(report[line]['balance_cents'])
        print(f"{line}\t\t\tinc: {income}\t\t\texp: {expenses}\t\t\tbal: {balance}")


# Execution

if __name__ == "__main__":
    with open(FILE_NAME, "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        report = {}
        for row in reader:
            update_report(report, row)
        print("Monthly Report:")
        print_report(report)
        print("")
        print("Quaterly Report:")
        print_report(make_quaterly(report))


        # Figures

        data_length = len(report)

        labels = [line for line in report]
        labels.reverse()
        monthly_expenses = [abs(report[line]["expense_cents"] / 100) for line in report]
        monthly_expenses.reverse()
        monthly_incomes = [abs(report[line]["income_cents"] / 100) for line in report]
        monthly_incomes.reverse()
        monthly_balances = [report[line]["balance_cents"] / 100 for line in report]
        monthly_balances.reverse()

        ind = np.arange(data_length)

        # Balances

        width = 0.75
        fig, ax = plt.subplots()

        p1 = ax.bar(labels, monthly_balances, width, color="mediumseagreen")

        ax.axhline(0, color='grey', linewidth=0.8)
        ax.set_xlabel('Month')
        ax.set_ylabel('Amount')
        ax.set_title('Balances')
        ax.set_xticks(ind, labels=labels)
        ax.bar_label(p1)

        plt.savefig('balances.png')

        # Income and Expenses

        fig2, bx = plt.subplots()
        width2 = 0.35
        rects1 = bx.bar(ind - width2 / 2, monthly_incomes, width2, label='Income', color="mediumseagreen")
        rects2 = bx.bar(ind + width2 / 2, monthly_expenses, width2, label='Expenses', color="salmon")

        bx.set_ylabel('Amount')
        bx.set_title('Income and Expenses')
        bx.set_xticks(ind, labels)
        bx.legend()

        bx.bar_label(rects1, padding=5)
        bx.bar_label(rects2, padding=5)

        fig2.tight_layout()

        plt.savefig('income-expenses.png')

        # Show all figures

        plt.show()
