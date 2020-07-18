import datetime

class DataBaseAnggota:
	def __init__(self, filename):
		self.filename = filename
		self.anggotas = None
		self.file = None
		self.load()

	def load(self):
		self.file = open(self.filename, "r")
		self.anggotas = {}

		for line in self.file:
			namaAnggota, komisariat, fakultas, jurusan, angkatan, deputi, created = line.strip().split(";")
			self.anggotas[namaAnggota] = (komisariat, fakultas, jurusan, angkatan, deputi, created)

		self.file.close()

	def get_anggota(self, namaAnggota):
		if namaAnggota in self.anggotas:
			return self.anggotas[namaAnggota]
		else:
			return -1

	def add_anggota(self, namaAnggota, komisariat, fakultas, jurusan, angkatan, deputi):
		if namaAnggota.strip() not in self.anggotas:
			self.anggotas[namaAnggota.strip()] = (komisariat.strip(), fakultas.strip(), jurusan.strip(), angkatan.strip(), deputi.strip(), DataBaseAnggota.get_date())
			self.save()
			return 1
		else:
			print("Anggota ini sudah terdaftar")
			return -1

	def save(self):
		with open(self.filename, "w") as f:
			for anggota in self.anggotas:
				f.write(anggota + ";"+ self.anggotas[anggota][0] + ";" + self.anggotas[anggota][1] + ";" + self.anggotas[anggota][2] + ";" + self.anggotas[anggota][3] + ";" + self.anggotas[anggota][4] +self.anggotas[anggota][5]+";"  + "\n")

	@staticmethod
	def get_date():
		return str(datetime.datetime.now()).split(" ")[0]
