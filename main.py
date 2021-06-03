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

Window.size = (350,600)

class HomeScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class MoneyScreen(Screen):
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
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class YourCarousel(Carousel):
    pass




class MainApp(MDApp):
    data = {
        'language-python': 'Python',
        'language-php': 'PHP',
        'git': 'Git',
    }


    def change_screen(self, screen, direction):
        self.root.transition.direction = direction
        self.root.current = screen


    def build(self):
        return Builder.load_file('appDesigntest.kv')


MainApp().run()
