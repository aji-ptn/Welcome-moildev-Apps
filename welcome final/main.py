from moildevApps.base_plugin import Plugin
from .controller.controller import *


class welcome_Apps(Plugin):
    def __init__(self):
        super().__init__()
        self.description = "this is from Aji pamungkas"

    def perform_operation(self, argument):
        self.w = Controller(argument)
        self.w.show()
