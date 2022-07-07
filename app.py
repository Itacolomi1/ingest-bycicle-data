from typing import final
from src.services.personService import Person

if __name__ == '__main__':

    try:
        personFile = Person()
        personFile.load()
    except Exception as ex:        
        print(ex)
    
        
            

    

