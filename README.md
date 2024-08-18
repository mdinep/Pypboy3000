# Pipboy-3000
 Python code recycled and forked to create a UI for a Hosyond 3.5" 480x320 Touch Screen TFT LCD.
 

Sources:
- Current own version: https://github.com/mdinep/Pypboy3000


- Credit to ColtonMcCasland who did the work converting/modernizing an older project. Repo can be found at: https://github.com/ColtonMcCasland/pypboy3000
- Additional credit to sabas1080's code, whose original work ColtonMcCasland's is based on: https://github.com/sabas1080/pypboy


- Software installation steps: 
    1. Use image recommended on this link:
        -  https://learn.adafruit.com/adafruit-pitft-3-dot-5-touch-screen-for-raspberry-pi/easy-install-2

    2. Download pygame for Debian:
        - sudo apt-get install python3-pygame

    3. Follow this link and instructions on sdl: 
		- https://learn.adafruit.com/adafruit-pitft-3-dot-5-touch-screen-for-raspberry-pi/faq?view=all#ensure-you-are-running-sdl-1-dot-2-2859156

    3. Clone the pip boy git repo in /home/pi/
        - git clone https://github.com/mdinep/Pypboy3000

    4. Follow option 2 in this link to create a script to run the pygame: 
		- https://www.makeuseof.com/how-to-run-a-raspberry-pi-program-script-at-startup/

    5. Follow this link and reference the ‘launcher.sh’ file you created. 

    6. Verify it works by running ‘sudo launcher.sh’.
        - This should work and launch the game, if the game errors on missing dependencies, add them. 


    7. Edit  and verify the boot file has dtparam-audio turned on with this command: sudo nano /boot/config.txt
        - Verify this works by running the game with the audio component connected and wired.

NOTE: radio on and off linked to a button is not currently implemented. To enable or disable radio, set the value of "RADIO_PLAYING" in config.py to True or False