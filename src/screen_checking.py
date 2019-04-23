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
from kivy.uix.label import Label

import sys, os


# Kivy UI builder:
Builder.load_string("""

<PinOutput>:

    Button:
        size: self.parent.size
        pos: self.parent.pos 
        background_normal: ''
        background_color: hex('#0D47A1ff')

<PinPassInCircuit>:

    Button:
        size: self.parent.size
        pos: self.parent.pos 
        background_normal: ''
        background_color: hex('#0D47A1ff')

<PinFailInCircuit>:

    Button:
        size: self.parent.size
        pos: self.parent.pos 
        background_normal: ''
        background_color: hex('#0D47A1ff')

<PinPassNonCircuit>:

    Button:
        size: self.parent.size
        pos: self.parent.pos 
        background_normal: ''
        background_color: hex('#0D47A1ff')

<PinFailNonCircuit>:

    Button:
        size: self.parent.size
        pos: self.parent.pos 
        background_normal: ''
        background_color: hex('#0D47A1ff')

      

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

        
<CheckingScreen>:

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


class PinOutput(Widget):
    pass

class PinPassInCircuit(Widget):
    pass

class PinFailInCircuit(Widget):
    pass

class PinPassNonCircuit(Widget):
    pass

class PinFailNonCircuit(Widget):
    pass


class CircuitTest(Widget):
    
    def add_pin(self, digital_status):
        pin = PinIndicator()
        pin.set_pin_status(digital_status)
        self.pin_line.add_widget(pin)


class CheckingScreen(Screen):
    
    def __init__(self, **kwargs):
    
        super(CheckingScreen, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']

    def on_enter(self):

        # extract data_set        
        data_source_path = './looms/' + self.sm.get_screen('lobby').loom_selected + '/logic_matrix.csv'
        data_set = []
        f = open(data_source_path, "r")
        for line in f:
            line_of_data = line.rstrip().split(',')
            data_set.append(line_of_data)

        # print header row
        header = CircuitTest()
        for col in data_set[1]:
            if col != "":
                l = Label(text=col)
                header.pin_line.add_widget(l)
        self.pin_matrix.add_widget(header)

        # print the rest
        i=2
        while i<len(data_set):
            circuit = CircuitTest()
            circuit.circuit_name.text = data_set[i][0]
            j=1
            while j<len(data_set[i]):
                l = Label(text=data_set[i][j])
                circuit.pin_line.add_widget(l)
                j+=1
            i+=1
            self.pin_matrix.add_widget(circuit)
                
        
            
            
            
# 
#         i=0 
#         while i < 10:
#             circuit = CircuitTest()
#             circuit.circuit_name.text = "Test " + str(i)
#             p=0 
#             while p < 30:
#                 circuit.add_pin(0)
#                 p += 1
#         
#             self.pin_matrix.add_widget(circuit)
#             i += 1
#         
    
    def quit_to_lobby(self):
        self.sm.current = 'lobby'
        

        