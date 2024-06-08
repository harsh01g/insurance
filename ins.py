import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('caramel-feat-425816-e3-094da0a283b1.json', scope)
client = gspread.authorize(creds)
gsheet = client.open("Policy").sheet1

number_from_gsheet = float(gsheet.cell(1, 1).value)
net_premium = 2895421.00

if net_premium > number_from_gsheet:
    print("The Net Premium is greater than the number in the Google Sheet.")
elif net_premium < number_from_gsheet:
    print("The Net Premium is lesser than the number in the Google Sheet.")
else:
    print("The Net Premium is equal to the number in the Google Sheet.")

