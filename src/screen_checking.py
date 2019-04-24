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
        background_color: hex('#000000ff')
        text: ''

<PinPassInCircuit>:

    Button:
        size: self.parent.size
        pos: self.parent.pos 
        background_normal: ''
        background_color: hex('#00ff00ff')
        text: ''
        

<PinFailInCircuit>:

    Button:
        size: self.parent.size
        pos: self.parent.pos 
        background_normal: ''
        background_color: hex('#ff0000ff')
        text: ''

<PinPassNonCircuit>:

    Label:
        size: self.parent.size
        pos: self.parent.pos 
        canvas:
            Color: 
                rgba: hex('#00ff0044')
            Rectangle: 
                size: self.size
                pos: self.pos

<PinFailNonCircuit>:

    Button:
        size: self.parent.size
        pos: self.parent.pos 
        background_normal: ''
        background_color: hex('#ff000088')
        text: ''

      

<CircuitTest>:

    pin_line:pin_line
    circuit_name:circuit_name
    
    BoxLayout:

        spacing: 10

        size: self.parent.size
        pos: self.parent.pos    

        Button:
            id: circuit_name
            size: self.parent.size
            pos: self.parent.pos 
            background_normal: ''
            background_color: hex('#00000044')
            text: 'Quit'    
            size_hint_x: 1
            on_press: root.quit_to_lobby()
        
        BoxLayout:
            spacing: 0
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
    
    def __init__(self, **kwargs):
        super(CircuitTest, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']    
        
    def add_pin(self, digital_status):
        pin = PinIndicator()
        pin.set_pin_status(digital_status)
        self.pin_line.add_widget(pin)
        
    def quit_to_lobby(self):
        self.sm.current = 'lobby'

if sys.platform != "win32":
    
    import RPi.GPIO as GPIO           # import RPi.GPIO module  
    GPIO.setmode(GPIO.BOARD)            # choose BCM (Broadcom chip pin number) or BOARD (GPIO pin number)


class CheckingScreen(Screen):

    
    def __init__(self, **kwargs):

        self.error_reason = 'Error reason'
        super(CheckingScreen, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']


    def on_enter(self):

        self.pin_matrix.clear_widgets()

        # extract data_set        
        data_source_path = './looms/' + self.sm.get_screen('lobby').loom_selected + '/logic_matrix.csv'
        data_set = []
        f = open(data_source_path, "r")
        for line in f:
            line_of_data = line.rstrip().split(',')
            data_set.append(line_of_data)

        # print header row
        header = CircuitTest(screen_manager = self.sm)
        for col in data_set[1]:
            if col != "":
                l = Label(text=col)
                header.pin_line.add_widget(l)
        self.pin_matrix.add_widget(header)


        # TEST EACH CIRCUIT
        
        i = 2 #row, data starts at row 3
        
        while i < len(data_set):

            circuit_passed = True
            end_process = False
            
            # ESTABLISH CIRCUIT NAME
            circuit = CircuitTest(screen_manager = self.sm)
            circuit_name = data_set[i][0]
            circuit.circuit_name.text = circuit_name
            print circuit_name

            # RPI PIN SETUP
            # INPUTS: default all relevant pins to inputs, pulled high (high because 2 pins on the Pi have to be pulled high (3&5), so they determine the default for all)
            
            p = 1
            while p < len(data_set[0]):
                self.rpi_input_pin = int(data_set[0][p])
                print self.rpi_input_pin 
                if sys.platform != "win32":
                    try:
                        GPIO.setup(self.rpi_input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set a port/pin as an output   
                    except:
                        self.error_reason = "Unable to assign RasPi pin " + str(self.rpi_input_pin) + " as input."
                        end_process = True
                        self.sm.current = 'error'
                        break
                
                p += 1

            if end_process:
                break
            
            # OUTPUT: set the first pin marked as '1' as the output
            output_index = data_set[i].index('1')
            rpi_output_pin = int(data_set[0][output_index])
            if sys.platform != "win32":
                GPIO.setup(rpi_output_pin, GPIO.OUT, initial = 0)   # set a port/pin as an output   
            
            # COMPARE INPUTS WITH DATASET
            j=1 #col, data starts at col 2
            
            while j<len(data_set[0]):
                
                rpi_pin = int(data_set[0][j])
                
                if j == output_index: # if it's the output pin, nothing to compare, just add pin flag
                    circuit.pin_line.add_widget(PinOutput())
                else:
                    if sys.platform != "win32":
                        if GPIO.input(rpi_pin) == 1 and data_set[i][j] == '': circuit.pin_line.add_widget(PinPassNonCircuit())
                        if GPIO.input(rpi_pin) == 0 and data_set[i][j] == '1': circuit.pin_line.add_widget(PinPassInCircuit())
                        if GPIO.input(rpi_pin) == 1 and data_set[i][j] == '1': 
                            circuit.pin_line.add_widget(PinFailInCircuit())
                            circuit_passed = False
                        if GPIO.input(rpi_pin) == 0 and data_set[i][j] == '': 
                            circuit.pin_line.add_widget(PinFailNonCircuit())
                            circuit_passed = False
                    else:
                        if data_set[i][j] == '': circuit.pin_line.add_widget(PinPassNonCircuit())
                        if data_set[i][j] == '1': circuit.pin_line.add_widget(PinPassInCircuit())

                j+=1
            
            i+=1

            # Paint circuit label result
            if circuit_passed: circuit.circuit_name.background_color = 0,1,0,0.5
            else: circuit.circuit_name.background_color = 1,0,0,0.5
                
            self.pin_matrix.add_widget(circuit)
                
        
    def quit_to_lobby(self):
        self.sm.current = 'lobby'
        

        