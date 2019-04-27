'''
Created on 19 Aug 2017

@author: eD
'''
# config

import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
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

    grid:grid
    
    canvas.before:
        Color: 
            rgba: hex('#0d47a1FF')
        Rectangle: 
            size: self.size
            pos: self.pos

                            
    GridLayout:

        id: grid
        rows: 2
        padding: 30
        spacing: 30

                
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
                    self.background_color = hex('#FFFFFF00')
                    root.sm.current = 'settings_screen'
                on_press:
                    self.background_color = hex('#FFFFFF00')
                BoxLayout:
                    padding: 0
                    size: self.parent.size
                    pos: self.parent.pos
                    Image:
                        id: image_select
                        source: "./img/settings_cog.png"
                        center_x: self.parent.center_x
                        y: self.parent.y
                        size: self.parent.width, self.parent.height
                        allow_stretch: True 
            Label:
                size_hint_y: 1
                font_size: '15sp'
                text: 'Settings'


                
#         BoxLayout:
#             orientation: 'vertical'
#             size_hint_x: 1
#             spacing: 20
#                                     
#             Button:
#                 id: load_button
#                 disabled: False
#                 size_hint_y: 8
#                 background_color: hex('#FFFFFF00')
#                 on_release: 
#                     self.background_color = hex('#FFFFFF00')
#                     root.sm.current = 'rpi_test'
#                 on_press:
#                     self.background_color = hex('#FFFFFF00')
#                 BoxLayout:
#                     padding: 0
#                     size: self.parent.size
#                     pos: self.parent.pos
#                     Image:
#                         id: image_select
#                         source: "./img/lobby_pro.png"
#                         center_x: self.parent.center_x
#                         y: self.parent.y
#                         size: self.parent.width, self.parent.height
#                         allow_stretch: True 
#             Label:
#                 size_hint_y: 1
#                 font_size: '25sp'
#                 text: 'RPi Test'

<IconSet>

    image_for_button:image_for_button
    text_for_icon_set:text_for_icon_set

    BoxLayout:
        orientation: 'vertical'
        spacing: 20
        size: self.parent.size
        pos: self.parent.pos
                                
        Button:
            size_hint_y: 8
            background_color: hex('#FFFFFF00')
            on_press: root.button_pushed()
            BoxLayout:
                padding: 0
                size: self.parent.size
                pos: self.parent.pos
                Image:
                    id: image_for_button
                    center_x: self.parent.center_x
                    y: self.parent.y
                    size: self.parent.width, self.parent.height
                    allow_stretch: True 
        Label:
            id: text_for_icon_set
            size_hint_y: 1
            font_size: '15sp'
    
                        
                
""")


class IconSet(Widget):

    def __init__(self, **kwargs):
        super(IconSet, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']
        
    def button_pushed(self):
#         self.loom_selected = self.text_for_icon_set.text
        self.sm.get_screen('lobby').loom_selected = self.text_for_icon_set.text
        self.sm.current = 'intro_screen'
        

class LobbyScreen(Screen):
    
    loom_selected = None
    
    def __init__(self, **kwargs):
        super(LobbyScreen, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']
        
        # crawl folders in 'looms' dir, to make an icon set for each
        loom_names = next(os.walk('./looms'))[1]
        
        for loom in loom_names:
            icon_set = IconSet(screen_manager = self.sm)
            icon_set.text_for_icon_set.text = str(loom)
            icon_set.image_for_button.source = './looms/' + loom + '/icon.png' 
            self.grid.add_widget(icon_set)
