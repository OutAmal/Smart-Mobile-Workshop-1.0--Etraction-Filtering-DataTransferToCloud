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
                
           

    












































        
