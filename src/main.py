'''
Created on 16 Nov 2017
@author: eD
A production console to check looms/wire harnesses for correct pin assignment, continuity and dead shorts
www.yetitool.com

'''
import time

from kivy.config import Config
from kivy.clock import Clock
Config.set('kivy', 'keyboard_mode', 'systemanddock')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')
Config.set('graphics', 'maxfps', '60')
Config.set('kivy', 'KIVY_CLOCK', 'interrupt')
Config.write()

import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.core.window import Window

import screen_lobby
import screen_settings
import screen_intro
import screen_result
import screen_checking
import screen_error

# import screen_zx_switch_loom

class LoomChecker(App):

    def build(self):

        print("Starting " + time.strftime('%H:%M:%S'))
        # Establish screens
        sm = ScreenManager(transition=NoTransition())

        # initialise the screens
        lobby_screen = screen_lobby.LobbyScreen(name='lobby', screen_manager = sm)
        settings_screen = screen_settings.SettingsScreen(name='settings_screen', screen_manager = sm)
        intro_screen = screen_intro.IntroScreen(name='intro_screen', screen_manager = sm)
        result_screen = screen_result.ResultScreen(name='result_screen', screen_manager = sm)
        checking_screen = screen_checking.CheckingScreen(name='checking_screen', screen_manager = sm)
        error_screen = screen_error.ErrorScreen(name='error_screen', screen_manager = sm)

#         zx_screen = screen_zx_switch_loom.ZXSwitchLoom(name='zx_screen', screen_manager = sm)

        # add the screens to screen manager
        sm.add_widget(lobby_screen)
        sm.add_widget(settings_screen)
        sm.add_widget(intro_screen)
        sm.add_widget(result_screen)
        sm.add_widget(checking_screen)
        sm.add_widget(error_screen)
#         sm.add_widget(zx_screen)

        # set screen to start on
        sm.current = 'lobby'
        
        return sm


if __name__ == '__main__':

    LoomChecker().run()
