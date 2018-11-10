""" Recrusive Following """
from following import do as f_do

def do(user):
    while user!="":
        print(f"doing: who {user} follows")
        user=f_do(user)
