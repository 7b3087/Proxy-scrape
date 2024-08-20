# Coded by 7b3087 
# dsc : 7b3087 

import ctypes
import colorama
from colorama import Fore    
import requests
import time 

bleu = Fore.BLUE 

global proxyscrape
def proxyscrape():
   cls()
   
print(bleu, 'Lancement du processus en cours.....')
print(" ")
time.sleep(3)
print(" Vérification de l'utilisateur en cours")
print (" ")
time.sleep(3)
print(" ######## - - 80 Pourcents...")
print (" ")
time.sleep(4)
print(bleu, "Utilisateur vérifié !")
print (" ")
time.sleep(4)
print(bleu, "Ouverture du logiciel en cours..")  
print (" ")
time.sleep(5)

ctypes.windll.kernel32.SetConsoleTitleW("Proxy Scraper")
print (Fore.BLUE + '''       






       

       




 ██▓███   ██▀███   ▒█████  ▒██   ██▒▓██   ██▓      ██████   ▄████▄  ██▀███   ▄▄▄      ██▓███   ▓█████ ██▀███  
▓██░  ██ ▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░ ▒██  ██▒    ▒██    ▒  ▒██▀ ▀█ ▓██ ▒ ██▒▒████▄   ▓██░  ██  ▓█   ▀▓██ ▒ ██▒
▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░  ▒██ ██░    ░ ▓██▄    ▒▓█    ▄▓██ ░▄█ ▒▒██  ▀█▄ ▓██░ ██▓▒ ▒███  ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒   ░ ▐██▓░      ▒   ██▒▒▒▓▓▄ ▄██▒██▀▀█▄  ░██▄▄▄▄██▒██▄█▓▒ ▒ ▒▓█  ▄▒██▀▀█▄  
▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒  ░ ██▒▓░    ▒██████▒▒░▒ ▓███▀ ░██▓ ▒██▒▒▓█   ▓██▒██▒ ░  ░▒░▒████░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░   ██▒▒▒     ▒ ▒▓▒ ▒ ░░░ ░▒ ▒  ░ ▒▓ ░▒▓░░▒▒   ▓▒█▒▓▒░ ░  ░░░░ ▒░ ░ ▒▓ ░▒▓░
░▒ ░       ░▒ ░ ▒   ░ ▒ ▒░ ░░   ░▒ ░ ▓██ ░▒░     ░ ░▒  ░ ░   ░  ▒    ░▒ ░ ▒ ░ ░   ▒▒ ░▒ ░     ░ ░ ░    ░▒ ░ ▒ 
░░         ░░   ░ ░ ░ ░ ▒   ░    ░   ▒ ▒ ░░      ░  ░  ░   ░         ░░   ░   ░   ▒  ░░           ░    ░░   ░ 
            ░         ░ ░   ░    ░   ░ ░               ░   ░ ░        ░           ░           ░   ░     ░     
       
    
       ''')
typeproxy = int(input('''

[1] Http/Https
[2] Socks4
[3] Socks5
                      
>: '''))
if typeproxy == 1:
    out_file = "Https Proxies.txt"
    proxies = open(out_file, 'ab')
    r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt')
    r2 = requests.get('https://api.openproxylist.xyz/http.txt')
    proxies.write(r1.content)
    proxies.write(r2.content)
    num = 0
    for lines in r1.iter_lines():
      num += 1
      num2 = 0
      for lines in r2.iter_lines():
        num2 += 1
      length1 = num2 + num
      print(Fore.GREEN + f"   Done! Successfully added {length1} proxies, Check where this file is located.")
      proxies.close()
    
elif typeproxy == 2:
      out_file = "Socks4 Proxies.txt"
      proxies = open(out_file,'wb')
      r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt')
      r2 = requests.get('https://api.openproxylist.xyz/socks4.txt')
      proxies.write(r1.content)
      proxies.write(r2.content)
      num = 0
      for lines in r1.iter_lines():
        num += 1
      num2 = 0
      for lines in r2.iter_lines():
        num2 += 1
      length1 = num2 + num
      print(Fore.GREEN + f"   Done! Successfully added {length1} proxies, Check where this file is located.")
      proxies.close()

elif typeproxy == 3:
      r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt')
      r2 = requests.get('https://api.openproxylist.xyz/socks5.txt')
      out_file = "Socks5 Proxies.txt"
      proxies = open(out_file,'wb')
      proxies.write(r1.content)
      proxies.write(r2.content)
      num = 0
      for lines in r1.iter_lines():
        num += 1
      num2 = 0
      for lines in r2.iter_lines():
        num2 += 1
      length1 = num2 + num
      print(Fore.GREEN + f"   Done! Successfully added {length1} proxies, Check where this file is located.")
      proxies.close()
else:
      print("Invalid Option")
