import datetime

class DataBaseProker:
	def __init__(self, filename):
		self.filename = filename
		self.prokers = None
		self.file = None
		self.load()

	def load(self):
		self.file = open(self.filename, "r")
		self.prokers = {}

		for line in self.file:
			namaProker, deputi, pic, partisipan, created = line.strip().split(";")
			self.prokers[namaProker] = (deputi, pic, partisipan, created)

		self.file.close()

	def get_proker(self, namaProker):
		if namaProker in self.prokers:
			return self.prokers[namaProker]
		else:
			return -1

	def add_proker(self, namaProker, deputi, pic, partisipan):
		if namaProker.strip() not in self.prokers:
			self.prokers[namaProker.strip()] = (deputi.strip(), pic.strip(), partisipan.strip(), DataBaseProker.get_date())
			self.save()
			return 1
		else:
			print("Proker ini sudah terdaftar")
			return -1


	def save(self):
		with open(self.filename, "w") as f:
			for proker in self.prokers:
				f.write(proker + ";" + self.prokers[proker][0] + ";" + self.prokers[proker][1] + ";" + self.prokers[proker][2] + ";" + self.prokers[proker][3] + "\n")

	@staticmethod
	def get_date():
		return str(datetime.datetime.now()).split(" ")[0]
