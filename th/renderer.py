from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import ResizeScreenError, StopApplication
from asciimatics.renderers import StaticRenderer, DynamicRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import PopUpDialog

HELP = """
Use the following keys:

- A, S, D, F, and G to press fret buttons.
- Space bar to pick string.
- X to quit
"""


class GameState(object):
    """
    Persistent state for this application.
    """

    def __init__(self):
        self.button_1 = False


class FretboardDynamic(DynamicRenderer):
    def __init__(self, height, width):
        super(FretboardDynamic, self).__init__(height, width)
        self._t = 0
        self._fret_line = "|----" * 6 + "|\n"
        self._line = "|    " * 6 + "|\n"
        self._lines = []

    def _render_now(self):
        if self._t % 4:
            self._lines.insert(0, self._line)
        else:
            self._lines.insert(0, self._fret_line)

        for index, line in enumerate(self._lines):
            self._write(line, 0, index)

        self._t += 1
        return self._plain_image, self._colour_map


class Button(StaticRenderer):
    def __init__(self):
        super(Button, self).__init__()
        box = "( )"
        self._images = [box]


class ScoreBoard(StaticRenderer):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        box = """
 ######## 
+--------+
| 232451 |
|        |
|   x4   |
+--------+"""
        self._images = [box]


class StarPower(StaticRenderer):
    def __init__(self):
        super(StarPower, self).__init__()
        box = """
 ******
+------+
| #### |
| #### |
| #### |
| ROCK |
+------+"""
        self._images = [box]


class GameController(Scene):
    """
    Scene to control the combined Effects for the demo.

    This class handles the user input, updating the game state and updating required Effects as needed.
    Drawing of the Scene is then handled in the usual way.
    """

    def __init__(self, screen, game_state):
        self._screen = screen
        self._state = game_state
        effects = [
            Print(screen, FretboardDynamic(40, 31), 0, x=13, transparent=False),
            Print(screen, Button(), 36, x=17, transparent=False),
            Print(screen, Button(), 36, x=22, transparent=False),
            Print(screen, Button(), 36, x=27, transparent=False),
            Print(screen, Button(), 36, x=32, transparent=False),
            Print(screen, Button(), 36, x=37, transparent=False),
            Print(screen, ScoreBoard(), 33, x=0),
            Print(screen, StarPower(), 32, x=46),
        ]
        super(GameController, self).__init__(effects, -1)

    def process_event(self, event):
        # Allow standard event processing first
        if super(GameController, self).process_event(event) is None:
            return

        # If that didn't handle it, check for a key that this demo understands.
        if isinstance(event, KeyboardEvent):
            c = event.key_code
            if c in (ord("x"), ord("X")):
                raise StopApplication("User exit")
            elif c in (ord("a"), ord("A")):
                # TODO activate button one
            elif c in (ord("s"), ord("S")):
                # TODO activate button two
            elif c in (ord("d"), ord("D")):
                # TODO activate button three
            elif c in (ord("f"), ord("F")):
                # TODO activate button four
            elif c in (ord("g"), ord("G")):
                # TODO activate button five
            elif c in (ord("h"), ord("H")):
                self.add_effect(PopUpDialog(self._screen, HELP, ["OK"]))
            else:
                # Not a recognised key - pass on to other handlers.
                return event
        else:
            # Ignore other types of events.
            return event


def demo(screen, game_state):
    screen.play([GameController(screen, game_state)], stop_on_resize=True)


if __name__ == "__main__":
    game_state = GameState()
    while True:
        try:
            Screen.wrapper(demo, catch_interrupt=False, arguments=[game_state])
            sys.exit(0)
        except ResizeScreenError:
            pass
