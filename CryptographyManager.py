import os
import uuid
import time
from WTFManager import WTFManager as wtf

class CryptographyManager():

	def encrypt(dir):
		os.system("color 4")
		import pyAesCrypt
		print("----------------")
		key = str(uuid.uuid4())
		password = key
		bufferSize = 512 * 1024
		pyAesCrypt.encryptFile(str(dir), str(dir) + ".aes", password, bufferSize)
		os.remove(dir)
		print("YOUR FILE WAS SUCCESFULLY CRYPTED!")
		print("If you want to decrypt your file, see output.txt into your Documents folder.")
		input("Press Enter for finished process!")
		os.system("color 7")
		from os.path import expanduser
		f = open(expanduser("~") + "\\Documents\\output.txt", 'a')
		wtf.writeToFile(f, "Your key for decryption " + str(dir) + " file:")
		wtf.writeToFile(f, key)
		wtf.writeToFile(f, "")
		wtf.closeWrite(f)


	def decrypt(edir):
		os.system("color 2")
		import pyAesCrypt
		print("----------------")
		password = input("Enter key to decrypt your files: ")
		bufferSize = 512 * 1024
		r = os.path.splitext(edir)[0]
		try:
			pyAesCrypt.decryptFile(str(edir), str(r), password, bufferSize)
			os.remove(edir)
			print("ENCRYPTED!")
		except:
			time.sleep(1)
			print("WRONG KEY!")
			CryptographyManager.encrypt(edir)
		os.system("color 7")