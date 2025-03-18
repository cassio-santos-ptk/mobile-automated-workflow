import sys
import os
import re
from service.input_service import execute_command, do_restart, do_open
from apps.andro_goat import mapping as androgoat_app
from service.log_service import log_splash
from service import vulnerability_service as vuln_service
from dotenv import load_dotenv
import os

# -    load the .env file   -
load_dotenv()

PACKAGE_NAME = os.getenv("PACKAGE_NAME")

#
# -    CHECK IF THERES DEVICES CONNECTED   -
#
def check_device():    
    devices = execute_command("adb devices")  
    if not has_device(devices):
        print("[-] Mobile Device is not connected")
        sys.exit()    

def has_device(devices):
    dvc = "device"
    matches = re.findall(dvc, devices)
    return len(matches) > 1

def do_test():

    # -     DEFINE THE MOCK DATA    -
    MOCK_USR = os.getenv("MOCK_USER_NAME")
    MOCK_PASWD = os.getenv("MOCK_PASSWORD")

    check_device()

    print(f"[+] Initiating tests on: {PACKAGE_NAME}")
    
    # -     OPEN THE APP     -
    do_open(PACKAGE_NAME)        

    #vuln_service.check_root(PACKAGE_NAME)

    #vuln_service.check_emulator(PACKAGE_NAME)

    # -     PERFORM THE SHARED PREFERENCES FLOW     -
    #androgoat_app.login_shared_pref_1()

    # -     LOOK TO SENSITIVE DATA ON SHARED PREF       -
    #vuln_service.search_shared_pref(MOCK_PASWD, PACKAGE_NAME)

    # -     RESTART THE APP      -
    #do_restart(PACKAGE_NAME)

    # -     PERFORM THE SQLITE FLOW
    #androgoat_app.login_sqlite()

    # -     LOOK TO SENSITIVE DATA ON SQLITE
    #vuln_service.search_sqlite(MOCK_USR, PACKAGE_NAME)

    #do_restart(PACKAGE_NAME)

    # -     PERFORM THE LOGGING FLOW 
    androgoat_app.login_insecure_logging()    

    # -     LOOK TO SENSITIVE DATA ON LOGS
 
    vuln_service.search_sensitive_log(MOCK_USR)
    vuln_service.search_sensitive_log(MOCK_PASWD)        

    #@todo check SSL pinning - use burp
    #@todo integrate with burp

    # -     CREATE THE .SARIF REPORT FILE
    vuln_service.build_report()

def main():
    log_splash()
    do_test()
    
main()