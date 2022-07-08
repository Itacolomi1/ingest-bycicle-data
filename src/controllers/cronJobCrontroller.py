from src.services.productService import Product
from src.services.customerService import Customer
from src.services.personService import Person
from src.services.specialOfferProductService import SpecialOfferProduct
from src.services.salesOrderDetailService import SalesOrderDetail
from src.services.salesOrderHeaderService import SalesOrderHeader


class CronJobController:


    def start(self):
        print('---------Início CronJob---------')

        # try:
        #     print(int('NaN'))
        # except Exception as ex:
        #     print(0)        

        # product = Product()
        # product.load()

        # customer = Customer()
        # customer.load()

        # person = Person()
        # person.load()

        # Sproduct = SpecialOfferProduct()
        # Sproduct.load()

        salesOrder = SalesOrderDetail()
        salesOrder.load()

        # salesOrderHeader = SalesOrderHeader()
        # salesOrderHeader.load()