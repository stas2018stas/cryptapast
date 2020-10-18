import os
import uuid

key = str(uuid.uuid4())

class CryptographyManager():

	def crypt(dir):
		os.system("color 4")
		import pyAesCrypt
		print("----------------")
		password = key
		bufferSize = 512 * 1024
		pyAesCrypt.encryptFile(str(dir), str(dir) + ".aes", password, bufferSize)
		os.remove(dir)
		print("YOUR FILE WAS SUCCESFULLY CRYPTED!")
		print(key)

	def encript(edir):
		import pyAesCrypt
		print("----------------")
		password = input("Enter key to encrypt your files: ")
		bufferSize = 512 * 1024
		r = os.path.splitext(edir)[0]
		if(password == key):
			pyAesCrypt.decryptFile(str(edir), str(r), password, bufferSize)
			os.remove(edir)
			print("ENCRYPTED!")
		else:
			time.sleep(1)
			print("WRONG KEY!")
			encript(edir)
		os.system("color 7")