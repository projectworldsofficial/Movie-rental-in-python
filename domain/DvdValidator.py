from domain.Dvd import Dvd
from domain.Errors import InvalidClassException


class DvdValidator():
    def validate(self,dvd):
        errors = ""
        
        if type(dvd.get_id_dvd()) != int:
            errors += "Invalid id! \n"
        
        if dvd.get_name() == "":
            errors += "Invalid name! \n" 
        
        if len(errors) != 0:
            raise InvalidClassException(errors)
        
""" 
def testdvd():
    dvalidator = DvdValidator()
    newDvd = Dvd("hgdd","kdgfj")  
    try:
        dvalidator.validate(newDvd)
    except InvalidClassException as ie:
        print (ie)
    
    newDvd = Dvd("hgdd","") 
    try:
        dvalidator.validate(newDvd)
    except InvalidClassException as ie:
        print (ie)
        
    newDvd = Dvd(6,"") 
    try:
        dvalidator.validate(newDvd)
    except InvalidClassException as ie:
        print (ie)
           
    
        
        
testdvd()   


"""     
        
        
        
          
          
        