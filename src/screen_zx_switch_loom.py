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

<ZXSwitchLoom>:

    switch_1_label:switch_1_label
    switch_2_label:switch_2_label
    switch_3_label:switch_3_label

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

            
        BoxLayout:
            size: self.parent.size
            pos: self.parent.pos 

            orientation: 'horizontal'
            padding: 10
            spacing: 10
            size_hint_x: 1
            
            Label:
                font_size: '60sp'
                markup: True
                text: "x-MIN"              
            
            Label:
                font_size: '60sp'
                markup: True
                text: "x-MAX"              
            
            Label:
                font_size: '60sp'
                markup: True
                text: "Z"              
        
      

        BoxLayout:
            orientation: 'horizontal'
            padding: 10
            spacing: 10
            size_hint_x: 1
            
            Label:
                id: switch_1_label
                font_size: '60sp'
                markup: True
                text: "0"              

            Label:
                id: switch_2_label
                font_size: '60sp'
                markup: True
                text: "0"              

            Label:
                id: switch_3_label
                font_size: '60sp'
                markup: True
                text: "0"    
        
        Button:
            on_press: root.sm.current = 'lobby'
            background_normal: ''
            background_color: 1, .3, .4, .85
            font_size: '60sp'
            markup: True
            text: "Quit to lobby"
         

""")

if sys.platform != "win32":
    
    import RPi.GPIO as GPIO           # import RPi.GPIO module  
    GPIO.setmode(GPIO.BOARD)            # choose BCM (Broadcom chip pin number) or BOARD (GPIO pin number)

class ZXSwitchLoom(Screen):

    pin_toggle_mode = StringProperty('normal') # toggles between 'normal' or 'down'(/looks like it's been pressed)
    
    
    def __init__(self, **kwargs):
    
        super(ZXSwitchLoom, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']
        


    def on_enter(self):
        if sys.platform != "win32":
            
            GPIO.setup(19, GPIO.OUT, initial = 0)   # set a port/pin as an output   
            GPIO.setup(21, 
            GPIO.setup(21, 
            GPIO.setup(21, 
            GPIO.setup(21, 
            GPIO.setup(21, 
            
            
            
            GPIO.setup(38, GPIO.OUT, initial = 0)   # set a port/pin as an output   
            GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # set a port/pin as an output   
            Clock.schedule_interval(self.check_pin, 0.1) # Delay for grbl to initialize        
 
    def pin_toggled(self):
        
        if self.pin_toggle_mode == 'normal': # virtual hw mode OFF
            print 'Pin toggle OFF'
            if sys.platform != "win32":
                GPIO.output(38, GPIO.LOW)

            
        if self.pin_toggle_mode == 'down': # virtual hw mode ON
            print 'Pin toggle ON'
            if sys.platform != "win32":
                GPIO.output(38, GPIO.HIGH)


    def check_pin(self, dt):
        
        print GPIO.input(40)
        
        if GPIO.input(40):
            self.pinBStatus.text = '1'
        else: 
            self.pinBStatus.text = '0' 
