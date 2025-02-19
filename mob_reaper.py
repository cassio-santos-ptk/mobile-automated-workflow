import sys
import os
import re
from service.input_service import execute_command, do_sleep
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

    print(f"[+] Initiating tests on: {PACKAGE_NAME}")
    
    #open the app
    execute_command(["adb", "shell", "monkey", "-p", f"{PACKAGE_NAME}", "-c", "android.intent.category.LAUNCHER", "1"])

    #wait initiate
    do_sleep(9)

    androgoat_app.login_data_storage_1()

def main():
    open_app()
    

main()