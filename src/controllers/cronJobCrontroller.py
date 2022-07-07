from src.services.productService import Product
from src.services.customerService import Customer
from src.services.personService import Person


class CronJobController:


    def start(self):
        print('---------Início CronJob---------')

        # try:
        #     print(int('NaN'))
        # except Exception as ex:
        #     print(0)
        

        # product = Product()
        # product.load()


        customer = Customer()
        customer.load()

        # person = Person()
        # person.load()