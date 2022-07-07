import mysql.connector
from mysql.connector import Error
from src.services.settingsService import SettingsService


class MysqlDatabase():

    def __init__(self):
        configuration = SettingsService()
        self.host = configuration.properties['host']
        self.database = configuration.properties['database']
        self.port = configuration.properties['port']
        self.user = configuration.properties['user']
        self.password = configuration.properties['password']

    
    def connect(self):
        try:
            connection = mysql.connector.connect(
                                        host= self.host,
                                        database= self.database,
                                        user= self.user,
                                        password= self.password,
                                        port = self.port)

            return connection

        except Exception as ex:
            print('Erro de conexão com o banco')
            print(ex)
            return False
    
    def disconnect(self,cursor,conection):
        cursor.close()
        conection.close()
        print('disconnected of mysql')

        
        
        
        



      





