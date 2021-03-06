For use, see wiki on github.
For installation, follow the steps below.

### Platform

Intended for RasPi with Rasbian Lite & use with 7" touchscreen.

### Preparation

These steps follow the same build steps use to prepared an EasyCut console platform (see [Readme](https://github.com/YetiTool/console-raspi3b-plus-platform)). When that's complete, procede...

### App installation

* Clone from the SmartBench repository:
  * `cd && git clone https://github.com/YetiTool/production-loom-checker.git`

### Autostart

#### Disable EasyCut autostart

To disable the pi from autostarting EasyCut app on booting:
* comment out the contents of the bash script:
  * `sudo nano starteasycut.sh` 
  * save & quit
  * `sudo reboot` to check (you'll only get the logo screen of course, since it's on silent boot)

#### Enable Loomchecker autostart

To enable the pi to autostart LoomChecker app on booting
* create bash script to run app
  * `touch /home/pi/startloomchecker.sh`
  * `sudo nano /home/pi/startloomchecker.sh`
    *  ... add
       ```
       #!/bin/bash
       echo "start loomchecker"
       cd /home/pi/production-loom-checker/src/
       exec python main.py
       ```
  * make sure script is executable:
    * `sudo chmod +x /home/pi/startloomchecker.sh`
  * test
    * `bash startloomchecker.sh`
* create a file for the service, edit and enable.
  * `sudo touch /lib/systemd/system/loomchecker.service`
  * `sudo nano /lib/systemd/system/loomchecker.service`
  * ...add (note "Type" can be 'simple' to speed up, but 'idle' will wait to avoid interleaved shelloutput)
    ```
    [Unit]
    Description=run loomchecker service and redirect stderr and stdout to a log file
    After=multi-user.target

    [Service]
    Type=idle
    ExecStart=/home/pi/startloomchecker.sh
    User=pi

    [Install]
    WantedBy=multi-user.target
    ```
  * ...to check file
    * `sudo systemctl cat loomchecker.service`

  * `sudo systemctl enable loomchecker.service`
  * `sudo systemctl start loomchecker.service`
  * `sudo reboot`
  * ...check status of service if not started
    * `sudo systemctl status loomchecker`
    * `sudo journalctl _SYSTEMD_UNIT=loomchecker.service`
