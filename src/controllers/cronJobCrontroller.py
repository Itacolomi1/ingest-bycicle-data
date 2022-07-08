from src.services.productService import Product
from src.services.customerService import Customer
from src.services.personService import Person
from src.services.specialOfferProductService import SpecialOfferProduct
from src.services.salesOrderDetailService import SalesOrderDetail
from src.services.salesOrderHeaderService import SalesOrderHeader
from src.services.productService import Product


class CronJobController:


    def start(self):
        print('---------Início CronJob---------')

        person = Person()
        person.load()

        product = Product()
        product.load()

        customer = Customer()
        customer.load()

        Sproduct = SpecialOfferProduct()
        Sproduct.load()

        salesOrderHeader = SalesOrderHeader()
        salesOrderHeader.load()

        salesOrder = SalesOrderDetail()
        salesOrder.load()
