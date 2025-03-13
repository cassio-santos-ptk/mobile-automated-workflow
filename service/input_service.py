from service.log_service import do_log_output
import subprocess
import time
import sys

DAEMON = "daemon not running"

def execute_command(command):
    try:                 
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE ,stderr=subprocess.PIPE, text=True)             

        output, error = process.communicate()

        #@todo handle error
        if error:
            print(f"[-] Error while executing command {command}")     
                      
        return output
            
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print("Error Output:", e.stderr)


def do_tap(x, y):    
    execute_command(f"adb shell input tap {x} {y}")
    do_sleep(4)

def do_input_text(data):        
    execute_command(f"adb shell input text {data}")

def do_sleep(amount):
    time.sleep(amount)

def do_restart(package):
    execute_command(f"adb shell am force-stop {package}")
    do_open(package)

def do_open(package):
    execute_command(f"adb shell monkey -p {package} -c android.intent.category.LAUNCHER 1")
    do_sleep(9)