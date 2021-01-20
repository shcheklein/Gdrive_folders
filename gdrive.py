from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import pygsheets

# Autenticacionn.

gauth = GoogleAuth()
gc = pygsheets.authorize(client_secret='sheet_secret.json')
gauth.LocalWebserverAuth()

#Settings 

FOLDER_INFORME_ID = "13Hbb2fVThUxyMRys_X_ovhzl4B9xLeLF"
FOLDER_REVELAMIENTO_ID= "1TVVfjVodkXwgv_pTq3GoOfaBtrj0iahp"
SHEET_ID = "1_Zd58iYN0M_dAZipl52Db2YCYiL5rf3Do9N4m70iFOU"

REMITO_COL = 1
INFORME_COL = 2
REVELEMIENTO_COL = 3

##################################################


# Requiere ID de una carpeta, retorna lista de archivos y/o sub carpetas
def search_folder(folderid: str):

    drive = GoogleDrive(gauth)
    file_list = drive.ListFile({'q': f"'{folderid}' in parents"}).GetList()
    return file_list

# Iterar por cada uno de los informes, revisar en la columna remito y escribir los hiperlinks
# No retorna nada
def escribir_informes(folder_list,col_objetivo, col_lista):
    for folder_element in folder_list:
        if folder_element["title"] in col_remito:
            index = col_remito.index(folder_element["title"])
            if not col_lista[index]:
                link = folder_element["alternateLink"]
                title = folder_element["title"]
                col_lista[index] = f'=HYPERLINK("{link}";"{title}")'

    ws.update_col(col_objetivo, col_lista)


# Inicializando valores
    informes = search_folder(FOLDER_INFORME_ID)
    revelamientos = search_folder(FOLDER_REVELAMIENTO_ID)
    sh = gc.open_by_key(SHEET_ID)
    ws = sh.sheet1

col_remito = ws.get_col(REMITO_COL)
col_informe = ws.get_col(INFORME_COL,value_render="FORMULA")
col_revelamiento = ws.get_col(REVELEMIENTO_COL,value_render="FORMULA")

escribir_informes(informes,INFORME_COL, col_informe)
escribir_informes(revelamientos, REVELEMIENTO_COL,col_revelamiento)
