import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("testproject.json", scope)
client = gspread.authorize(credentials)
spreadsheet_id = '1HLvJU_aR3q9lZRqtfg0h7W03t_9GmGfvmhTESJ-1t18'

service = discovery.build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

def sendUpdate(range_, values):
	update = sheet.values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption='USER_ENTERED', body={'values': values}).execute()
	print("update sent of range", range_, "and values", values)

def getValues(range_):
	request = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_).execute()
	values = request.get("values", [])
	return values

sendUpdate('A1', [[1,2],[3,4]])
print(getValues('A1:B2')[0:2])
sendUpdate('A2', [[5]])
print(getValues('A1:B2')[0:2])
print(getValues('A1:B2')[0][0], "is a", type(getValues('A1:B2')[0][0]))
