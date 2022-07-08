import pandas as pd
import os
from src.services.settingsService import SettingsService
from src.services.folderService import FolderService
from src.DAO.SalesOrderDetailDAO import SalesOrderDetailDAO
from src.DAO.MysqlDatabase import MysqlDatabase

class SalesOrderDetail():

    def __init__(self):
        configuration = SettingsService()
        self._bucket = configuration.properties['bucketPath']  
        self._name = 'Sales.SalesOrderDetail.csv'
        self._folderService = FolderService(self._name)
       

    def load(self):
        try: 
           
            if(self._folderService.findFile(self._bucket + '/toDo/')):

                print('--------CARREGAR SALES ORDER DETAIL---------') 
                path = self._bucket + '/toDo/' + self._name
                df = pd.read_csv(path, sep=';')         
                # print(df.columns)
                print(df.info())
                self._folderService.moveToDoing()

                mysql = MysqlDatabase()
                connection = mysql.connect()

                for index, row in df.iterrows():
                    # print(row)                                
                    salesOrder = SalesOrderDetailDAO(row,connection)
                    salesOrder.insert()
                  
                    
                    
                    
                
                self._folderService.moveToDone()
                
                   
            else:
                print(f'Não existe arquivo {self._name} para ser processado')

        except Exception as ex:
            print('Erro na Leitura de salesOrder')
            print(ex)
        finally:
            if (connection != False and connection.is_connected()):
                connection.close()