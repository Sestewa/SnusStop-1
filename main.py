#import
from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.properties import ObjectProperty
#Uix import
from kivy.uix.behaviors import TouchRippleBehavior
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout


Window.size = (350,600)



class HomeScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class SettingScreen(Screen):
    pass


class ScreenManager(ScreenManager):
    pass


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class MainApp(MDApp):
    def build(self):
        return Builder.load_file('AppDesign.kv')

    def change_screen(self, screen, direction):
        self.root.transition.direction = direction
        self.root.current = screen

MainApp().run()
