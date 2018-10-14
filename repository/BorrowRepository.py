from domain.Errors import DuplicateException, InexistingException
from domain.Borrow import Borrow
from domain.BorrowValidator import BorrowValidator

class BorrowRepository():
    def __init__(self, file_name):
        self.__borrows = []
        self.__file_name = file_name
        self.__bValidator = BorrowValidator()
        self.__load_file()
        

    def find(self, id):
        for i in range(0,len(self.__borrows)):
            if self.__borrows[i].get_id() == id :
                return i
        
        return -1 
    
    def add(self, borrow):
        if self.find(borrow.get_id()) == -1:
            self.__bValidator.validate(borrow)
            self.__borrows.append(borrow)
            self.__write_file()
        else:
            raise DuplicateException()
        
    def add_without_writing(self, borrow):
        if self.find(borrow.get_id()) == -1:
            self.__bValidator.validate(borrow)
            self.__borrows.append(borrow)
        else:
            raise DuplicateException()
        
    def remove(self,id): 
        pos = self.find(id)      
        if pos != -1:
            self.__borrows.pop(pos)
            self.__write_file()
        else:
            raise InexistingException()
            
    def update(self, id, idDvd, name):
        pos = self.find(id)
        if pos == -1:
            raise InexistingException()
        else:
            self.__borrows[pos].set_name_client(name)
            self.__borrows[pos].set_id_dvd(idDvd)
            
            
            
    def show(self,id):
        pos = self.find(id)
        if pos != -1:
            return self.__borrows[pos]
        else:
            raise InexistingException()
                                                 
    def get_all(self):
        return self.__borrows
    
    def __load_file(self):
        f = open(self.__file_name, "r")
        info = f.readline()
        j = 0
        while info:
            borrow_info = info.split(";;")
            if len(borrow_info) == 3:
                borrow = Borrow(int(borrow_info[0]), int(borrow_info[1]), borrow_info[2])
                self.add_without_writing(borrow)
                info = f.readline()
            else:
                info = f.readline()
                j += 1
                continue
        if j != 0:
            print(str(j) + " lines have been corrupted in your file.\n")
        print("Borrows have been successfully loaded in the system.\n")
        f.close()
        
    def __write_file(self):
        f = open(self.__file_name,"w")
        for borrow in self.__borrows:
            f.write(str(borrow.get_id()) + ";;" + str(borrow.get_id_dvd()) + ";;" + borrow.get_name_client() + "\n")
        f.close()
        
        
    
    
    
"""    
def test():
    borepo = BorrowRepository() 
    newBorrow = Borrow(1,5,"khkja")
    borepo.add(newBorrow)
    
    newBorrow1 = Borrow(2,6,"jjkdsaff")
    borepo.add(newBorrow1)
    
    newBorrow2 = Borrow(3,7,"hd")
    borepo.add(newBorrow2)
    
    
    try:
        borepo.add(newBorrow)
    except DuplicateException as de:
        print (de) 
        
    borepo.remove(1)
    
    try:
        borepo.remove(40)
    except InexistingException as ie:
        print (ie)   

        
    try:
        borepo.update(70,3,"sgjsa")
    except InexistingException as ie:
        print (ie)
              
    
    try:
        borepo.update(40,8,"ahakjs")  
    except  InexistingException as ie:
        print (ie)
        
    borepo.show(3)
    borepo.update(3,90,"lalala")
    borepo.show(3) 
    print (borepo.show(3)) 
    
    try:
        borepo.show(678)
    except InexistingException   as ie:
        print (ie)    
                 
        
test()
           
"""        
    
        
        
    
           
        
    