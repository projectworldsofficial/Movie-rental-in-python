from domain.Errors import InvalidClassException
from domain.Rental import Rental
class RentalValidator():
    def validate(self, rental):
        errors = ""
        if type(rental.get_id()) != int:
            errors += "Invalid id! \n"
        
        if len(rental.get_dvd_name()) == 0:
            errors += "Invalid dvd name! \n "
            
        if len(rental.get_client_name()) == 0:
            errors += "Invalid client name! \n" 
                 
        if errors != "" :
            raise InvalidClassException(errors)
        
"""
def test():
    validator = RentalValidator()
    newRental = Rental(5,"shg","kfkas")
    
    validator.validate(newRental)
    
    newRental = Rental("lala","shg","kfkas")

    try:
        validator.validate(newRental)
    
    except InvalidClassException as ics:
        print (ics)  
    
    newRental = Rental(5,"","kfkas")    
    try:
        validator.validate(newRental)
    
    except InvalidClassException as ics:
        print (ics)  
        
    newRental = Rental(5,"shg","")    
    try:
        validator.validate(newRental)
    
    except InvalidClassException as ics:
        print (ics)         
        
test()   

"""     
        
    
    
    
            
        
        
        
        
            
               
            
            
        
            
        
        