from moildevApps.base_plugin import Plugin
from .contoller.controller import *


class Welcome_Awwpps(Plugin):
    def __init__(self):
        super().__init__()
        self.description = "this is from welcomqweqe"

    def perform_operation(self, argument):
        self.w = Controller(argument)
        self.w.show()
