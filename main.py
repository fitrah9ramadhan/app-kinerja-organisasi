from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from databaseAdmin import DataBaseAdmin
from databaseProker import DataBaseProker
from databaseAnggota import DataBaseAnggota

#Daftar Sebagai Admin
class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    tes = ObjectProperty(None)
    password = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0 and self.tes.text != "":
            if self.password != "":
                dbAdmin.add_user(self.email.text, self.password.text, self.namee.text, self.tes.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""
        self.tes.text = ""

#Login Admin
class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if dbAdmin.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass



class TambahAnggota(Screen):

    namaAnggota = ObjectProperty(None)
    komisariat = ObjectProperty(None)
    fakultas = ObjectProperty(None)
    jurusan = ObjectProperty(None)
    deputi = ObjectProperty(None)

    def tombol_tambah_anggota(self):
        if self.namaAnggota.text != "" and self.komisariat.text != "" and self.fakultas.text != "" and self.jurusan.text != "" and self.deputi.text != "":

            dbAnggota.add_anggota(self.namaAnggota.text, self.komisariat.text, self.fakultas.text, self.jurusan.text, self.deputi.text)

            self.tambah_anggota_berhasil_popup()
            self.reset()
            sm.current = "main"
        else:
            self.tambah_anggota_gagal_popup()
            self.reset()

    def tambah_anggota_berhasil_popup(self):

        pop = Popup(title = "Keterangan",
                        content = Label(text = "Berhasil Ditambahkan"),
                        size_hint = (None, None), size = (200, 200))
        pop.open()

    def tambah_anggota_gagal_popup(self):

        pop = Popup(title = "Keterangan", 
                    content = Label(text = "Gagal Ditambahkan"),
                    size_hint = (None, None),
                    size = (200,200))
        pop.open()

    def reset(self):
        self.namaAnggota.text = ""
        self.komisariat.text = ""
        self.fakultas.text = ""
        self.jurusan.text = ""
        self.deputi.text = ""

    def back(self):
        self.reset()
        sm.current = "main"





class TambahProker(Screen):

    nama_proker = ObjectProperty(None)
    deputi = ObjectProperty(None)
    pic = ObjectProperty(None)
    partisipan = ObjectProperty(None)

    def tombol_tambah_proker(self):
        if self.nama_proker.text != "" and self.deputi.text != "" and self.pic.text != "" and self.partisipan.text != "":

            dbProker.add_proker(self.nama_proker.text, self.deputi.text, self.pic.text, self.partisipan.text)

            self.tambah_proker_berhasil_popup()
        else:
            self.tambah_proker_gagal_popup()
            self.reset()

    def tambah_proker_berhasil_popup(self):
        pop = Popup(title = "Keterangan",
                        content = Label(text = "Berhasil Ditambah"),
                        size_hint = (None, None), size = (200, 200))
        pop.open()

    def tambah_proker_gagal_popup(self):

        pop = Popup(title = "Keterangan", 
                    content = Label(text = "Gagal Ditambahkan"),
                    size_hint = (None, None),
                    size = (200,200))
        pop.open()

    def reset(self):
        self.nama_proker.text = ""
        self.deputi.text = ""
        self.pic.text = ""
        self.partisipan.text = ""

    def back(self):
        self.reset()
        sm.current = "main"

class Credits(Screen):
    def back(self):
        sm.current = "main"

class LihatKeaktivan(Screen):
    namaAnggota = ObjectProperty(None)
    komisariat = ObjectProperty(None)

    def tombol_cari_anggota(self):

        if dbAnggota.validate(self.namaAnggota.text, self.komisariat.text):

            HasilAnggota.current = self.namaAnggota.text
            self.reset()
            sm.current = "hasang"
        else:
            invalidLogin()

    def reset(self):
        self.namaAnggota.text = ""
        self.komisariat.text = ""


class HasilAnggota(Screen):

    n = ObjectProperty(None)
    komisariatt = ObjectProperty(None)
    fakultass = ObjectProperty(None)
    jurusann = ObjectProperty(None)
    deputii = ObjectProperty(None)
    created = ObjectProperty(None)
    current = ""

    def on_enter(self, *args):
        komisariat, fakultas, jurusan, deputi, created = dbAnggota.get_anggota(self.current)

        self.n.text = "Nama Lengkap: " + self.current
        self.komisariatt.text = "Komisariat: " + komisariat
        self.fakultass.text = "Fakultas: " + fakultas
        self.jurusann.text = "Jurusan: " + jurusan
        self.deputii.text = "Deputi: " + deputi
        self.createdd.text = "Terdaftar pada Tanggal: " + created


        
def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

kv = Builder.load_file("my.kv")

sm = WindowManager()
dbAdmin = DataBaseAdmin("users.txt")
dbProker = DataBaseProker("prokers.txt")
dbAnggota = DataBaseAnggota("anggota.txt")

screens = [LoginWindow(name="login"), 
           CreateAccountWindow(name="create"),
           MainWindow(name="main"), 
           TambahProker(name = "tambpro"), 
           Credits(name = "credits"),
           TambahAnggota(name = "tambang"),
           LihatKeaktivan(name = "lihkea"),
           HasilAnggota(name = "hasang")]

for screen in screens:
    sm.add_widget(screen)

sm.current = "login"




class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
