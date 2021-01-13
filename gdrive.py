from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()

# Creates local webserver and auto handles authentication.
gauth.LocalWebserverAuth()

FOLDER_ID = "13Hbb2fVThUxyMRys_X_ovhzl4B9xLeLF"
SHEET_ID = ""


# Create GoogleDrive instance with authenticated GoogleAuth instance
drive = GoogleDrive(gauth)

# Auto-iterate through all files in the root folder.
file_list = drive.ListFile({'q': f"'{FOLDER_ID}' in parents"}).GetList()
print(file_list[0]["title"])
print("-------------------------------------")
for file1 in file_list:
    print('title: %s, id: %s' % (file1['title'], file1['id']))
