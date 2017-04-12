#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from gi.repository import GObject as gobject
from dbus import SessionBus
from dbus.mainloop.glib import DBusGMainLoop

class ScreensaverTrigger:
    def sendmqtt(self, status):
        mqttc = mqtt.Client("python_pub")
        mqttc.connect("bjornson.nu", 1883)
        mqttc.publish("home/device/laptop01", "{ \"status\": \" " + status + " \" }")
        mqttc.loop(2)

    def __init__(self):
        DBusGMainLoop(set_as_default=True)
        self.mem='ActiveChanged'
        self.dest='org.gnome.ScreenSaver'
        self.bus=SessionBus()
        self.mainloop=gobject.MainLoop()
        self.bus.add_signal_receiver(self.catch,self.mem,self.dest)

    def catch(self,ssOn):
        if ssOn == 1:
            # Screensaver turned on
            self.sendmqtt("Inactive")

        else:
            # Screensaver turned off
            self.sendmqtt("Active")




ScreensaverTrigger().mainloop.run()