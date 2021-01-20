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


class Sheet():
    def __init__(self,folder_inf=FOLDER_INFORME_ID,folder_rev=FOLDER_REVELAMIENTO_ID,
                 sheet_id=SHEET_ID,remito=REMITO_COL,informe=INFORME_COL,
                 revelamiento=REVELEMIENTO_COL) -> None:
        
        #Inicicializando Variables de Settings
        self.FOLDER_INFORME_ID = folder_inf
        self.FOLDER_REVELAMIENTO_ID = folder_rev
        self.SHEET_ID = sheet_id
        self.REMITO_COL = remito
        self.INFORME_COL = informe
        self.REVELEMIENTO_COL = revelamiento
        
        # Declarando Variables de trabajo
        self.informes = []
        self.revelamientos = []
        self.sh = []
        self.ws = []
        
        self.col_remito = []
        self.col_informe = []
        self.col_revelamiento = []
        
        # Autenticacion
        self.gauth = GoogleAuth()
        self.gc = pygsheets.authorize(client_secret='sheet_secret.json')
        self.gauth.LocalWebserverAuth()

    # Obtener valores de trabajos actuales
    def get_values(self):
        
        self.informes = self.search_folder(self.FOLDER_INFORME_ID)
        self.revelamientos = self.search_folder(self.FOLDER_REVELAMIENTO_ID)
        self.sh = self.gc.open_by_key(self.SHEET_ID)
        self.ws = self.sh.sheet1
        
        self.col_remito = self.ws.get_col(REMITO_COL)
        self.col_informe = self.ws.get_col(INFORME_COL,value_render="FORMULA")
        self.col_revelamiento = self.ws.get_col(REVELEMIENTO_COL,value_render="FORMULA")
   
    # Requiere ID de una carpeta, retorna lista de archivos y/o sub carpetas
    def search_folder(self,folderid: str):

        drive = GoogleDrive(self.gauth)
        file_list = drive.ListFile({'q': f"'{folderid}' in parents"}).GetList()
        return file_list
    
    # Iterar por cada uno de los informes, revisar en la columna remito y escribir los hiperlinks
    # No retorna nada
    def escribir_informes(self,folder_list,col_objetivo, col_lista):
        
        for folder_element in folder_list:
            if folder_element["title"] in self.col_remito:
                index = self.col_remito.index(folder_element["title"])
                if not col_lista[index]:
                    link = folder_element["alternateLink"]
                    title = folder_element["title"]
                    col_lista[index] = f'=HYPERLINK("{link}";"{title}")'

        self.ws.update_col(col_objetivo, col_lista)
        
        
if __name__ == "__main__":
    
    sheet = Sheet()
    sheet.get_values()
    sheet.escribir_informes(sheet.informes,sheet.INFORME_COL,sheet.col_informe)
    sheet.escribir_informes(sheet.revelamientos,sheet.REVELEMIENTO_COL,sheet.col_revelamiento)
