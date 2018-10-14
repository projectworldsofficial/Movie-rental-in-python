class InvalidClassException(BaseException):
    def __init__(self,msg):
        self.__msg = msg
        
    def __str__(self):
        return str(self.__msg)   
    
class DuplicateException(BaseException):  
    def __str__(self):
        return ("The item is already in the list. \n")


class InexistingException(BaseException): 
    def __str__(self):
        return ("We're sorry, but the item doesn't exist. \n")   
        
    
class AlreadyBurrowed(BaseException):
    def __str__(self):
        return("We're sorry, but the item is already rented. \n")