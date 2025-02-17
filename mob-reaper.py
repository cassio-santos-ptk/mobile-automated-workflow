import subprocess
import sys
import os
import re
import time

PACKAGE_NAME = os.getenv("PACKAGE_NAME")
DAEMON = "daemon not running"
retry  = 0

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
    do_tap(394, 613)

def do_sleep():
    time.sleep(9)

def do_tap(x, y):    
    execute_command(["adb", "shell", "input", "tap", f"{x}", f"{y}"])


def open_app():
    # Example: Execute a simple command
    devices = execute_command(["adb", "devices"])  # Replace with your desired command
    if not has_device(devices):
        print("[-] Mobile Device is not connected")
        sys.exit()

    print(f"[+] Initiating tests on: {PACKAGE_NAME}")
    
    #open the app
    execute_command(["adb", "shell", "monkey", "-p", f"{PACKAGE_NAME}", "-c", "android.intent.category.LAUNCHER", "1"])

    #wait initiate
    do_sleep()

    do_login()
    

open_app()