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

            
        ToggleButton:
            state: root.pin_toggle_mode
            size: self.parent.size
            pos: self.parent.pos 
            background_normal: ''
            background_color: 1, .3, .4, .85
            text_size: self.size
            font_size: '25sp'
            markup: True
            text: 'Toggle pin'
            on_state:
                root.pin_toggle_mode = self.state
                root.pin_toggled()
        
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

class RpiTestScreen(Screen):

    pin_toggle_mode = StringProperty('normal') # toggles between 'normal' or 'down'(/looks like it's been pressed)
    
    
    def __init__(self, **kwargs):
    
        super(RpiTestScreen, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']
        
        if sys.platform != "win32":
            GPIO.setup(3, GPIO.OUT, initial = 0)   # set a port/pin as an output   
            GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set a port/pin as an output   
            Clock.schedule_interval(self.check_pin, 0.5) # Delay for grbl to initialize

 
    def pin_toggled(self):
        
        if self.pin_toggle_mode == 'normal': # virtual hw mode OFF
            #turn soft limits, hard limts and homing cycle ON
            print 'Pin toggle OFF'
            if sys.platform != "win32":
                GPIO.output(3, GPIO.LOW)

            
        if self.pin_toggle_mode == 'down': # virtual hw mode ON
            #turn soft limits, hard limts and homing cycle OFF
            print 'Pin toggle ON'
            if sys.platform != "win32":
                GPIO.output(3, GPIO.HIGH)


    def check_pin(self, dt):
        
        if GPIO.input(5):
            self.pinBStatus.text = '1'
        else: 
            self.pinBStatus.text = '0' 
