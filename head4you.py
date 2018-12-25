import urllib2
import sys
import colorama
from colorama import Fore, Back,  init

def print_header():
  print(Fore.BLUE+'''

 /$$   /$$                           /$$ /$$   
/$$ /$$     /$$                 
| $$  | $$                          | $$| $$  | 
$$|  $$   /$$/                 
| $$  | $$  /$$$$$$   /$$$$$$   /$$$$$$$| $$  | 
$$ \  $$ /$$//$$$$$$  /$$   /$$
| $$$$$$$$ /$$__  $$ |____  $$ /$$__  $$| 
$$$$$$$$  \  $$$$//$$__  $$| $$  | $$
| $$__  $$| $$$$$$$$  /$$$$$$$| $$  | $$|_____  
$$   \  $$/| $$  \ $$| $$  | $$
| $$  | $$| $$_____/ /$$__  $$| $$  | $$      | 
$$    | $$ | $$  | $$| $$  | $$
| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$      | 
$$    | $$ |  $$$$$$/|  $$$$$$/
|__/  |__/ \_______/ \_______/ \_______/      
|__/    |__/  \______/  \______/ 
                                                                                 
Tool For Grabbing Http Headers..
      Author:- A1C3VENOM..
     ''')
     
print_header()
url =raw_input("Enter Full Website Name:- ")
url.rstrip()
header = urllib2.urlopen(url).info()
print(str(header))


init()

    
                                                                                                                                                     
                                                                               
                                                                               


