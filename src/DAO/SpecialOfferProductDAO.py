from src.validators.coreValidator import CoreValidator
from src.DAO.MysqlDatabase import MysqlDatabase


class SpecialOfferProductDAO():

    def __init__(self,valores, conexao):
         self._tabela = 'sales.specialOfferProduct'
         self._valores = valores
         self.coreIngest = CoreValidator()
         self._conexao = conexao

    def insert(self):
        try:
            query = f'''INSERT INTO `{self._tabela}` 
                    (                   
                     SpecialOfferID,
                     ProductID,                  
                     rowguid,
                     ModifiedDate)   
                VALUES
                (
                    {self.coreIngest.validateINT(self._valores['SpecialOfferID'])},                    
                    {self.coreIngest.validateINT(self._valores['ProductID'])},                
                    {self.coreIngest.stringField(self._valores['rowguid'])},
                    {self.coreIngest.stringField(self._valores['ModifiedDate'])}
                )
                     '''

   
            
            cursor = self._conexao.cursor()

            cursor.execute(query)
            self._conexao.commit()
            print(cursor.rowcount, "Record inserted successfully into sales.specialOfferProduct table")
            cursor.close()
            return True

        except Exception as ex:
            print(ex)
            return False
    


       

        
        
        

 