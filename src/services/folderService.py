
import os
from os import listdir
from src.services.settingsService import SettingsService

class FolderService():

    def __init__(self, file):
        configuration = SettingsService()
        self._basePath = configuration.properties['bucketPath']  

        self._file = file        
        self._donePath = self._basePath + "/Done/"
        self._doingPath = self._basePath + "/Doing/"
        self._toDoPath = self._basePath + "/toDo/"
    
    def moveToDoing(self):
        os.replace(self._toDoPath + self._file, self._doingPath + self._file)
    
    def moveToDone(self):
        os.replace(self._doingPath + self._file, self._donePath + self._file)
    
    def findFile(self,path):

        for f in listdir(path):
            if(f == self._file):
                return True
        
        return False
    
    
    


    

