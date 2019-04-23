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

<ResultScreen>:

    pass_fail_label:pass_fail_label
    report_button:report_button
             
    BoxLayout:
        size: self.parent.size
        pos: self.parent.pos   
        
        orientation: 'vertical'
        spacing: 0
        size_hint_y: None
        height: 400
            
        Label:
            id: pass_fail_label
            size: self.parent.size
            pos: self.parent.pos  
            font_size: '150sp'
            markup: True

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
                id:report_button
                font_size: '30sp'
                markup: True
                text: 'Report'
                on_press: root.sm.current = 'lobby'
    
            Button:
                font_size: '30sp'
                markup: True
                text: 'Go'
                on_press: root.sm.current = 'checking_screen'
        

""")


class ResultScreen(Screen):


    is_pass =  True
    
    def __init__(self, **kwargs):
    
        super(ResultScreen, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']
        
    def on_enter(self):

        if self.is_pass:
            with self.canvas.before:
                Color(0, 1, 0, 1)
                Rectangle(pos=self.pos, size=self.size)
            self.pass_fail_label.text='[color=000000]Pass :-)[/color]'

        else:
            with self.canvas.before:
                Color(1, 0, 0, 1)
                Rectangle(pos=self.pos, size=self.size)
            self.pass_fail_label.text='[color=000000]Fail :-([/color]'
