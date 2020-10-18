import os
import uuid
import time
import sqlite3
from CryptographyManager import CryptographyManager as cm
from SqliteManager import SqliteManager as sm


sm.connectToDatabase("data.db")
file = input("Enter file name: ")
cm.crypt(file)
cm.encript(file + ".aes")
