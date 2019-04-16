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

import socket, sys, os


# Kivy UI builder:
Builder.load_string("""

<SettingsScreen>:

    network_container:network_container
    developer_container:developer_container    
    
    Accordion:
        orientation: 'horizontal'

        AccordionItem:
            title: 'Network'
            id: network_container

        AccordionItem:
            title: 'Developer'
            id: developer_container

<NetworkSetup>:

    networkTextEntry:networkTextEntry
    passwordTextEntry:passwordTextEntry
    ipLabel:ipLabel
    netNameLabel:netNameLabel
    countryTextEntry:countryTextEntry

    BoxLayout:
    
        size: self.parent.size
        pos: self.parent.pos      
        padding: 10
        spacing: 10
        orientation: "vertical" 
        canvas:
            Color:
                rgba: 0,0,0,0.2
            Rectangle:
                size: self.size
                pos: self.pos

        Button:
            text: 'Refresh status...'
            on_release: root.detectIP()
        TextInput:
            id: countryTextEntry
            size_hint_y: None
            height: '32dp'
            text: 'GB'
            focus: False
            multiline: False
        TextInput:
            id: networkTextEntry
            size_hint_y: None
            height: '32dp'
            text: 'Network name...'
            focus: False
            multiline: False
        TextInput:
            id: passwordTextEntry
            size_hint_y: None
            height: '32dp'
            text: 'Network password...'
            focus: False
            multiline: False
        Label:
            id: ipLabel
            text: 'IP address info here'
        Label:
            id: netNameLabel
            text: 'IP address info here'
        Button:
            text: 'Connect...'
            on_release: root.connectWifi()

<DevOptions>:

    sw_version_label:sw_version_label
    sw_branch_label:sw_branch_label

    GridLayout:
        size: self.parent.size
        pos: self.parent.pos
        cols: 2

        Button:
            text: 'Reboot'
            on_release: root.reboot()

        Button:
            text: 'Quit to Console'
            on_release: root.quit_to_console()

        Button:
            text: 'Return to lobby'
            on_release: root.return_to_lobby()

        Button:
            text: 'Get SW update'
            on_release: root.get_sw_update()

        Label:
            test: 'Repository Branch'
            font_size: 18
            color: 0,0,0,1
            id: sw_branch_label

        Label:
            text: 'SW VER'
            font_size: 18
            color: 0,0,0,1
            id: sw_branch_label
            id: sw_version_label

""")

class DevOptions(Widget):


    def __init__(self, **kwargs):

        super(DevOptions, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']
        self.refresh_sw_branch_label()
        self.refresh_sw_version_label()

    def reboot(self):

        if sys.platform != "win32":
            sudoPassword = 'pi'
            command = 'sudo reboot'
            p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))

    def quit_to_console(self):
        print 'Quitting to console - bye!'
        sys.exit()

    def return_to_lobby(self):
        self.sm.current = 'lobby'

    def refresh_sw_branch_label(self):
        data = os.popen("git symbolic-ref --short HEAD").read()
        self.sw_branch_label.text = data

    def refresh_sw_version_label(self):
        data = os.popen("git describe --always").read()
        self.sw_version_label.text = data

    def get_sw_update(self):
        os.system("cd /home/pi/production-loom-checker && git pull")
        self.reboot()
 

class NetworkSetup(Widget):

    def __init__(self, **kwargs):
    
        super(NetworkSetup, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']

    def connectWifi(self):

        # get network name and password from text entered (widget)
        self.netname = self.networkTextEntry.text
        self.password = self.passwordTextEntry.text
        self.country = self.countryTextEntry.text 

        # pass credentials to wpa_supplicant file
        self.wpanetpass = 'wpa_passphrase "' + self.netname + '" "' + self.password + '" 2>/dev/null | sudo tee /etc/wpa_supplicant/wpa_supplicant.conf'
        self.wpanetpasswlan0 = 'wpa_passphrase "' + self.netname + '" "' + self.password + '" 2>/dev/null | sudo tee /etc/wpa_supplicant/wpa_supplicant-wlan0.conf'
        
        #if wpanetpass.startswith('network={'):       

        # put the credentials and the necessary appendages into the wpa file
        os.system(self.wpanetpass)
        os.system('echo "ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev" | sudo tee --append /etc/wpa_supplicant/wpa_supplicant.conf')
        os.system('echo "country="' + self.country + '| sudo tee --append /etc/wpa_supplicant/wpa_supplicant.conf')
        os.system('echo "update_config=1" | sudo tee --append /etc/wpa_supplicant/wpa_supplicant.conf')
   
        os.system(self.wpanetpasswlan0)
        os.system('echo "ctrl_interface=run/wpa_supplicant" | sudo tee --append /etc/wpa_supplicant/wpa_supplicant-wlan0.conf')
        os.system('echo "update_config=1" | sudo tee --append /etc/wpa_supplicant/wpa_supplicant-wlan0.conf')
        os.system('echo "country="' + self.country + '| sudo tee --append /etc/wpa_supplicant/wpa_supplicant-wlan0.conf')
        
        os.system('sudo reboot')
        


class SettingsScreen(Screen):
   
    
    def __init__(self, **kwargs):
    
        super(SettingsScreen, self).__init__(**kwargs)
        self.sm=kwargs['screen_manager']
        
        self.network_container.add_widget(NetworkSetup(screen_manager=self.sm))
        self.developer_container.add_widget(DevOptions(screen_manager=self.sm))
