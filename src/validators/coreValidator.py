class CoreValidator():            
        
    
    def validateINT(self, field):
        try:
            return int(field)
        except Exception as ex:
            return 0
    
    def stringField(sel, field):
        return "'" + str(field) + "'"
    
