import pandas as pd
from src.services.settingsService import SettingsService
from src.services.PersonIngest import PersonIngest
from src.services.MysqlDatabase import MysqlDatabase

class Person():

    def __init__(self):
        configuration = SettingsService()
        self._bucket = configuration.properties['bucketPath']  
        self._name = 'Person.Person.csv'
       

    def load(self):
        try: 
            print('--------CARREGAR PERSON----------') 
            path = self._bucket + '/' + self._name
           
            df = pd.read_csv(path, sep=';')         
            # print(df.columns)

            mysql = MysqlDatabase()
            connection = mysql.connect()

            for index, row in df.iterrows():
                print(row['ModifiedDate'])                
                person = PersonIngest(row,connection)
                sql = person.insert()

        except Exception as ex:
            print('Erro na Leitura de Person')
            print(ex)
        finally:
            if (connection != False and connection.is_connected()):
                connection.close()




