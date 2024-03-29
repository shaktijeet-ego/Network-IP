import socket
import re
import datetime

from regex import regex

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
Timeoout = socket.getdefaulttimeout()
timeNow = datetime.datetime.now()
print("\n\n**System built to find the ip of the computer in which this software is hosted in**")
print("**Used for test purposes**")
print("-----------------------------------------------")
print("The current time is: " + str(timeNow))
print("------------------------------------------------")
print("hostname is : " + hostname)
print("Ip address: " + IPAddr)
print("Timeoout: " + str(Timeoout))
print("------------------------------------------------")

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''


def validIp(checkIP):
    # checkIP = input("Enter the required ip in 'XXX.XXX.XXX.XXX' Format: \n Eg: 192.168.0.1-255: "))
    if re.search(regex, checkIP):
        print("**Valid IP address**")
    else:
        print("**Invalid Ip address**")


while True:
    try:
        if __name__ == '__main__':
            checkIP = input("Enter the required ip in 'XXX.XXX.XXX.XXX' Format: \n Eg: 192.168.0.1-255: ")
            if checkIP == IPAddr:
                print("-----This ip belongs to " + hostname + " computer----")
                break
            else:
                print("This ip doesn't belong to this computer, Please check another")
                break
            validIp(checkIP)
    except ValueError:
        print("Enter valid IP")
