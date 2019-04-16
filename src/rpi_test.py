'''
Created on 12 Feb 2019

@author: Letty
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

<RpiTestScreen>:

    pinBStatus:pinBStatus

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
        padding: 10
        spacing: 10
        size_hint_x: 1

        Button:
            on_press: root.toggle_pinA()
            size: self.parent.size
            pos: self.parent.pos 
            background_normal: ''
            background_color: 1, .3, .4, .85
            text_size: self.size
            font_size: '25sp'
            markup: True
            text: "Toggle Pin A"
        
        Button:
            id: pinBStatus
            size: self.parent.size
            pos: self.parent.pos 
            background_normal: ''
            background_color: 1, .3, .4, .85
            text_size: self.size
            font_size: '25sp'
            markup: True
            text: "Pin B status"
        
        Button:
            on_press: root.sm.current = 'lobby'
            size: self.parent.size
            pos: self.parent.pos 
            background_normal: ''
            background_color: 1, .3, .4, .85
            text_size: self.size
            font_size: '25sp'
            markup: True
            text: "Quit to lobby"
        

""")

if sys.platform != "win32":
    import RPi.GPIO as GPIO           # import RPi.GPIO module  
    GPIO.setmode(GPIO.BOARD)            # choose BCM (Broadcom chip pin number) or BOARD (GPIO pin number)
    GPIO.setup(3, GPIO.OUT, initial) # set a port/pin as an output   

class RpiTestScreen(Screen):
    
    
    def __init__(self, **kwargs):
    
        super(RpiTestScreen, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']
        

    def toggle_pinA(self):
        
        if sys.platform != "win32":
            pass
            