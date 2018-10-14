from domain.Rental import Rental
from domain.Errors import DuplicateException, InexistingException

class RentalRepository():
    def __init__(self):
        self.__rentals = []
    
    
    
    def find(self, id):
        for i in range(0,len(self.__rentals)):
            if self.__rentals[i].get_id() == id:
                return i
        return -1
        
            
    def add(self, rental): 
        pos = self.find(rental.get_id())
        if pos == -1:
            self.__rentals.append(rental)
        else:
            raise DuplicateException()
        
    def update(self, id, name, client):
        pos = self.find(id) 
        if pos != -1:
            self.__rentals[pos].set_dvd_name(name) 
            self.__rentals[pos].set_client_name(client)
        else:
            raise InexistingException()
     
    def remove(self,id):
        pos = self.find(id)
        if pos != -1:
            self.__rentals.pop(pos)
        else:
            raise InexistingException()
        
    
    def show(self,id):
        pos = self.find(id)  
        if pos != -1:
            return self.__rentals[pos]      
        else:
            raise InexistingException()
                 
           
    def get_all(self): 
        return self.__rentals 
         
        
"""        
def test():
    rentrepo = RentalRepository()
    newRental = Rental(6,"jasja","jahdj")
    rentrepo.add(newRental)
    
    newRental1 = Rental(7,"jasas","jaeryre")
    rentrepo.add(newRental1)
    
    newRental1 = Rental(9,"jasas","jaeryre")
    rentrepo.add(newRental1)
    
    try:
        rentrepo.remove(40)
    except InexistingException as ie:
        print (ie)
    
    rentrepo.remove(6)
        
    try: 
        rentrepo.update(100,"lala","bla")
    except InexistingException as ie:
        print (ie)     
              
    try:
        rentrepo.show(788)
    except InexistingException as ie:
        print (ie)     
                            
    
test()    
    
"""    
    
            
             
           