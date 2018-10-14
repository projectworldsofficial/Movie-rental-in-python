

class Rental():
   
    def __init__(self, idRental, dvd_name, client_name):
        self.__idRental = idRental
        self.dvd_name = dvd_name
        self.__client_name = client_name
        
    def get_id(self):
        return self.__idRental
    
    def get_dvd_name(self):
        return self.dvd_name
    
    def get_client_name(self):
        return self.__client_name
    
    def set_id(self,value): 
        self.__idRental = value
        
    def set_dvd_name (self,value):
        self.dvd_name = value
        
    def set_client_name(self,value): 
        self.__client_name = value
        
    def __str__(self):
        return (str(self.__idRental) + " " + str(self.dvd_name) + " " + str(self.__client_name))
    
    
"""    
def test(): 
    obj = Rental(7,"lala","ana")
    print(obj.get_id()) 
    obj.set_id(9)
    print(obj.get_id())
    
    print(obj.get_dvd_name())
    obj.set_dvd_name("hjaghda")
    print(obj.get_dvd_name())
    
    print(obj.get_client_name())
    obj.set_client_name("alina")
    print (obj.get_client_name())
       

test()

"""
      
    
        
                 
       
        