import gspread
from google.oauth2.service_account import Credentials

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = Credentials.from_service_account_file('caramel-feat-425816-e3-094da0a283b1.json', scopes=scope)

# Authorize the clientsheet
client = gspread.authorize(creds)

# Get the instance of the Spreadsheet
sheet = client.open('Policy')

# Get the first sheet of the Spreadsheet
worksheet = sheet.get_worksheet(0)

# Get the value from the cell (assuming the number is in cell A1)
sheet_value = worksheet.cell(1, 1).value
sheet_value = float(sheet_value.replace(',', ''))

# The net premium from your document
net_premium = 2895421.00

# Compare the values
if net_premium > sheet_value:
    print("Net Premium is greater than the value in the Google Sheet.")
elif net_premium < sheet_value:
    print("Net Premium is less than the value in the Google Sheet.")
else:
    print("Net Premium is equal to the value in the Google Sheet.")
