from talon import Module
import os

mod = Module()

@mod.action_class
class Actions:
    def write_mode_to_file(mode: str):
        """Write current mode to temp file for menu bar display"""
        with open(os.path.expanduser("~/.talon_mode"), "w") as f:
            f.write(mode)
