import math
class CoreValidator():            
        
    
    def validateINT(self, field):
        try:
            return int(field)
        except Exception as ex:
            return 0
    
    def stringField(sel, field):
        return "'" + str(field) + "'"
    
    def validateFloat(self,field):
        try:
            l = float(field)
            if(math.isnan(l)):
                return 0
            else:
                return l

        except Exception as ex:
            return 0
        
    
