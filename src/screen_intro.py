'''
Created on 12 Feb 2019

@author: eD
'''
import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, ListProperty, NumericProperty, StringProperty # @UnresolvedImport
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.widget import Widget

import sys, os


# Kivy UI builder:
Builder.load_string("""

<IntroScreen>:

    intro_image:intro_image
    
    canvas:
        Color: 
            rgba: hex('#0D47A1ff')
        Rectangle: 
            size: self.size
            pos: self.pos
             
    BoxLayout:
        size: self.parent.size
        pos: self.parent.pos   
        
        orientation: 'vertical'
        spacing: 0
        size_hint_y: None
        height: 400
            
        Image:
            id: intro_image
            size: self.parent.size
            pos: self.parent.pos   

        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: 80
    
            Button:
                font_size: '30sp'
                markup: True
                text: 'Quit'
                on_press: root.sm.current = 'lobby'
    
            Button:
                font_size: '30sp'
                markup: True
                text: 'Go'
                on_press: root.sm.current = 'checking_screen'
        

""")


class IntroScreen(Screen):

    
    def __init__(self, **kwargs):
    
        super(IntroScreen, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']
        
    def on_enter(self):
        self.intro_image.source = './looms/' + self.sm.get_screen('lobby').loom_selected + '/intro_img.png' 
        