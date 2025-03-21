import os
from common import helper
from apps.andro_goat import manager as androgoat
from apps.va_lottery import manager as vallotery
from service.log_service import log_splash
from dotenv import load_dotenv
import os

""""

    Main file. Responsible for centralize all the supported applications

"""

# -    load the .env file   -
load_dotenv()

PACKAGE_NAME = os.getenv("PACKAGE_NAME")

def do_test():

    helper.check_device()
    print(f"[+] Initiating tests on: {PACKAGE_NAME}")

    match PACKAGE_NAME:
        case "owasp.sat.agoat":
            androgoat.do_test(PACKAGE_NAME)
        case "com.va.lottery.uat":
            vallotery.do_test(PACKAGE_NAME)
        case _:
            print(f"[-] Error: The application is not mapped: {PACKAGE_NAME}")        

def main():
    log_splash()
    do_test()
    
main()