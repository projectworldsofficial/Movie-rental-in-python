from domain.Rental import Rental
from domain.Errors import DuplicateException, InexistingException,\
    AlreadyBurrowed

class UI():
    def __init__(self, ctrl):
        self.__ctrl = ctrl
        
    def menu(self):
        menu_list = ""
        menu_list += "\t\tMOVIE RENTAL SHOP MANAGEMENT \n\n"
        menu_list += "\t\t\t  Menu:\n\n"
        menu_list += "\t To get all rentals type <list rentals>. \n"
        menu_list += "\t To get filtered rentals type <filter 'dvd name'>. \n"
        menu_list += "\t To add a new rental type <add 'dvd id' 'client name'>. \n"
        menu_list += "\t To return a rental type <ret 'dvd id'>. \n"
        
        menu_list += "\t To show the menu type <menu>.\n"
        menu_list += "\t To exit type <exit>.\n"
        print (menu_list)
        
    def print_list(self, myList):
        if len(myList) == 0:
            print("The list is empty!\n")
        else:
            for i in myList:
                print (i)
            
    def run(self):
        self.menu()
        while True:
            command = input("Please give me a command:")
            if command == "menu":
                self.menu()
            elif command == "list rentals":
                self.print_list(self.__ctrl.list_rentals())
            elif command == "exit":
                print("The program will exit...")
                return
            elif "filter" in command:
                info = command.split(" ", 1)
                if len(info) == 2:
                    self.print_list(self.__ctrl.filter_dvds_name(info[1]))
                else:
                    print("Please give me a valid command! \n")
                    #fncall1353
            elif "add" in command:
                info = command.split(" ")
                try:
                    self.__ctrl.add_new_borrow(info[2],info[1])
                    print("Successfully rented a dvd. \n")
                except DuplicateException as de:
                    print(de)  
                except InexistingException as ie:
                    print (ie)  
                except AlreadyBurrowed as ae:
                    print(ae)
            elif "ret" in command:
                info = command.split(" ")
                try:
                    self.__ctrl.delete_borrow(int(info[1]))
                    print("Successfully returned a rented a dvd. \n")
                except InexistingException as ie:
                    print (ie)
                    
                            
                     
            
            else:
                print("Please give me a valid command! \n") 
            
            
                        
