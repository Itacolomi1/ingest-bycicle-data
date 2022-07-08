from src.validators.coreValidator import CoreValidator
from src.DAO.MysqlDatabase import MysqlDatabase


class SalesOrderDetailDAO():

    def __init__(self,valores, conexao):
         self._tabela = 'sales.salesOrderDetail'
         self._valores = valores
         self.coreIngest = CoreValidator()
         self._conexao = conexao

    def insert(self):
        try:
            query = f'''INSERT INTO `{self._tabela}` 
                    (                   
                     SalesOrderID,
                     SalesOrderDetailID,
                     CarrierTrackingNumber,
                     OrderQty,
                     ProductID,
                     SpecialOfferID,
                     UnitPrice,
                     UnitPriceDiscount,
                     LineTotal,                  
                     rowguid,
                     ModifiedDate)   
                VALUES
                (
                    {self.coreIngest.validateINT(self._valores['SalesOrderID'])},                    
                    {self.coreIngest.validateINT(self._valores['SalesOrderDetailID'])},
                    {self.coreIngest.stringField(self._valores['CarrierTrackingNumber'])},
                    {self.coreIngest.validateINT(self._valores['OrderQty'])},
                    {self.coreIngest.validateINT(self._valores['ProductID'])},
                    {self.coreIngest.validateINT(self._valores['SpecialOfferID'])},
                    {self.coreIngest.validateFloat(self._valores['UnitPrice'])},
                    {self.coreIngest.validateINT(self._valores['UnitPriceDiscount'])},
                    {self.coreIngest.validateINT(self._valores['LineTotal'])},
                    {self.coreIngest.stringField(self._valores['rowguid'])},
                    {self.coreIngest.stringField(self._valores['ModifiedDate'])}
                )
                     '''

   
            
            cursor = self._conexao.cursor()

            cursor.execute(query)
            self._conexao.commit()
            print(cursor.rowcount, f"Record inserted successfully into {self._tabela} table")
            cursor.close()
            return True

        except Exception as ex:
            print(ex)
            return False
    


       

        
        
        

 