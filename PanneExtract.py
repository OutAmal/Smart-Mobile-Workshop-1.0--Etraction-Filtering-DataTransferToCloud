import re
import serial
from datetime import datetime, timedelta
 

def Classification(list=[]):
    list != 0 
    codeHex = int(list[0], 16)
    if codeHex in range(int("0x0000", 0), int("0x1FFF", 0)):
        return ("Reserve")
    elif codeHex in range (int("0x2000", 0) , int("0x3FFF", 0)):
        return ("CCU")
    elif codeHex in range (int("0x4000", 0) , int("0x5FFF", 0)):
        return ("TCU")
    elif codeHex in range (int("0x6000", 0) , int("0x7FFF", 0)):
        return ( "CGS")
    elif codeHex in range (int("0x8000", 0) , int("0x9FFF", 0)):
        return ( "Noeud, Moniteur et divers")
    else :
        return  ("UGC")    
                
            #return extract[0]
    #def Voiture(self,str):
    #    extract = re.findall(r'(?<=uic:)[0-9]+',str)
     #   if   extract != []:
      #      if  extract[0] is not None:
       #           print ( extract [0])    
       
        
#def mainExtract(element):
 #   element = Panne()
  #  element.code()
   # element.Voiture()
   #element.time()
       #ser=serial.Serial('/dev/ttyACM0',38400,timeout=1)
       #data=ser.readlines()
    #Code = re.findall(r'(?<=code:)[0-9-a-zA-Z]+', element)
    #Voiture=re.findall(r'(?<=uic:)[0-9]+',element)
    #time = datetime.now().strftime("%B %d, %Y %I:%M%p")
    #if Code != []:
     #          print(Code[0], Voiture [0], time, Class(int(Code[0], 16)))
#if __name__=="__main__":
 #   mainExtract (element)

    












































        
