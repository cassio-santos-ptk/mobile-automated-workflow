import subprocess
import sys
import os
import re
import time

PACKAGE_NAME = os.getenv("PACKAGE_NAME")
DAEMON = "daemon not running"
retry  = 0

mock_data = {
    "username":"user",
    "password":"password123"
}

def execute_command(command):
    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # Print the command output
        print("* Output *")
        print(result.stdout)   
        
        # Print error messages if have it
        if(result.returncode != 0 and result.stderr):            
            if(DAEMON in result.stderr and retry <1):
                retry +=1
                print(result.stderr)
                print("Retrying ..")
                execute_command(command)                

            print("Error Output:")
            print(result.stderr)
            sys.exit()

        return result.stdout
            
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print("Error Output:", e.stderr)

def has_device(devices):
    dvc = "device"
    matches = re.findall(dvc, devices)
    
    return len(matches) > 1

def do_login():
    do_tap(395, 809)
    do_tap(382, 509)
    # digitar user
    do_input_text(mock_data['username'])
    # tap pass
    # digitar pass
    # tap save

def do_input_text(data):        
    execute_command(["adb", "shell", "input", "text", f"{data}"])


def do_sleep(amount):
    time.sleep(amount)

def do_tap(x, y):    
    execute_command(["adb", "shell", "input", "tap", f"{x}", f"{y}"])
    do_sleep(4)


def open_app():
    #check the devices connected by adb
    devices = execute_command(["adb", "devices"])  
    if not has_device(devices):
        print("[-] Mobile Device is not connected")
        sys.exit()

    print(f"[+] Initiating tests on: {PACKAGE_NAME}")
    
    #open the app
    execute_command(["adb", "shell", "monkey", "-p", f"{PACKAGE_NAME}", "-c", "android.intent.category.LAUNCHER", "1"])

    #wait initiate
    do_sleep(9)

    do_login()
    

open_app()