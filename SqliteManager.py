import sqlite3
class SqliteManager():
	def connectToDatabase(base):
		conn = sqlite3.connect(base)
		cursor = conn.cursor()