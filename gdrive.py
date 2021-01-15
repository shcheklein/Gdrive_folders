from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import pygsheets

gauth = GoogleAuth()
gc = pygsheets.authorize(client_secret='sheet_secret.json')
# Creates local webserver and auto handles authentication.
gauth.LocalWebserverAuth()

FOLDER_ID = "13Hbb2fVThUxyMRys_X_ovhzl4B9xLeLF"
SHEET_ID = "1_Zd58iYN0M_dAZipl52Db2YCYiL5rf3Do9N4m70iFOU"

sh = gc.open_by_key(SHEET_ID)
ws = sh.sheet1

# print(ws.get_values("A1","B3"))


col_remito= ws.get_col(1)
col_informe= ws.get_col(2)




# # Create GoogleDrive instance with authenticated GoogleAuth instance
# drive = GoogleDrive(gauth)

# # Auto-iterate through all files in the root folder.
# file_list = drive.ListFile({'q': f"'{FOLDER_ID}' in parents"}).GetList()
# print(file_list[0]["alternateLink"])
# print("-------------------------------------")
# for file1 in file_list:
#     print('title: %s, id: %s' % (file1['title'], file1['id']))
