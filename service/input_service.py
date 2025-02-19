from service.log_service import do_log_output
import subprocess
import time
import sys

DAEMON = "daemon not running"

def execute_command(command):
    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # Print the command output
        do_log_output(result.stdout)         
        
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


def do_tap(x, y):    
    execute_command(["adb", "shell", "input", "tap", f"{x}", f"{y}"])
    do_sleep(4)

def do_input_text(data):        
    execute_command(["adb", "shell", "input", "text", f"{data}"])

def do_sleep(amount):
    time.sleep(amount)