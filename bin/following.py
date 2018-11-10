""" Following trick """
import requests # not scratchapi2
import time
import gid
from random import randint

def do(user):
    offset=0
    xxx=""
    while True:
        req=requests.get("https://api.scratch.mit.edu/users/{}/following?limit=40&offset={}"
                         .format(user,offset))
        try:
            j=req.json()
            _=j[0]
        except:
            break
        offset+=40
        for u in j:
            print("{0} is {1}".format(u["id"],u["username"]))
            gid.save_user(u["id"], u["username"])
            if randint(1,10)>7:
                xxx=u["username"]
        time.sleep(1)
    return xxx            
