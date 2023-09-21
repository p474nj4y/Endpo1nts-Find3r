import requests
import pyfiglet

xdxd = pyfiglet.figlet_format("Endpoints\nf1nd3r ", font = "slant"  )
print(xdxd) 
ydyd = pyfiglet.figlet_format("Coded w/ <3 By - @p474nj4y", font = "digital" )
print(ydyd)


def checkpoint(url) :
    response = requests.get(url)
    if response.status_code == 200 :
        print(f"endpoint found >{url}")
    else :
        print(f"endpoint not found >{url}")

yoururl = input("enter your url : ")
yourwordlist = input("enter your wordlist : ")

try :
    file = open(yourwordlist,"r")
    paths = [line.strip() for line in file.readlines()]

    for path in paths :
        fullurl = yoururl + "/" + path  
        checkpoint(fullurl)




except FileNotFoundError :
    print(f"your file doesn't exists :{yourwordlist}")