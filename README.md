# Screensaver Trigger
This script sends a MQTT message to a server when the Gnome screen saver activates or deavtivates. This is used together with my home automation system as a sensor that trigger a lights etc. when i'm not at the computer.

## Post installation


## Installation
Start by creating the directory `/opt/screensaver-trigger/` and move the file screensaver-trigger_1.0.py to the directory.

* Cd to `/opt/screensaver-trigger/`
* Create a symbolic link `ln -s ./screensaver-trigger_[VERSION].py screensaver-trigger`
* Cd upp one directory and change ownerchip of the directory and files with `chown -R username:username /opt/screensaver-trigger/`

### Set the script to start at login

1. Open the Startup Applications menu: System -> Preferences -> Startup Applications
2. Click "Add" to create a new startup application.
3. Set Name to Screensaver Trigger and the Command to `/opt/screensaver-trigger/screensaver-trigger`
4. Click "Add" to save your new application.

The script will run automatecly next time you restart yor computer.

## Licensing
