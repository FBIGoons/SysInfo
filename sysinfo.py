import platform
import socket
import os
import colorama 
import requests
import platform
import shutil
import sys
import time
import shutil
import winshell

from requests import get # For IP :/
from colorama import *
colorama.init()
import shutil


os.system("cls")
os.system("title SysInfo ^| Showing System Information")

# Get Local IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
local_ip_address = s.getsockname()[0]

# Get IP
ip = get('https://api.ipify.org').text


APP_Folder = 'C:/Windows/Temp'

totalFiles = 0

totalDir = 0

l = ['|', '/', '-', '\\']

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r' + f'  {Fore.LIGHTCYAN_EX}[*] Loading... {Fore.LIGHTYELLOW_EX}'+i)
		sys.stdout.flush()
		time.sleep(0.6)


def TempDelete():
    del_dir = r'C:/Windows/Temp'
    for f in os.listdir(del_dir):
        if os.path.isfile(r'C:/Windows/Temp//'+f):
            os.remove(r'C:/Windows/Temp//'+f)
        elif os.path.isdir(r'C:/Windows/Temp//'+f):
            shutil.rmtree(r'C:/Windows/Temp//'+f, ignore_errors=True)


def RBin():
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)


for base, dirs, files in os.walk(APP_Folder):
    for directories in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1



print(f'''
    {Fore.LIGHTCYAN_EX}
    ███████╗██╗   ██╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
    ██╔════╝╚██╗ ██╔╝██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
    ███████╗ ╚████╔╝ ███████╗██║██╔██╗ ██║█████╗  ██║   ██║
    ╚════██║  ╚██╔╝  ╚════██║██║██║╚██╗██║██╔══╝  ██║   ██║
    ███████║   ██║   ███████║██║██║ ╚████║██║     ╚██████╔╝
    ╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                       

'''+ Fore.RESET)

print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Computer Name: {os.environ['COMPUTERNAME']}{Fore.RESET}")
print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Local IP Address: {local_ip_address}{Fore.RESET}")
print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}IP Address: {ip}{Fore.RESET}")
print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Platform: {platform.platform()}{Fore.RESET}")
print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System: {platform.system()} {platform.release()}{Fore.RESET}")
print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Version: {platform.version()}{Fore.RESET}")
print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Machine: {platform.machine()}{Fore.RESET}\n")

print(f"  {Fore.LIGHTCYAN_EX}════════════════════════════════════════════════════════════════════════════\n")

print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Counting Files in Temp Folder {Fore.LIGHTCYAN_EX}{Fore.RESET}\n")

Spinner()

os.system("cls")

print(f'''
    {Fore.LIGHTCYAN_EX}
    ███████╗██╗   ██╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
    ██╔════╝╚██╗ ██╔╝██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
    ███████╗ ╚████╔╝ ███████╗██║██╔██╗ ██║█████╗  ██║   ██║
    ╚════██║  ╚██╔╝  ╚════██║██║██║╚██╗██║██╔══╝  ██║   ██║
    ███████║   ██║   ███████║██║██║ ╚████║██║     ╚██████╔╝
    ╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                       

'''+ Fore.RESET)

print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Computer Name: {os.environ['COMPUTERNAME']}{Fore.RESET}")
print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Local IP Address: {local_ip_address}{Fore.RESET}")
print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}IP Address: {ip}{Fore.RESET}")
print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Platform: {platform.platform()}{Fore.RESET}")
print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System: {platform.system()} {platform.release()}{Fore.RESET}")
print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Version: {platform.version()}{Fore.RESET}")
print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Machine: {platform.machine()}{Fore.RESET}\n")

print(f"  {Fore.LIGHTCYAN_EX}════════════════════════════════════════════════════════════════════════════\n")

print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Number Of Files Found In Temp Folder: {Fore.RESET}{totalFiles} {Fore.LIGHTCYAN_EX}{Fore.RESET}")
print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Number Of Directories Found In Temp Folder: {Fore.RESET}{totalDir} {Fore.LIGHTCYAN_EX}{Fore.RESET}\n")

