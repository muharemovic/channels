# Author: Ramiz Muharemovic
# https://github.com/muharemovic
from urllib.request import urlopen
import getpass
import urllib,urllib.parse
from sys import platform as OS


print("\t\tKanali, VLC playerom otvoriti")
korisnik = getpass.getuser()

def skinuti():
    STRANICA = "http://lalsbenpn.weebly.com/uploads/5/7/9/7/57972205/lista.txt"
    txt = urlopen(STRANICA).read().decode('utf-8')
    url = STRANICA
    split = urllib.parse.urlsplit(txt)

    netfilename = split.path.split("/")[-1]  # add to list -1
    datum_kanala = netfilename[:-4]
    print("Datum kanala:",datum_kanala)
    print("Skinuti:")
    print("1-Da")
    izbor=input("Unesi izbor: ")

    if izbor =="1":
        if OS == "win32":
            downloadfile = ("C:\\Users\\"+korisnik+"\\Desktop\\"+netfilename)
            urllib.request.urlretrieve(txt,downloadfile)
            input("Kanali skinuti na Desktop")
        elif OS == "linux" or OS == "linux2":
            downloadfile = ("/home/"+korisnik+"/Documents/"+netfilename)
            urllib.request.urlretrieve(txt,downloadfile)
            input("Kanali skinuti u Documents")
        elif OS == "darwin":
            downloadfile = ("/Users/"+korisnik+"/Desktop/"+netfilename)
            urllib.request.urlretrieve(txt,downloadfile)
            input("Kanali skinuti na Desktop")
        
        
    else:
        print("")
        
try:
    skinuti()
except:
    print("Greška")




