'''
Created on 19 Aug 2017

@author: Ed
'''
# config

import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, ListProperty, NumericProperty # @UnresolvedImport
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.clock import Clock


import sys, os
from os.path import expanduser
from shutil import copy


Builder.load_string("""

#:import hex kivy.utils.get_color_from_hex


<LobbyScreen>:

    carousel:carousel

    canvas.before:
        Color: 
            rgba: hex('#0d47a1FF')
        Rectangle: 
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size: self.parent.size
        pos: self.parent.pos
        padding: 0
        spacing: 0

        Carousel:
            size_hint_y: 340
            id: carousel
            loop: True
                            
            BoxLayout:
                orientation: 'horizontal'
                padding: 70
                spacing: 70

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_x: 1
                    spacing: 20
    
                    Button:
                        size_hint_y: 8
                        id: load_button
                        disabled: False
                        background_color: hex('#FFFFFF00')
                        on_release: 
                            root.goto_upper_loom()
                            self.background_color = hex('#FFFFFF00')
                        on_press:
                            self.background_color = hex('#FFFFFF00')
                        BoxLayout:
                            padding: 0
                            size: self.parent.size
                            pos: self.parent.pos
                            Image:
                                id: image_select
                                source: "./img/lobby_pro.png"
                                center_x: self.parent.center_x
                                center_y: self.parent.center_y
                                size: self.parent.width, self.parent.height
                                allow_stretch: True 
                    Label:
                        size_hint_y: 1
                        font_size: '25sp'
                        text: 'Upper Loom'
                        
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_x: 1
                    spacing: 20
                                            
                    Button:
                        id: load_button
                        disabled: True
                        size_hint_y: 8
                        background_color: hex('#FFFFFF00')
                        on_release: 
#                             root.go_to_initial_screen(1)
#                            root.manager.current = 'template'
#                            root.manager.current = 'vj_polygon'
                            self.background_color = hex('#FFFFFF00')
                        on_press:
                            self.background_color = hex('#FFFFFF00')
                        BoxLayout:
                            padding: 0
                            size: self.parent.size
                            pos: self.parent.pos
                            Image:
                                id: image_select
                                source: "./img/lobby_pro.png"
                                center_x: self.parent.center_x
                                y: self.parent.y
                                size: self.parent.width, self.parent.height
                                allow_stretch: True 
                    Label:
                        size_hint_y: 1
                        font_size: '25sp'
                        text: 'Lower Loom'
                        
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_x: 1
                    spacing: 20

                    Button:
                        id: load_button
                        disabled: True
                        size_hint_y: 8
                        background_color: hex('#FFFFFF00')
                        on_release: 
#                             root.go_to_initial_screen(1)
                            self.background_color = hex('#FFFFFF00')
                        on_press:
                            self.background_color = hex('#FFFFFF00')
                        BoxLayout:
                            padding: 0
                            size: self.parent.size
                            pos: self.parent.pos
                            Image:
                                id: image_select
                                source: "./img/lobby_pro.png"
                                center_x: self.parent.center_x
                                y: self.parent.y
                                size: self.parent.width, self.parent.height
                                allow_stretch: True 
                    Label:
                        size_hint_y: 1
                        font_size: '25sp'
                        text: ''
                        
            # Carousel pane 2
        
            BoxLayout:
                orientation: 'horizontal'
                padding: 70
                spacing: 70

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_x: 1
                    spacing: 20
    
                    Button:
                        size_hint_y: 8
                        id: load_button
                        disabled: False
                        background_color: hex('#FFFFFF00')
                        on_release: 
#                             root.go_to_initial_screen(1)
                            self.background_color = hex('#FFFFFF00')
                        on_press:
                            self.background_color = hex('#FFFFFF00')
                        BoxLayout:
                            padding: 0
                            size: self.parent.size
                            pos: self.parent.pos
                            Image:
                                id: image_select
                                source: "./img/lobby_pro.png"
                                center_x: self.parent.center_x
                                center_y: self.parent.center_y
                                size: self.parent.width, self.parent.height
                                allow_stretch: True 
                    Label:
                        size_hint_y: 1
                        font_size: '25sp'
                        text: ''
                        
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_x: 1
                    spacing: 20
                                            
                    Button:
                        id: load_button
                        disabled: False
                        size_hint_y: 8
                        background_color: hex('#FFFFFF00')
                        on_release: 
#                             root.go_to_initial_screen(1)
                            self.background_color = hex('#FFFFFF00')
                        on_press:
                            self.background_color = hex('#FFFFFF00')
                        BoxLayout:
                            padding: 0
                            size: self.parent.size
                            pos: self.parent.pos
                            Image:
                                id: image_select
                                source: "./img/lobby_pro.png"
                                center_x: self.parent.center_x
                                y: self.parent.y
                                size: self.parent.width, self.parent.height
                                allow_stretch: True 
                    Label:
                        size_hint_y: 1
                        font_size: '25sp'
                        text: ''
                        
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_x: 1
                    spacing: 20

                    Button:
                        id: load_button
                        disabled: False
                        size_hint_y: 8
                        background_color: hex('#FFFFFF00')
                        on_release: 
#                             root.go_to_initial_screen(1)
                            self.background_color = hex('#FFFFFF00')
                        on_press:
                            self.background_color = hex('#FFFFFF00')
                        BoxLayout:
                            padding: 0
                            size: self.parent.size
                            pos: self.parent.pos
                            Image:
                                id: image_select
                                source: "./img/lobby_pro.png"
                                center_x: self.parent.center_x
                                y: self.parent.y
                                size: self.parent.width, self.parent.height
                                allow_stretch: True 
                    Label:
                        size_hint_y: 1
                        font_size: '25sp'
                        text: ''

        BoxLayout:
            size_hint_y: 6
            size: self.parent.size
            pos: self.parent.pos
          
            Image:
                source: "./img/lobby_separator.png"


        BoxLayout:
            size_hint_y: 134
            size: self.parent.size
            pos: self.parent.pos
            padding: 40
            orientation: 'horizontal'
            
            Button:
                disabled: False
                size_hint_y: 1
                background_color: hex('#FFFFFF00')
                on_release: 
                    carousel.load_previous()
                    self.background_color = hex('#FFFFFF00')
                on_press:
                    self.background_color = hex('#FFFFFF00')
                BoxLayout:
                    size: self.parent.size
                    pos: self.parent.pos
                    Image:
                        id: image_cancel
                        source: "./img/lobby_scrollleft.png"
                        center_x: self.parent.center_x
                        y: self.parent.y
                        size: self.parent.width, self.parent.height
                        allow_stretch: True 

            Label:
                size_hint_y: 1

            Label:
                size_hint_y: 1

            Button:
                id: load_button
                disabled: False
                size_hint_y: 1
                background_color: hex('#FFFFFF00')
                on_release: 
                    carousel.load_next(mode='next')
                    self.background_color = hex('#FFFFFF00')
                on_press:
                    self.background_color = hex('#FFFFFF00')
                BoxLayout:
                    size: self.parent.size
                    pos: self.parent.pos
                    Image:
                        id: image_select
                        source: "./img/lobby_scrollright.png"
                        center_x: self.parent.center_x
                        y: self.parent.y
                        size: self.parent.width, self.parent.height
                        allow_stretch: True 

                
""")


class LobbyScreen(Screen):
    
    
    def __init__(self, **kwargs):
        super(LobbyScreen, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']


    def goto_upper_loom(self):
        self.sm.current = 'upper_loom'
    
    
        
