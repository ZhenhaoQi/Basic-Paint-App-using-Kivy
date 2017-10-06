from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, Ellipse
from random import random
from kivy.uix.colorpicker import ColorPicker 
from kivy.properties import ListProperty
from kivy.uix.popup import Popup

clr=[1,1,0.5,1]
pre_clr=clr
def retclr():
    return clr

class Painter(Widget):
    
    col = ListProperty(clr)
    def on_touch_down(self, touch):
        self.col= retclr()
        if Widget.on_touch_down(self, touch):
            return True

        with self.canvas:
            Color(*self.col)
            d = 30
            Ellipse(pos=(touch.x - d / 2,touch.y - d / 2), size=(d,d))
            touch.ud['line'] = Line(points=(touch.x, touch.y),width=10)
         
    def on_touch_move(self, touch):
        
        touch.ud["line"].points += [touch.x, touch.y]

class Cpicker(ColorPicker):
    pass

class popup(Popup):
    def hello (self, y):
        global clr,pre_clr
        pre_clr=clr    
        clr=y 

class MainScreen(Screen):
    def open_it(self):
        popup().open()

    def eraser(self):
        global clr,pre_clr
        pre_clr = clr
        clr= [0,0,0,1]
    
    def pencil(self):
        global clr,pre_clr
        clr=pre_clr    


class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("kvf.kv")

class painApp(App):
    def build(self):
        print "start"
        return presentation

if __name__== "__main__":
    painApp().run()