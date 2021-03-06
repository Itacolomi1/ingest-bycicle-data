import pandas as pd
from src.services.settingsService import SettingsService
from src.services.folderService import FolderService
from src.DAO.PersonDAO import PersonDAO
from src.DAO.MysqlDatabase import MysqlDatabase

class Person():

    def __init__(self):
        configuration = SettingsService()
        self._bucket = configuration.properties['bucketPath']  
        self._name = 'Person.Person.csv'
        self._folderService = FolderService(self._name)
       

    def load(self):
        try: 

            if(self._folderService.findFile(self._bucket + '/toDo/')):

                print('--------CARREGAR PERSON----------') 
                path = self._bucket + '/toDo/' + self._name
            
                df = pd.read_csv(path, sep=';')         
                # print(df.columns)
                self._folderService.moveToDoing()

                mysql = MysqlDatabase()
                connection = mysql.connect()

                for index, row in df.iterrows():
                    print(row['ModifiedDate'])                
                    person = PersonDAO(row,connection)
                    person.insert()
                    break

                self._folderService.moveToDone()
            else:
                print("Não existe arquivo Person.Person para ser processado")

        except Exception as ex:
            print('Erro na Leitura de Person')
            print(ex)
        finally:
            if (connection != False and connection.is_connected()):
                connection.close()




