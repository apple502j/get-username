from gpath import *

def user_exist(uid):
    i=get_cat(uid)
    if cat_exist(i)[0] is False:
        return (False, '')
    j=load_cat(i)
    try:
        p=j[str(uid)]
        return (True,p)
    except:
        return (False,'')

def save_user(uid,n):
    if user_exist(uid)[0]:
        return
    i=get_cat(uid)
    create_cat(i)
    j=load_cat(i)[1]
    j[str(uid)]=n
    save_cat(i,j)
