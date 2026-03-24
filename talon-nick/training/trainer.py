from talon import Module, Context, actions, canvas, ui, app
import os, json, re

mod = Module()
mod.tag("training_active", desc="Vocabulary trainer is active")

mod.list("training_control", desc="Training control commands")


@mod.action_class
class TrainerActions:
    def trainer_start():
        """Start a vocabulary training session"""

    def trainer_next():
        """Advance to the next training phrase"""

    def trainer_record(phrase: str):
        """Record spoken phrase mapped to current display phrase"""

    def trainer_retry():
        """Retry the current phrase without recording"""

    def trainer_stop():
        """Stop the training session and save vocabulary"""


# ── state ────────────────────────────────────────────────────────────────────

_state: dict = {
    "phrases": [],
    "index": 0,
    "learned": {},
    "overlay": None,
}

ctx = Context()  # no matches → always active; used to control the tag


def _phrases_file() -> str:
    return os.path.join(os.path.dirname(__file__), "phrases.txt")


def _learned_file() -> str:
    return os.path.join(os.path.dirname(__file__), "learned_vocabulary.py")


def _save_learned() -> None:
    with open(_learned_file(), "w") as f:
        f.write("from talon import Context\n\n")
        f.write("ctx = Context()\n\n")
        f.write("ctx.lists[\"user.vocabulary\"] = {\n")
        for spoken, written in _state["learned"].items():
            f.write(f"    {json.dumps(spoken)}: {json.dumps(written)},\n")
        f.write("}\n")


def _load_learned() -> dict:
    path = _learned_file()
    if not os.path.exists(path):
        return {}
    try:
        with open(path) as f:
            content = f.read()
        match = re.search(
            r'ctx\.lists\["user\.vocabulary"\]\s*=\s*\{([^}]*)\}',
            content,
            re.DOTALL,
        )
        if not match:
            return {}
        result = {}
        for line in match.group(1).strip().splitlines():
            line = line.strip().rstrip(",")
            if not line:
                continue
            try:
                key, _, val = line.partition(": ")
                result[json.loads(key)] = json.loads(val)
            except Exception:
                pass
        return result
    except Exception:
        return {}


# ── canvas drawing ────────────────────────────────────────────────────────────

def _draw(c: canvas.Canvas) -> None:
    phrases = _state["phrases"]
    index = _state["index"]

    if not phrases or index >= len(phrases):
        return

    phrase = phrases[index]
    progress = f"{index + 1} / {len(phrases)}  ({len(_state['learned'])} saved)"

    c.paint.textsize = 24
    c.paint.color = "888888"
    c.draw_text(progress, 40, 50)

    c.paint.textsize = 52
    c.paint.color = "ffffff"
    c.draw_text(phrase, 40, c.height / 2)

    c.paint.textsize = 20
    c.paint.color = "666666"
    c.draw_text('"next" skip  "again" retry  "stop training" quit', 40, c.height - 40)


def _refresh() -> None:
    overlay = _state["overlay"]
    if overlay:
        overlay.freeze()


# ── action implementations ────────────────────────────────────────────────────

@ctx.action_class("user")
class TrainerImpl:
    def trainer_start():
        path = _phrases_file()
        if not os.path.exists(path):
            app.notify("Trainer", f"No phrases file found at:\n{path}")
            return

        with open(path) as f:
            phrases = [ln.strip() for ln in f if ln.strip()]

        if not phrases:
            app.notify("Trainer", "phrases.txt is empty")
            return

        _state["phrases"] = phrases
        _state["index"] = 0
        _state["learned"] = _load_learned()

        screen = ui.main_screen()
        overlay = canvas.Canvas(screen.x, screen.y, screen.width, screen.height)
        overlay.register("draw", _draw)
        overlay.freeze()
        _state["overlay"] = overlay

        # Activate training-mode commands
        ctx.tags = ["user.training_active"]

    def trainer_next():
        _state["index"] += 1
        if _state["index"] >= len(_state["phrases"]):
            actions.user.trainer_stop()
            return
        _refresh()

    def trainer_record(phrase: str):
        phrases = _state["phrases"]
        index = _state["index"]
        if not phrases or index >= len(phrases):
            return

        target = phrases[index]
        spoken = phrase.strip()

        if spoken.lower() != target.lower():
            _state["learned"][spoken.lower()] = target
            _save_learned()

        actions.user.trainer_next()

    def trainer_retry():
        _refresh()  # just redraw; index stays the same

    def trainer_stop():
        ctx.tags = []
        overlay = _state["overlay"]
        if overlay:
            overlay.close()
            _state["overlay"] = None
        _state["phrases"] = []
        _save_learned()
        n = len(_state["learned"])
        app.notify("Training complete", f"{n} vocabulary corrections saved")
