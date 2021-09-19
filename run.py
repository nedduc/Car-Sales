import gspread
from google.oauth2.service_account import Credentials

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
    Get car sales input from user
    """
    while True:
        print("Please enter car sales data from the last day of sales")
        print("Data should be six numbers, seperated by commas.")
        print("Example: 10,20,30,40,50,60\n")

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
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


data = get_sales_data()
