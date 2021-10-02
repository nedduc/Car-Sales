import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('CREDS.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('car-sales')


def get_sales_data():
    """
    Get car sales input from user.
    Run a while loop ro collect a valid string of data from user
    via the terminal, a string of 6 numbers seperated by commas.
    The loope will repeat request, until valid.
    """
    while True:
        print("Please enter car sales data for each day of sales\n")
        print("Data should be six numbers, seperated by commas.")
        print("Example: 5,10,15,20,25,30\n")

        data_str = input("Enter your car sales here: ")

        sales_data = data_str.split(",")

        if check_data(sales_data):
            print("Your car sales data is valid!")
            break

    return sales_data


def check_data(values):
    """
    Inside the try statment, converts all strings values to intergers.
    Raise ValueError is strings can not be converted into intergers,
    or if there is not exactly 6 values entered.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid information: {e}, please try again.\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Receives a list of numbers to be inserted into worksheet
    update the correct worksheet with data inserted
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheeet_to_update = SHEET.worksheet(worksheet)
    worksheeet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def calculate_unsold_data(sales_row):
    """
    Stock minus car sales equals unsold cars:
    -Positive indicates, cars in stock.
    -Negative indicates cars to pre-ordered in.
    """
    print("Calculating unsold cars each day...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    unsold_data = []
    for stock, sales in zip(stock_row, sales_row):
        unsold = int(stock) - sales
        unsold_data.append(unsold)

    return unsold_data


def get_last_5_car_entries_sales():
    """
    Data list from last 5 entries of car sales on each model
    """
    sales = SHEET.worksheet("sales")
    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])

    return columns


def calculate_stock_data(data):
    """
    what needs to be ordered
    """
    print("Replenish stock ...\n")
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        bought = sum(int_column) / len(int_column)
        stock_num = bought * 1
        new_stock_data.append(round(stock_num))

    return new_stock_data


def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_unsold_data = calculate_unsold_data(sales_data)
    update_worksheet(new_unsold_data, "unsold")
    sales_columns = get_last_5_car_entries_sales()
    stock_data = calculate_stock_data(sales_columns)
    print(stock_data)


person = input("Enter your name: ")

pprint("Hello " + person + " this is your Car Sales Data Automation")
main()
