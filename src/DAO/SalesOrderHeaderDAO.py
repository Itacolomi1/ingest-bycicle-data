from src.validators.coreValidator import CoreValidator
from src.DAO.MysqlDatabase import MysqlDatabase


class SalesOrderHeaderDAO():

    def __init__(self,valores, conexao):
         self._tabela = 'sales.salesOrderHeader'
         self._valores = valores
         self.coreIngest = CoreValidator()
         self._conexao = conexao

    def insert(self):
        try:
            query = f'''INSERT INTO `{self._tabela}` 
                    (                   
                        SalesOrderID,
                        RevisionNumber,
                        OrderDate,
                        DueDate,
                        ShipDate,
                        Status,
                        OnlineOrderFlag,
                        SalesOrderNumber,
                        PurchaseOrderNumber,
                        AccountNumber,
                        CustomerID,
                        SalesPersonID,
                        TerritoryID,
                        BillToAddressID,
                        ShipToAddressID,
                        ShipMethodID,
                        CreditCardID,
                        CreditCardApprovalCode,
                        CurrencyRateID,
                        SubTotal,
                        TaxAmt,
                        Freight,
                        TotalDue,
                        Comment,
                        rowguid,
                        ModifiedDate)   
                VALUES
                (
                    {self.coreIngest.validateINT(self._valores['SalesOrderID'])},                    
                    {self.coreIngest.validateINT(self._valores['RevisionNumber'])},
                    {self.coreIngest.stringField(self._valores['OrderDate'])},
                    {self.coreIngest.stringField(self._valores['DueDate'])},
                    {self.coreIngest.stringField(self._valores['ShipDate'])},
                    {self.coreIngest.validateINT(self._valores['Status'])},
                    {self.coreIngest.validateINT(self._valores['OnlineOrderFlag'])},
                    {self.coreIngest.stringField(self._valores['SalesOrderNumber'])},
                    {self.coreIngest.stringField(self._valores['PurchaseOrderNumber'])},
                    {self.coreIngest.stringField(self._valores['AccountNumber'])},
                    {self.coreIngest.validateINT(self._valores['CustomerID'])},
                    {self.coreIngest.validateINT(self._valores['SalesPersonID'])},
                    {self.coreIngest.validateINT(self._valores['TerritoryID'])},
                    {self.coreIngest.validateINT(self._valores['BillToAddressID'])},
                    {self.coreIngest.validateINT(self._valores['ShipToAddressID'])},
                    {self.coreIngest.validateINT(self._valores['ShipMethodID'])},
                    {self.coreIngest.validateINT(self._valores['CreditCardID'])},
                    {self.coreIngest.stringField(self._valores['CreditCardApprovalCode'])},
                    {self.coreIngest.validateINT(self._valores['CurrencyRateID'])},
                    {self.coreIngest.validateFloat(self._valores['SubTotal'])},
                    {self.coreIngest.validateFloat(self._valores['TaxAmt'])},
                    {self.coreIngest.validateFloat(self._valores['Freight'])},
                    {self.coreIngest.validateFloat(self._valores['TotalDue'])},
                    {self.coreIngest.stringField(self._valores['Comment'])},
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
    


       

        
        
        

 