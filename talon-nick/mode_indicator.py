# ~/.talon/user/nick/mode_indicator.py
from talon import app, actions, registry

def on_mode_change(event):
    modes = registry.modes
    if "dictation" in modes:
        app.icon_color(0, 0.7, 0, 1)    # green = talk mode
    elif "sleep" in modes:
        app.icon_color(1, 0, 0, 1)      # red = sleeping
    else:
        app.icon_color(0, 0.5, 1, 1)    # blue = command mode

registry.register("mode", on_mode_change)
