from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import BoxLayout

class MD3Card(BoxLayout):
    pass

class BoxLayout(BoxLayout):
    pass

#login screen
class LoginWindow(Screen):
    pass



#createWindow
class CreateWindow(Screen):
    pass



#DashboardWindow
class DashboardWindow(Screen):
    pass



#TrainingWindow
class TrainingWindow(Screen):
    pass



#accidentWindow
class AccidentWindow(Screen):
    pass



#safetyWindow
class SafetyWindow(Screen):
    pass



#ActivityWindow
class ActivityWindow(Screen):
    pass


# screen manager
class ScreenManager(ScreenManager):
    pass



# main class
class MainApp(MDApp):
    def build(self):
        screen = Builder.load_file("Main.kv")
        return screen

# run app
if __name__ == "__main__":
    MainApp().run()