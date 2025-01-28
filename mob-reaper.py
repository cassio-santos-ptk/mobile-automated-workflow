import subprocess
import sys
import os

PACKAGE_NAME = os.getenv("PACKAGE_NAME")

def execute_command(command):
    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # Print the command output
        print("* Output *")
        print(result.stdout)        
        
        # Print any error messages
        if result.stderr:
            print("Error Output:")
            print(result.stderr)
            sys.exit()

        return result.stdout
            
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print("Error Output:", e.stderr)


def open_app():
    # Example: Execute a simple command
    devices = execute_command(["adb", "devices"])  # Replace with your desired command
    if devices is None:
        print("[-] Mobile Device not connected")
        sys.exit()

    print("PN")
    print(PACKAGE_NAME)
    
    oppened_app = execute_command(["adb", "shell", "monkey", "-p", f"{PACKAGE_NAME}", "-c", "android.intent.category.LAUNCHER", "1"])
    

open_app()