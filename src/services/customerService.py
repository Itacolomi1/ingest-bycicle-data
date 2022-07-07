import pandas as pd
import os
from src.services.settingsService import SettingsService
from src.services.folderService import FolderService
from src.DAO.CustomerDAO import CustomerDAO
from src.DAO.MysqlDatabase import MysqlDatabase

class Customer():

    def __init__(self):
        configuration = SettingsService()
        self._bucket = configuration.properties['bucketPath']  
        self._name = 'Sales.Customer.csv'
        self._folderService = FolderService(self._name)
       

    def load(self):
        try: 
           
            if(self._folderService.findFile(self._bucket + '/toDo/')):

                print('--------CARREGAR CUSTOMER----------') 
                path = self._bucket + '/toDo/' + self._name
                df = pd.read_csv(path, sep=';')         
                # print(df.columns)
                print(df.info())
                self._folderService.moveToDoing()

                mysql = MysqlDatabase()
                connection = mysql.connect()

                for index, row in df.iterrows():
                    # print(row)                
                    product = CustomerDAO(row,connection)
                    product.insert()
                    
                
                self._folderService.moveToDone()
                
                   
            else:
                print('Não existe arquivo Sale.Customer para ser processado')

        except Exception as ex:
            print('Erro na Leitura de Product')
            print(ex)
        finally:
            if (connection != False and connection.is_connected()):
                connection.close()