cleantemp = input(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Would You like to clean the Temp Files? [y/n]: {Fore.RESET}")

if cleantemp == 'y':
    os.system("cls")
    print(f'''
    {Fore.LIGHTCYAN_EX}
    ███████╗██╗   ██╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
    ██╔════╝╚██╗ ██╔╝██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
    ███████╗ ╚████╔╝ ███████╗██║██╔██╗ ██║█████╗  ██║   ██║
    ╚════██║  ╚██╔╝  ╚════██║██║██║╚██╗██║██╔══╝  ██║   ██║
    ███████║   ██║   ███████║██║██║ ╚████║██║     ╚██████╔╝
    ╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                       

    '''+ Fore.RESET)

    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Computer Name: {os.environ['COMPUTERNAME']}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Local IP Address: {local_ip_address}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}IP Address: {ip}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Platform: {platform.platform()}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System: {platform.system()} {platform.release()}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Version: {platform.version()}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Machine: {platform.machine()}{Fore.RESET}\n")

    print(f"  {Fore.LIGHTCYAN_EX}════════════════════════════════════════════════════════════════════════════\n")

    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Please Wait While We Delete Temp Files And Directories{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")
    TempDelete()

    Spinner()

    os.system('cls')

    
    print(f'''
    {Fore.LIGHTCYAN_EX}
    ███████╗██╗   ██╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
    ██╔════╝╚██╗ ██╔╝██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
    ███████╗ ╚████╔╝ ███████╗██║██╔██╗ ██║█████╗  ██║   ██║
    ╚════██║  ╚██╔╝  ╚════██║██║██║╚██╗██║██╔══╝  ██║   ██║
    ███████║   ██║   ███████║██║██║ ╚████║██║     ╚██████╔╝
    ╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                       

    '''+ Fore.RESET)

    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Computer Name: {os.environ['COMPUTERNAME']}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Local IP Address: {local_ip_address}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}IP Address: {ip}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Platform: {platform.platform()}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System: {platform.system()} {platform.release()}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Version: {platform.version()}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Machine: {platform.machine()}{Fore.RESET}\n")

    print(f"  {Fore.LIGHTCYAN_EX}════════════════════════════════════════════════════════════════════════════\n")

    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Successfully Deleted Temp Files And Directories!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")
    time.sleep(0.3)
    rbin = input(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Would You like to clean the Recycle Bin? [y/n]: {Fore.RESET}")

    if rbin == "y":
        os.system("cls")
        print(f'''
        {Fore.LIGHTCYAN_EX}
        ███████╗██╗   ██╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
        ██╔════╝╚██╗ ██╔╝██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
        ███████╗ ╚████╔╝ ███████╗██║██╔██╗ ██║█████╗  ██║   ██║
        ╚════██║  ╚██╔╝  ╚════██║██║██║╚██╗██║██╔══╝  ██║   ██║
        ███████║   ██║   ███████║██║██║ ╚████║██║     ╚██████╔╝
        ╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                        

        '''+ Fore.RESET)

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Computer Name: {os.environ['COMPUTERNAME']}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Local IP Address: {local_ip_address}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}IP Address: {ip}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Platform: {platform.platform()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System: {platform.system()} {platform.release()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Version: {platform.version()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Machine: {platform.machine()}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}════════════════════════════════════════════════════════════════════════════\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Successfully Deleted Temp Files And Directories!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Please Wait While We Delete Recycle Bin Files!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")
        RBin()
        Spinner()

        os.system('cls')

        
        print(f'''
        {Fore.LIGHTCYAN_EX}
        ███████╗██╗   ██╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
        ██╔════╝╚██╗ ██╔╝██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
        ███████╗ ╚████╔╝ ███████╗██║██╔██╗ ██║█████╗  ██║   ██║
        ╚════██║  ╚██╔╝  ╚════██║██║██║╚██╗██║██╔══╝  ██║   ██║
        ███████║   ██║   ███████║██║██║ ╚████║██║     ╚██████╔╝
        ╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                        

        '''+ Fore.RESET)

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Computer Name: {os.environ['COMPUTERNAME']}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Local IP Address: {local_ip_address}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}IP Address: {ip}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Platform: {platform.platform()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System: {platform.system()} {platform.release()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Version: {platform.version()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Machine: {platform.machine()}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}════════════════════════════════════════════════════════════════════════════\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Successfully Deleted Temp Files And Directories!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Successfully Cleaned Recycle Bin!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Script Is Complete!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")

        i = input()
    elif rbin == "n":
        os.system("cls")
        print(f'''
        {Fore.LIGHTCYAN_EX}
        ███████╗██╗   ██╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
        ██╔════╝╚██╗ ██╔╝██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
        ███████╗ ╚████╔╝ ███████╗██║██╔██╗ ██║█████╗  ██║   ██║
        ╚════██║  ╚██╔╝  ╚════██║██║██║╚██╗██║██╔══╝  ██║   ██║
        ███████║   ██║   ███████║██║██║ ╚████║██║     ╚██████╔╝
        ╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                        

        '''+ Fore.RESET)

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Computer Name: {os.environ['COMPUTERNAME']}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Local IP Address: {local_ip_address}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}IP Address: {ip}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Platform: {platform.platform()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System: {platform.system()} {platform.release()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Version: {platform.version()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Machine: {platform.machine()}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}════════════════════════════════════════════════════════════════════════════\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Successfully Deleted Temp Files And Directories!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Skipped Cleaning Recycle Bin!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Script Is Complete!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")
        
       

        





elif cleantemp == "n":
    os.system('cls')

    
    print(f'''
    {Fore.LIGHTCYAN_EX}
    ███████╗██╗   ██╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
    ██╔════╝╚██╗ ██╔╝██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
    ███████╗ ╚████╔╝ ███████╗██║██╔██╗ ██║█████╗  ██║   ██║
    ╚════██║  ╚██╔╝  ╚════██║██║██║╚██╗██║██╔══╝  ██║   ██║
    ███████║   ██║   ███████║██║██║ ╚████║██║     ╚██████╔╝
    ╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                       

    '''+ Fore.RESET)

    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Computer Name: {os.environ['COMPUTERNAME']}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Local IP Address: {local_ip_address}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}IP Address: {ip}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Platform: {platform.platform()}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System: {platform.system()} {platform.release()}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Version: {platform.version()}{Fore.RESET}")
    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Machine: {platform.machine()}{Fore.RESET}\n")

    print(f"  {Fore.LIGHTCYAN_EX}════════════════════════════════════════════════════════════════════════════\n")

    print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Skipped Cleaning Temp Folders And Directories!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")
    time.sleep(0.3)
    rbin2 = input(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Would You like to clean the Recycle Bin? [y/n]: {Fore.RESET}")

    if rbin2 == "n":
        os.system("cls")
        print(f'''
        {Fore.LIGHTCYAN_EX}
        ███████╗██╗   ██╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
        ██╔════╝╚██╗ ██╔╝██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
        ███████╗ ╚████╔╝ ███████╗██║██╔██╗ ██║█████╗  ██║   ██║
        ╚════██║  ╚██╔╝  ╚════██║██║██║╚██╗██║██╔══╝  ██║   ██║
        ███████║   ██║   ███████║██║██║ ╚████║██║     ╚██████╔╝
        ╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                        

        '''+ Fore.RESET)

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Computer Name: {os.environ['COMPUTERNAME']}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Local IP Address: {local_ip_address}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}IP Address: {ip}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Platform: {platform.platform()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System: {platform.system()} {platform.release()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Version: {platform.version()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Machine: {platform.machine()}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}════════════════════════════════════════════════════════════════════════════\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Skipped Cleaning Temp Folders And Directories!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Skipped Cleaning Recycle Bin!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Script Is Complete!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")
    
    elif rbin2 == "y":
        os.system("cls")
        print(f'''
        {Fore.LIGHTCYAN_EX}
        ███████╗██╗   ██╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
        ██╔════╝╚██╗ ██╔╝██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
        ███████╗ ╚████╔╝ ███████╗██║██╔██╗ ██║█████╗  ██║   ██║
        ╚════██║  ╚██╔╝  ╚════██║██║██║╚██╗██║██╔══╝  ██║   ██║
        ███████║   ██║   ███████║██║██║ ╚████║██║     ╚██████╔╝
        ╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                        

        '''+ Fore.RESET)

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Computer Name: {os.environ['COMPUTERNAME']}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Local IP Address: {local_ip_address}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}IP Address: {ip}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Platform: {platform.platform()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System: {platform.system()} {platform.release()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Version: {platform.version()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Machine: {platform.machine()}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}════════════════════════════════════════════════════════════════════════════\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Skipped Cleaning Temp Folders And Directories!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Please Wait While We Delete Recycle Bin Files!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")
        
        RBin()
        Spinner()

        os.system('cls')

        
        print(f'''
        {Fore.LIGHTCYAN_EX}
        ███████╗██╗   ██╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
        ██╔════╝╚██╗ ██╔╝██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
        ███████╗ ╚████╔╝ ███████╗██║██╔██╗ ██║█████╗  ██║   ██║
        ╚════██║  ╚██╔╝  ╚════██║██║██║╚██╗██║██╔══╝  ██║   ██║
        ███████║   ██║   ███████║██║██║ ╚████║██║     ╚██████╔╝
        ╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                        

        '''+ Fore.RESET)

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Computer Name: {os.environ['COMPUTERNAME']}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Local IP Address: {local_ip_address}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}IP Address: {ip}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Platform: {platform.platform()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System: {platform.system()} {platform.release()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Version: {platform.version()}{Fore.RESET}")
        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}System Machine: {platform.machine()}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}════════════════════════════════════════════════════════════════════════════\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Successfully Deleted Temp Files And Directories!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Successfully Cleaned Recycle Bin!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")

        print(f"  {Fore.LIGHTCYAN_EX}[+] {Fore.LIGHTYELLOW_EX}Script Is Complete!{Fore.LIGHTCYAN_EX}{Fore.RESET}\n")



            
