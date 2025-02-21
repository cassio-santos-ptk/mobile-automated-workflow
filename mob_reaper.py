import sys
import os
import re
from service.input_service import execute_command, do_restart, do_open
from apps.andro_goat import mapping as androgoat_app

PACKAGE_NAME = os.getenv("PACKAGE_NAME")
retry  = 0

def has_device(devices):
    dvc = "device"
    matches = re.findall(dvc, devices)
    return len(matches) > 1

def check_device():    
    #check the devices connected by adb
    devices = execute_command(["adb", "devices"])  
    if not has_device(devices):
        print("[-] Mobile Device is not connected")
        sys.exit()    

def open_app():

    check_device()

    #@todo add an env file with all the known apps and relate them with the folder, providing more abstraction

    print(f"[+] Initiating tests on: {PACKAGE_NAME}")
    
    #open the app
    do_open(PACKAGE_NAME)    

    #@todo add an validation that checks that the app is still running on an root environment and did not displayed
    #anything about on the screen

    #@todo add an validation that checks that the app is still running on an emulator environment and did not displayed
    #anything about on the screen

    androgoat_app.login_shared_pref_1()

    do_restart(PACKAGE_NAME)

    androgoat_app.login_sqlite()

    do_restart(PACKAGE_NAME)

    androgoat_app.login_insecure_logging()

    #@todo check the logs with logcat and verify if the credentials is outputed

    #@todo check the apk signature

    #@todo check the min sdk

    #@todo look to manifest common issues


def main():
    open_app()
    
main()