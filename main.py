import os
import uuid
import time
import sqlite3
from CryptographyManager import CryptographyManager as cm
from SqliteManager import SqliteManager as sm


sm.connectToDatabase("data.db")

print("CRYPTAPAST V0.1.0.0")
file = input("Enter file name(without .aes if you want to decrypt): ")
want = input("if you want encrypt your file, write 'e' without brackets or you can write 'd' to perform the opposite action")
if(want == "e"):
	cm.crypt(file)
elif(want == "d"):
	cm.encript(file + ".aes")
else:
	print("You write wrong letter =(")
