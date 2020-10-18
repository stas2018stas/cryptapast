import os
import uuid
import time

class CryptographyManager():

	def crypt(dir):
		os.system("color 4")
		import pyAesCrypt
		print("----------------")
		key = str(uuid.uuid4())
		password = key
		bufferSize = 512 * 1024
		pyAesCrypt.encryptFile(str(dir), str(dir) + ".aes", password, bufferSize)
		os.remove(dir)
		print("YOUR FILE WAS SUCCESFULLY CRYPTED!")
		print(key)

	def encript(edir):
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
			CryptographyManager.encript(edir)
		os.system("color 7")