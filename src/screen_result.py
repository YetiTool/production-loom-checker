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
from kivy.uix.scrollview import ScrollView

import sys, os


# Kivy UI builder:
Builder.load_string("""

<ResultScreen>:

    report_button:report_button
    consoleScrollText:consoleScrollText
             
    BoxLayout:
        size: self.parent.size
        pos: self.parent.pos   
        
        orientation: 'vertical'
        padding: 10
        spacing: 10
            
        ScrollableLabel:
            size_hint_y: 5                       
            id: consoleScrollText
            
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 1
    
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
                text: 'GO AGAIN!'
                on_press: root.sm.current = 'checking_screen'

<ScrollableLabel>:
    scroll_y:0

    Label:
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        max_lines: 60 
        markup: True
        font_size: root.font_size
        text: root.text
       

""")

class ScrollableLabel(ScrollView):

    text = StringProperty('')
    font_size = NumericProperty('')

class ResultScreen(Screen):


    is_pass =  True
    
    def __init__(self, **kwargs):
    
        super(ResultScreen, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']
        
    def on_enter(self):

        if self.sm.get_screen('checking_screen').fail_reasons == []:
            with self.canvas.before:
                Color(0, 1, 0, 1)
                Rectangle(pos=self.pos, size=self.size)
            self.update_display_text("Pass :-)", '150sp')


        else:
            with self.canvas.before:
                Color(1, 0, 0, 1)
                Rectangle(pos=self.pos, size=self.size)
            self.pass_fail_label.font_size='20sp'
            failure_description='[color=000000]Uh-oh!! \n\n' + '\n'.join(self.sm.get_screen('checking_screen').fail_reasons) + '[/color]'
            self.update_display_text(failure_description, '25sp')
    

    def update_display_text(self, failure_description, font_size):   
        
        self.consoleScrollText.font_size = font_size
        self.consoleScrollText.text = '[color=000000]' + failure_description + '[/color]'