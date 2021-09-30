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
    Get car sales input from user.
    Run a while loop ro collect a valid string of data from user
    via the terminal, a string of 6 numbers seperated by commas.
    The loope will repeat request, until valid.
    """
    while True:
        print("Please enter car sales data for each day of sales\n")
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
        print(f"Invalid information: {e}, please try again.\n")
        return False

    return True


def update_sales_worksheet(data):
    """
    Update worksheet for car sales, add new row when the data is provided.
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Car sales worksheet updated successfully.\n")


def update_unsold_worksheet(data):
    """
    Update unsold cars worksheet, add new row with provided data.
    """
    print("Updating unsold worksheet...\n")
    unsold_worksheet = SHEET.worksheet("unsold")
    unsold_worksheet.append_row(data)
    print("Car sales worksheet updated successfully.\n")


def calculate_unsold_data(sales_row):
    """
    Compare sales with car stock and calulate the unsold cars.
    The unsold is defined as the sales data subtracted from stock:
    -Positive unsold indicates, cars in stock.
    -Negative unsold indicates cars that had to be ordered in.
    """
    print("Calculating unsold cars each day...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    unsold_data = []
    for stock, sales in zip(stock_row, sales_row):
        unsold = int(stock) - sales
        unsold_data.append(unsold)
        
    return unsold_data


def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    calculate_unsold_data(sales_data)
    new_unsold_data = calculate_unsold_data(sales_data)
    print(new_unsold_data)


print("Welcome to Car Sales Data Automation")
main()
