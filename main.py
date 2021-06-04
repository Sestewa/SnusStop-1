#import
from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.properties import BooleanProperty, NumericProperty, ObjectProperty, StringProperty
from kivymd.theming import ThemableBehavior
from kivy.animation import Animation
from kivy.clock import Clock

#Uix import
from kivy.uix.behaviors import TouchRippleBehavior
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.carousel import Carousel
from kivymd.uix.picker import MDDatePicker


Window.size = (350,600)

class LoginScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class HelpScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class SparetScreen(Screen):
    pass

class ArticleScreen(Screen):
    pass

class SettingScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

class DrawerList(ThemableBehavior, MDList):
    pass

class YourCarousel(Carousel):
    pass


class MainApp(MDApp):
    #en defination der gør at når vi nævner den kan vi skifter til en anden skærm i den direktion vi vil have
    def change_screen(self, screen, direction):
        self.root.transition.direction = direction
        self.root.current = screen
    #En defination der tager og bygger programmet op ved at loade kivy filen
    def build(self):
        return Builder.load_file('AppDesign.kv')

    #En defination der gemmer dataen fra hvad man vælger i datovælgeren og printer den
    def on_save(self, instance, value, date_range):
        print(instance, value, date_range)
    #en defination der gør at når brugeren cancler at der kan ske noget
    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
    #her har vi definationen for at vise datoen og give muligheden for at vælge og lukke den
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


#Så beder vi om at klassen MainApp skal køre som er vores mainframe af programmet
MainApp().run()
