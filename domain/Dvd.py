class Dvd():
   def __init__(self,idDvd, name):
       self.__idDvd = idDvd
       self.__name = name

   def get_id_dvd(self):
       return self.__idDvd


   def get_name(self):
       return self.__name


   def set_id_dvd(self, value):
       self.__idDvd = value


   def set_name(self, value):
       self.__name = value
   
   def __str__(self):
       return (str(self.__idDvd) + " " + self.__name)

   idDvd = property(get_id_dvd, set_id_dvd)
   name = property(get_name, set_name)
   
   


    
       

   
        