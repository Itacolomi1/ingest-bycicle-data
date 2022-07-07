from typing import final
from src.services.MysqlDatabase import MysqlDatabase

if __name__ == '__main__':

    try:
        mysql = MysqlDatabase()
        conection = mysql.connect()        
        print(conection)
        if conection != False:
            cursor = conection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: {0}".format(record))
        else:
            print('Error')

    except Exception as ex:        
        print(ex)
    finally:
        if(conection != False):
            mysql.disconnect(cursor,conection)

    

