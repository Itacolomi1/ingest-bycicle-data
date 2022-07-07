from typing import final
from src.controllers.cronJobCrontroller import CronJobController

if __name__ == '__main__':

    try:
        controller = CronJobController()
        controller.start()
        
    except Exception as ex:        
        print(ex)
    
        
            

    

