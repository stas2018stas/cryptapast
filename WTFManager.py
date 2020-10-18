class WTFManager():
	# file = None
	# def initalize(txt):
	# file = open("output.txt", 'a')

	def writeToFile(file, index):
		file.write(index + '\n')

	def closeWrite(file):
		file.close()