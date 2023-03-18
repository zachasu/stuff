import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

#designate the API's that will be used and take the credentials from a .json file
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("testproject.json", scope)
client = gspread.authorize(credentials)

#create a new google sheet and share it with a google account
#sheet = client.create("NewDatabase")
#sheet.share('zue747@gmail.com', perm_type='user', role='writer')

spreadsheet_id = '1HLvJU_aR3q9lZRqtfg0h7W03t_9GmGfvmhTESJ-1t18'
range_ = 'A1:B2'

#set up a 'client for interacting with a google API'
service = discovery.build('sheets', 'v4', credentials=credentials)

#need to research what this does
sheet = service.spreadsheets()

#define a spreadsheet_id, range, and values to send, as a .update, to a google sheet
update = sheet.values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption='USER_ENTERED', body={'values': [[1,2], [3,4]]})

#send an .update to a google sheet to change a range to a set of values
update_response = update.execute()

#define a spreadsheet_id and a range to send, as a .get, to a google sheet
request = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_)

#send a .get to google sheet to get a ValueRange object
response = request.execute()

#isolate the Value list in the recieved ValueRange object
values = response.get("values", [])

#values are stored as strings in a list
row1 = values[0]
row2 = values[1]

print(response)
print("int(value):", int(row1[1]), type(row1[1]))
for row in values:
	print(row)
