import pandas as pd
from src.services.settingsService import SettingsService

class Person():

    def __init__(self):
        configuration = SettingsService()
        self._bucket = configuration.properties['bucketPath']  
        self._name = 'Person.Person.csv' 

    def load(self):
        try: 
            print('--------CARREGAR PERSON----------') 
            path = self._bucket + '/' + self._name
            print(path)
            df = pd.read_csv(path, sep=';')         
            print(df.columns)

        except Exception as ex:
            print('Erro na Leitura de Person')
            print(ex)




