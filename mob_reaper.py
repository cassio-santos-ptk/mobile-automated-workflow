import sys
import os
import re
from service.input_service import execute_command, do_restart, do_open
from apps.andro_goat import mapping as androgoat_app
from service.log_service import log_splash
from service import vulnerability_service as vuln_service
from config import shared
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

PACKAGE_NAME = os.getenv("PACKAGE_NAME")
retry  = 0


def has_device(devices):
    dvc = "device"
    matches = re.findall(dvc, devices)
    return len(matches) > 1

def check_device():    
    #check the devices connected by adb
    devices = execute_command("adb devices")  
    if not has_device(devices):
        print("[-] Mobile Device is not connected")
        sys.exit()    

def open_app():

    check_device()

    #@todo 0 add an env file with all the known apps and relate them with the folder, providing more abstraction
    
    log_splash()
    print(f"[+] Initiating tests on: {PACKAGE_NAME}")
    
    #open the app
    do_open(PACKAGE_NAME)        

    #check for root detection
    #vuln_service.check_root(PACKAGE_NAME)

    #check for emulator detection
    #vuln_service.check_emulator(PACKAGE_NAME)

    #androgoat_app.login_shared_pref_1()

    #@todo check if sensitive data are stored on shared pref

    #do_restart(PACKAGE_NAME)

    #androgoat_app.login_sqlite()

    #@todo check if sensitive data are stored on sqlite

    #do_restart(PACKAGE_NAME)

    androgoat_app.login_insecure_logging()
        
    #search for sensitive logfed information - password
    vuln_service.search_sensitive_log(shared.mock_data['password']) 

    vuln_service.build_report()

    #@todo check the apk signature

    #@todo check the min sdk

    #@todo look to manifest common issues

def main():
    open_app()
    #print("skipin this for a while ..")
    
main()