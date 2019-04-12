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

import sys, os


# Kivy UI builder:
Builder.load_string("""

<UpperLoomScreen>:

    homing_label:homing_label

    canvas:
        Color: 
            rgba: hex('#0D47A1ff')
        Rectangle: 
            size: self.size
            pos: self.pos
             
    BoxLayout:
        orientation: 'horizontal'
        padding: 70
        spacing: 70
        size_hint_x: 1

        BoxLayout:
            orientation: 'vertical'
            size_hint_x: 1
#             spacing: 20
#             padding: 10
            
                
            Label:
                id: homing_label
                text_size: self.size
                size_hint_y: 0.5
                text: 'Ya mama'
                markup: True
                font_size: '40sp'   
                valign: 'bottom'
                halign: 'center'
                
            AnchorLayout: 
                Button:
                    size_hint_x: 0.25
                    size_hint_y: 0.35
                    halign: 'center'
                    valign: 'middle'
                    background_normal: ''
                    background_color: hex('#1E88E5ff')
                    on_release: 
                        root.quit_to_lobby()
                    
                    Label:
                        #size: self.texture_size
                        text: '[b]Quit[/b]'
                        size: self.parent.size
                        pos: self.parent.pos
                        text_size: self.size
                        valign: 'middle'
                        halign: 'center'
                        font_size: '22sp'
                        markup: True
            Label: 
                size_hint_y: 0.2
                text: 'Squaring the axes will cause the machine to make a stalling noise. This is normal.'
                markup: True
                font_size: '20sp' 
                valign: 'top'
                

""")


class UpperLoomScreen(Screen):
    
    
    def __init__(self, **kwargs):
    
        super(UpperLoomScreen, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']
    
    
    def quit_to_lobby(self):
        self.sm.current = 'lobby'