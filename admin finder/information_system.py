#coded by green cyber and prof.wolf
#team: wolf cyber security
#black hat hacker of iran

from time import sleep



def information():
    try:
        try:
            import socket
        except:
            print("please install socket")
        try:
            import time
        except:
            print("please install time ")
        try:
            import platform
        except:
            print("please install platform")
        try:
            import os
        except:
            print("please install os")
        try:
            import getpass
        
        except:
            print("please install getpass") 
        try:
            import requests
        except:
            print("please install reqests")
        #importing librarys
        ########################################################
        os.system("cls" or "clear")
        #######################################################
        
        system_name = getpass.getuser()
        #python_version = os.system("python --version")
        system_os = platform.uname()
        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        my_ip = ip_request.json()['ip']
        #######################################################
        print(f"Hello {system_name}:)")
        print("internet:"+"conecct")
        time.sleep(.5)
        print("System name: "+system_name)
        time.sleep(.5)
        print("os: "+system_os[0])
        time.sleep(.5)
        print("node: "+system_os[1])
        time.sleep(.5)
       # print("python version: "+python_version)
        time.sleep(.5)
        print("release: "+system_os[2])
        time.sleep(.5)
        print("version: "+system_os[3])
        time.sleep(.5)
        print("machine: "+system_os[4])
        time.sleep(.5)
        print("ip: " +my_ip)
        time.sleep(.5)
        print("cpu: "+platform.processor())
        time.sleep(.5)
    except:
        print("[!]please conect to internet first")

#coded by green cyber and prof.wolf
#team: wolf cyber security
#black hat hacker of iran