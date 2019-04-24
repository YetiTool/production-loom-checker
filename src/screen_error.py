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
from kivy.graphics import Color, Rectangle

import sys, os


# Kivy UI builder:
Builder.load_string("""

<ErrorScreen>:


    error_reason:error_reason

    canvas:
        Color: 
            rgba: hex('#ff0000ff')
        Rectangle: 
            size: self.size
            pos: self.pos
         
    BoxLayout:
        size: self.parent.size
        pos: self.parent.pos   
        
        orientation: 'vertical'
        spacing: 0
            
        Label:
            size: self.parent.size
            pos: self.parent.pos  
            font_size: '150sp'
            markup: True
            text: 'Error!'
            size_hint_y: 3

        Label:
            id: error_reason
            size: self.parent.size
            pos: self.parent.pos  
            font_size: '20sp'
            markup: True
            text: 'Reason'
            size_hint_y: 1
            
        Button:
            font_size: '20sp'
            markup: True
            text: 'Quit'
            on_press: root.sm.current = 'lobby'
            size_hint_y: 1
       

""")


class ErrorScreen(Screen):


    is_pass =  True
    
    def __init__(self, **kwargs):
    
        super(ErrorScreen, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']
        
    def on_enter(self):
        self.error_reason.text = self.sm.get_screen('checking_screen').error_reason

        
