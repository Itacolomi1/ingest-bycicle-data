from src.validators.coreValidator import CoreValidator
from src.DAO.MysqlDatabase import MysqlDatabase


class PersonDAO():

    def __init__(self,valores, conexao):
         self._tabela = 'person.person'
         self._valores = valores
         self.coreIngest = CoreValidator()
         self._conexao = conexao

    def insert(self):
        try:
            query = f'''INSERT INTO `{self._tabela}` 
                    (BusinessEntityID,
                     PersonType,
                     NameStyle,
                     Title,
                     FirstName,
                     MiddleName,
                     LastName,
                     Suffix,
                     EmailPromotion,
                     AdditionalContactInfo,
                     Demographics,
                     rowguid,
                     ModifiedDate)   
                VALUES
                (
                    {self.coreIngest.validateINT(self._valores['BusinessEntityID'])},
                    {self.coreIngest.stringField(self._valores['PersonType'])},
                    {self.coreIngest.validateINT(self._valores['NameStyle'])},
                    {self.coreIngest.stringField(self._valores['Title'])},
                    {self.coreIngest.stringField(self._valores['FirstName'])},
                    {self.coreIngest.stringField(self._valores['MiddleName'])},
                    {self.coreIngest.stringField(self._valores['LastName'])},
                    {self.coreIngest.stringField(self._valores['Suffix'])},
                    {self.coreIngest.validateINT(self._valores['EmailPromotion'])},
                    {self.coreIngest.stringField(self._valores['AdditionalContactInfo'])},
                    {self.coreIngest.stringField(self._valores['Demographics'])},
                    {self.coreIngest.stringField(self._valores['rowguid'])},
                    {self.coreIngest.stringField(self._valores['ModifiedDate'])}
                )
                     '''

   
            print(query)
            # cursor = self._conexao.cursor()

            # cursor.execute(query)
            # self._conexao.commit()
            # print(cursor.rowcount, "Record inserted successfully into person.person table")
            # cursor.close()
            # return True

        except Exception as ex:
            print(ex)
            return False
       

        
        
        

 