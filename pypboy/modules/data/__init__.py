from pypboy import BaseModule
from pypboy.modules.data import local_map
from pypboy.modules.data import world_map
from pypboy.modules.data import quests
from pypboy.modules.data import misc
from pypboy.modules.data import radio
import config

if config.GPIO_AVAILABLE:
    import RPi.GPIO as GPIO

class Module(BaseModule):

    label = "DATA"
    GPIO_LED_ID = 24

    def __init__(self, *args, **kwargs):
        
        self.submodules = [
            local_map.Module(self),
            world_map.Module(self),
            quests.Module(self),
            misc.Module(self),
            radio.Module(self)
        ]
        super(Module, self).__init__(*args, **kwargs)
        
    def handle_resume(self):
        self.pypboy.header.headline = self.label
        self.pypboy.header.title = ["Seattle"]
        self.active.handle_action("resume")
        
