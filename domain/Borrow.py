
class Borrow():
    def __init__(self, id, idDvD, nameClient):
        self.__id = id
        self.__idDvd = idDvD
        self.__nameClient = nameClient
    
    def get_id(self):
        return self.__id
    
    def get_id_dvd(self):    
        return self.__idDvd
    
    def get_name_client(self):
        return self.__nameClient
    
    def set_id(self, id): 
        self.__id = id
    
    def set_id_dvd(self,idDvd):
        self.__idDvd = idDvd
        
    def set_name_client(self,nameClient):
        self.__nameClient = nameClient
        
    def __str__(self): 
        return (str(self.__id) + " "  + self.__nameClient+" "+ str(self.__idDvd)) 
        
        

    
    
    
          
        
          
        
            
        
        
        
