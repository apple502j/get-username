""" Get path """
import os, os.path, json

cpath = os.getcwd()


def get_cat(n):
    return n//100000

def cat_exist(cid):
    p=os.path.join("..", "data", str(cid)+".json")
    if os.path.exists(p):
        try:
            with open(p,"r") as f:
                if f.read().strip():
                    return (True, p)
                else:
                    return (False, p)
        except:
            return (False, p)
    else:
        return (False, p)

def create_cat(cid):
    e, p=cat_exist(cid)
    if e:
        return p
    with open(p, "w+") as f:
        f.write("{\n}")
    return p

def load_cat(cid):
    p=create_cat(cid)
    with open(p,"r") as f:
        return (p, json.load(f))

def save_cat(cid, j):
    #print("savecat {},{}".format(cid,j))
    p=create_cat(cid)
    with open(p, "w") as f:
        json.dump(j,f)
