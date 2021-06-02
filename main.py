#import
from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty
from kivymd.theming import ThemableBehavior

#Uix import
from kivy.uix.behaviors import TouchRippleBehavior
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList


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



class MainApp(MDApp):
    def build(self):
        return Builder.load_file('AppDesign.kv')


    def change_screen(self, screen, direction):
        self.root.transition.direction = direction
        self.root.current = screen

    def on_start(self):
        icons_item = {
        "folder": "My files",
        "account-multiple": "Shared with me",
        "star": "Starred",
        "history": "Recent",
        "checkbox-marked": "Shared with me",
        "upload": "Upload",
        }
        for icon_name in icons_item.keys():
            self.root.ids.drawer.ids.md_list.add_widget(
            ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )


MainApp().run()
