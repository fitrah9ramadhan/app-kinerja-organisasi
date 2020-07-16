from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class Login(Screen):
	pass


class Beranda(Screen):
	pass


class Registrasi(Screen):
	pass


class WindowManager(ScreenManager):
	pass


kv = Builder.load_file("my.kv")

class MyMainApp(App):
	def build(self):
		return kv

if __name__ == "__main__":
	MyMainApp().run()
