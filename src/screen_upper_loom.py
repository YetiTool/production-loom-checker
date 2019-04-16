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

<PinIndicator>:

    pin_status:pin_status
    
    Button:
        id: pin_status
        size: self.parent.size
        pos: self.parent.pos 
        background_normal: ''
        background_color: 1, .3, .4, .85
        text_size: self.size
        font_size: '25sp'
        markup: True
        text: ""
      

<CircuitTest>:

    pin_line:pin_line
    circuit_name:circuit_name
    
    BoxLayout:
        
        size: self.parent.size
        pos: self.parent.pos    
    
        Label:
            id: circuit_name
            size: self.parent.size
            pos: self.parent.pos    
            size_hint_x: 1
        
        BoxLayout:
            id:pin_line
            size: self.parent.size
            pos: self.parent.pos    
            orientation: 'horizontal'
            size_hint_x: 9
        
<UpperLoomScreen>:

    pin_matrix:pin_matrix
    
    canvas:
        Color: 
            rgba: hex('#0D47A1ff')
        Rectangle: 
            size: self.size
            pos: self.pos
             
    BoxLayout:
        size: self.parent.size
        pos: self.parent.pos      


        id:pin_matrix
        orientation: 'vertical'
        padding: 10
        spacing: 10
        size_hint_x: 1

        

""")

pin_list = []        

class PinIndicator(Widget):
    
    def set_pin_status(self, digital_status):
        self.pin_status.text = str(digital_status)


class CircuitTest(Widget):
    
    def add_pin(self, digital_status):
        pin = PinIndicator()
        pin.set_pin_status(digital_status)
        self.pin_line.add_widget(pin)


class UpperLoomScreen(Screen):
    
    def __init__(self, **kwargs):
    
        super(UpperLoomScreen, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']

        i=0 
        while i < 10:
            circuit = CircuitTest()
            circuit.circuit_name.text = "Test " + str(i)
            p=0 
            while p < 30:
                circuit.add_pin(0)
                p += 1
        
            self.pin_matrix.add_widget(circuit)
            i += 1
        
    
    def quit_to_lobby(self):
        self.sm.current = 'lobby'
        

        