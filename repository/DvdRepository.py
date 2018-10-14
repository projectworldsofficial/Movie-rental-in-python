from domain.Dvd import Dvd
from domain.Errors import DuplicateException
from domain.Errors import InexistingException
from domain.DvdValidator import DvdValidator

class DvdRepository():
    def __init__(self, file_name):
        self.__dvds = []
        self.__file_name = file_name
        self.__dValidator = DvdValidator()
        self.__load_file()
        
    def find(self, id):
        for i in range(0, len(self.__dvds)):
            if self.__dvds[i].get_id_dvd() == id:
                return i
        return -1
                    
                          
    def add(self, dvd):
        if self.find(dvd.get_id_dvd()) == -1:
            self.__dValidator.validate(dvd)
            self.__dvds.append(dvd)
        else:
            raise DuplicateException()
    
        
    def remove(self, id):
        position = self.find(id)
        if position != -1:
            self.__dvds.pop(position)
        else:
            raise InexistingException()
        
    def update(self, id, name): 
        pos = self.find(id) 
        if pos == -1:
            raise InexistingException()
        
        else:
            self.__dvds[pos].set_name(name)
             
             
    def show(self, id): 
        pos = self.find(id)
        if pos == -1:
            raise InexistingException()
        else:
            return self.__dvds[pos]
        
        
    def get_all(self): 
        return self.__dvds
    
    def __load_file(self):
        f = open(self.__file_name, "r")
        info = f.readline()
        j = 0
        while info:
            dvd_info = info.split(";;")
            if len(dvd_info) == 2:
                dvd = Dvd(int(dvd_info[0]), dvd_info[1])
                self.add(dvd)
                info = f.readline()
            else:
                info = f.readline()
                j += 1
                continue
        if j != 0:
            print(str(j) + " lines have been corrupted in your file.\n")
        print("Dvds have been successfully loaded in the system.\n")
        f.close()
        
        
    
"""       
def test():
    
    newDvd = Dvd(5,"jgsj")
    dvdrepo = DvdRepository()
    dvdrepo.add(newDvd)
    
    newDvd1 = Dvd(2,"dkska")
    dvdrepo.add(newDvd1)
    
    newDvd2 = Dvd(1,"jjdd")
    dvdrepo.add(newDvd2)
    
    
    try:
        dvdrepo.add(newDvd)
    except DuplicateException as de:
        print (de)
        
    try:
        dvdrepo.remove(30)
    except InexistingException as ie:
        print (ie) 
    
    
    dvdrepo.remove(2)
    
    try:
        dvdrepo.show(45)
    except InexistingException as ie:
        print (ie)    
        
    try:
        dvdrepo.update(6,"dsfds")
    except InexistingException as ie:
        print (ie)   
    
    dvdrepo.update(1,"ana") 
    print (dvdrepo.show(1))
      
    
      
        
test()
        
"""             
             
            
            
    
    
      
    
        
             
        
                
               
               
            
        