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
  update = sheet.values().update(spreadsheetId=spreadsheet_id,
	range=range_,
	valueInputOption='USER_ENTERED',
	body={'values': values}).execute()

def getValuelist(range_):
	request = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_).execute()
	values = request.get("values", [])
	valuelist = []
	for i in range(len(values)):
		valuelist.append(values[i])
	return valuelist

def getValues(range_):
	request = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_).execute()
	values = request.get("values", [])
	return values

#I NEED TO STORE ALL VALUES IN LISTS TO MAKE UPLOADING THEM EASIER

samplestatlist = ["statement", 5, 8, "word"]
othersamplelist = ["cool word", 2, 1, "thing"]

class testclass:
	def __init__ (self, name, argument, number, word):
		self.name=name
		self.argument=argument
		self.number=number
		self.word=word

#sendUpdate('A9', [samplestatlist])
#sendUpdate('A2', [othersamplelist])
#allvalues = getValues('A1:D')
#row1 = allvalues[0]

#print(allvalues)

#aclass = testclass(row1[0],row1[1],row1[2],row1[3])
#for i in range(len(row1)):
#	print(row1[i])

#print(aclass.name)

