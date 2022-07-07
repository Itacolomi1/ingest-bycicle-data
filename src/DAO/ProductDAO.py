from src.validators.coreValidator import CoreValidator
from src.DAO.MysqlDatabase import MysqlDatabase


class ProductDAO():

    def __init__(self,valores, conexao):
         self._tabela = 'production.product'
         self._valores = valores
         self.coreIngest = CoreValidator()
         self._conexao = conexao

    def insert(self):
        try:
            query = f'''INSERT INTO `{self._tabela}` 
                    (ProductID,
                     Name,
                     ProductNumber,
                     MakeFlag,
                     FinishedGoodsFlag,
                     Color,
                     SafetyStockLevel,
                     ReorderPoint,
                     StandardCost,
                     ListPrice,
                     Size,
                     SizeUnitMeasureCode,
                     WeightUnitMeasureCode,
                     Weight,
                     DaysToManufacture,
                     ProductLine,
                     Class,
                     Style,
                     ProductSubcategoryID,
                     ProductModelID,
                     SellStartDate,
                     SellEndDate,
                     DiscontinuedDate,       
                     rowguid,
                     ModifiedDate)   
                VALUES
                (
                    {self.coreIngest.validateINT(self._valores['ProductID'])},
                    {self.coreIngest.stringField(self._valores['Name'])},
                    {self.coreIngest.stringField(self._valores['ProductNumber'])},
                    {self.coreIngest.validateINT(self._valores['MakeFlag'])},
                    {self.coreIngest.validateINT(self._valores['FinishedGoodsFlag'])},
                    {self.coreIngest.stringField(self._valores['Color'])},
                    {self.coreIngest.validateINT(self._valores['SafetyStockLevel'])},
                    {self.coreIngest.validateINT(self._valores['ReorderPoint'])},
                    {self.coreIngest.validateFloat(self._valores['StandardCost'])},
                    {self.coreIngest.validateFloat(self._valores['ListPrice'])},
                    {self.coreIngest.stringField(self._valores['Size'])},
                    {self.coreIngest.stringField(self._valores['SizeUnitMeasureCode'])},
                    {self.coreIngest.stringField(self._valores['WeightUnitMeasureCode'])},
                    {self.coreIngest.validateFloat(self._valores['Weight'])},
                    {self.coreIngest.validateINT(self._valores['DaysToManufacture'])},
                    {self.coreIngest.stringField(self._valores['ProductLine'])},
                    {self.coreIngest.stringField(self._valores['Class'])},
                    {self.coreIngest.stringField(self._valores['Style'])},
                    {self.coreIngest.validateINT(self._valores['ProductSubcategoryID'])},
                    {self.coreIngest.validateINT(self._valores['ProductModelID'])},
                    {self.coreIngest.stringField(self._valores['SellStartDate'])},
                    {self.coreIngest.stringField(self._valores['SellEndDate'])},
                    {self.coreIngest.stringField(self._valores['DiscontinuedDate'])},                   
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
       

        
        
        

 