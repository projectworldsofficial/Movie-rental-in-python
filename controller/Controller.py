from domain.Borrow import Borrow
from domain.Rental import Rental 
from repository.BorrowRepository import BorrowRepository
from repository.DvdRepository import DvdRepository
from domain.Dvd import Dvd
from random import randint
from domain.Errors import DuplicateException, InexistingException, AlreadyBurrowed


class Controller():
    def __init__(self,borepo,dvdrepo):
        self.__borepo = borepo
        self.__dvdrepo = dvdrepo
        
    def list_rentals(self): 
        rentals = []
        
        for i in self.__borepo.get_all():
            r = Rental(i.get_id(), self.__dvdrepo.get_all()[self.__dvdrepo.find(i.get_id_dvd())].get_name(), i.get_name_client()) 
            rentals.append(r)

        rentals = sorted(rentals, key = lambda x: x.dvd_name)    
        return rentals 
    
    def filter_dvds_name(self, filterString):
        filteredList = []
        for dvd in self.__dvdrepo.get_all():
            if filterString.lower() in dvd.get_name().lower():
                filteredList.append(dvd)
        return filteredList
    
    def __get_all_borrow_ids(self):
        idsList = []
        for i in self.__borepo.get_all():
            idsList.append(i.get_id())
        return idsList
        
                   
    def add_new_borrow(self, name, dvd_id):
        rand_ids = self.__get_all_borrow_ids()
        id = randint(0, len(rand_ids)*10)  
        while(id in rand_ids):
            id = randint(0, len(rand_ids)*10)
        if str(dvd_id) in str(self.__get_all_dvds_ids()):
            if not(str(dvd_id) in str(self.__get_all_dvds_ids_from_borrows())): 
                b = Borrow(int(id), int(dvd_id), name)
                self.__borepo.add(b)
            else:
                raise AlreadyBurrowed()
        else:
            raise InexistingException()
        
    def delete_borrow(self, idBorrow):
        self.__borepo.remove(idBorrow)
        
    def __get_all_dvds_ids_from_borrows(self):
        dvdIds = []
        for b in self.__borepo.get_all():
            dvdIds.append(b.get_id_dvd())
        return dvdIds
        
              
    def __get_all_dvds_ids(self): 
        dvdIds = []
        for i in self.__dvdrepo.get_all():
            dvdIds.append(i.get_id_dvd())
        return dvdIds       
        
        
    
    
        
    
"""      
def test():
    BorrowRepo = BorrowRepository()
    newBor = Borrow(5,7,"ajska")
    BorrowRepo.add(newBor)
    newBor = Borrow(1,2,"asdfas")
    BorrowRepo.add(newBor)
    newBor = Borrow(2,1,"hurrdurr")
    BorrowRepo.add(newBor)
    
    DvdRepo = DvdRepository()
    newDvd = Dvd(2,"hkasf")
    DvdRepo.add(newDvd)
    newDvd = Dvd(1,"hkdss")
    DvdRepo.add(newDvd)
    newDvd = Dvd(7,"hk98098080")
    DvdRepo.add(newDvd)
    
    ctrl = Controller(BorrowRepo,DvdRepo) 
    
    for r in ctrl.show_all_rentals():
        print (r)
        
        
test()
"""    
    
    
    
       
     
            
            
            
            
        
        
            