#import
from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

#Uix import
from kivy.uix.behaviors import TouchRippleBehavior
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (350,600)

class MainScreen(Screen):
    pass

class FirstScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        return Builder.load_file('AppDesign.kv')

    def change_screen(self, screen, direction):
        self.root.transition.direction = direction
        self.root.current = screen

MainApp().run()
