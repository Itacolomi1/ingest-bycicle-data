from src.validators.coreValidator import CoreValidator
from src.DAO.MysqlDatabase import MysqlDatabase


class CustomerDAO():

    def __init__(self,valores, conexao):
         self._tabela = 'sales.customer'
         self._valores = valores
         self.coreIngest = CoreValidator()
         self._conexao = conexao

    def insert(self):
        try:
            query = f'''INSERT INTO `{self._tabela}` 
                    (CustomerID,
                     PersonID,
                     StoreID,
                     TerritoryID,
                     AccountNumber,                    
                     rowguid,
                     ModifiedDate)   
                VALUES
                (
                    {self.coreIngest.validateINT(self._valores['CustomerID'])},
                    {self.checkPerson()},
                    {self.coreIngest.validateINT(self._valores['StoreID'])},
                    {self.coreIngest.validateINT(self._valores['TerritoryID'])},
                    {self.coreIngest.stringField(self._valores['AccountNumber'])},                  
                    {self.coreIngest.stringField(self._valores['rowguid'])},
                    {self.coreIngest.stringField(self._valores['ModifiedDate'])}
                )
                     '''

   
            
            cursor = self._conexao.cursor()

            cursor.execute(query)
            self._conexao.commit()
            print(cursor.rowcount, "Record inserted successfully into production.product table")
            cursor.close()
            return True

        except Exception as ex:
            print(ex)
            return False
    
    #Caso não haja Id de pessoa na tabela de pessoa atribuir a usuário default
    def checkPerson(self):

        if(self.coreIngest.validateINT(self._valores['PersonID']) == 0):
            return 20778
        else:
            return self.coreIngest.validateINT(self._valores['PersonID'])

       

        
        
        

 