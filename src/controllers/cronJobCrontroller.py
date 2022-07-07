from src.services.productService import Product

class CronJobController:


    def start(self):
        print('---------Início CronJob---------')

        # try:
        #     print(int('NaN'))
        # except Exception as ex:
        #     print(0)
        

        product = Product()
        product.load()