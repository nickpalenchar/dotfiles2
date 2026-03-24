from talon import Context, actions, scope, app

def on_ready():
    actions.user.hud_activate_poller("mode")

app.register("ready", on_ready)

ctx = Context()
ctx.matches = """
tag: user.talon_hud_available
"""

@ctx.action_class("user")
class Actions:

    def hud_determine_mode() -> str:
        """Determine the current mode used for the status bar icons"""
        active_modes = scope.get("mode")
        available_modes = ["dictation", "command", "sleep"]

        current_mode = "command"
        for available_mode in available_modes:
            if available_mode in active_modes:
                current_mode = available_mode
                break

        return current_mode

    def hud_toggle_mode():
        """Toggle between dictation and sleep"""
        current_mode = actions.user.hud_determine_mode()
        if current_mode == "dictation":
            actions.speech.disable()
        elif current_mode == "command":
            actions.speech.disable()
        elif current_mode == "sleep":
            actions.speech.enable()
