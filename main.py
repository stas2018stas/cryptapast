import os
import uuid
import time
import sqlite3
from CryptographyManager import CryptographyManager as cm


# LOGO
print("CRYPTAPAST V1.0.0.0")

# MAIN
file = input("Enter file name(without .aes if you want to decrypt): ")
want = input("if you want encrypt your file, write 'e' without brackets or you can write 'd' to perform the opposite action: ")
if(want == "e"):
	cm.encrypt(file)
elif(want == "d"):
	cm.decrypt(file + ".aes")
else:
	print("You write wrong letter =(")
