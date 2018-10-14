from domain.Borrow import Borrow
from domain.Errors import InvalidClassException
from _overlapped import NULL


class BorrowValidator():
    def validate(self,borrow):
        errors = ""
        
        if type(borrow.get_id()) != int:
            errors += "Invalid id! \n"
                    
        if type(borrow.get_id_dvd()) != int:
            errors += "Invalid dvd id! \n"
            
        if borrow.get_name_client() == "":
            errors += "Invalid client name! \n"
            
        if len(errors) != 0:
            raise InvalidClassException(errors)
        
"""
def sygys():
    newborrow = Borrow(5,5,"") 
    bvalidator = BorrowValidator()
    try:
        bvalidator.validate(newborrow)
    except InvalidClassException as ie:
        print(ie)
    
    newborrow = Borrow("sgs", 5, "Chestii")
    try:
        bvalidator.validate(newborrow)
    except InvalidClassException as ie:
        print(ie)
        
    newborrow = Borrow(1, "csdfas", "Hurr durr")
    try:
        bvalidator.validate(newborrow)
    except InvalidClassException as ie:
        print(ie)
    
    newborrow = Borrow("asdfads", "asdfasd", "")
    try:
        bvalidator.validate(newborrow)
    except InvalidClassException as ie:
        print(ie)

sygys()
"""
    
   
      

        
            
            
            
            
                
                
        