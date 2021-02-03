from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import pygsheets
from api.models import Config

# # Autenticacionn.

# gauth = GoogleAuth()
# gc = pygsheets.authorize(client_secret='sheet_secret.json')
# gauth.LocalWebserverAuth()
# gauth.CommandLineAuth()

#Settings 


#FOLDER_INFORME_ID = "1zrxd0yR5pKrufqgZsddqXx_Ev2sejgMj"
FOLDER_INFORME_ID = Config.folder_informe_id
#FOLDER_REVELAMIENTO_ID = "1sOvDaGAQvjY9TwlXW4VBQtToz2d_somv"
FOLDER_REVELAMIENTO_ID = Config.folder_relevamiento_id
SHEET_ID = Config.sheet_id
#SHEET_ID = "1pw6ElLByNNRgLVvc9WwzVESsPLKdJqVBBDpg_eE4nBQ"

REMITO_COL = Config.remito_col
INFORME_COL = Config.informe_col
REVELEMIENTO_COL = Config.relevamientos_col


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
        self.gauth.CommandLineAuth()

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
            element = folder_element['title'].split('.', 1)
            if element[0] in self.col_remito:
                index = self.col_remito.index(element[0])
                if not col_lista[index]:
                    link = folder_element["alternateLink"]
                    title = folder_element["title"]
                    col_lista[index] = f'=HYPERLINK("{link}";"{title}")'

        self.ws.update_col(col_objetivo, col_lista)
        

def run():
    
    sheet = Sheet()
    sheet.get_values()
    sheet.escribir_informes(sheet.informes,sheet.INFORME_COL,sheet.col_informe)
    sheet.escribir_informes(sheet.revelamientos,sheet.REVELEMIENTO_COL,sheet.col_revelamiento)
