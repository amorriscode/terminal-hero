from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import StopApplication
from asciimatics.widgets import PopUpDialog

from .constants import HELP
from .renderers import FretboardDynamic, Button, ScoreBoard, StarPower


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
                pass
            elif c in (ord("s"), ord("S")):
                # TODO activate button two
                pass
            elif c in (ord("d"), ord("D")):
                # TODO activate button three
                pass
            elif c in (ord("f"), ord("F")):
                # TODO activate button four
                pass
            elif c in (ord("g"), ord("G")):
                # TODO activate button five
                pass
            elif c in (ord("h"), ord("H")):
                self.add_effect(PopUpDialog(self._screen, HELP, ["OK"]))
            else:
                # Not a recognised key - pass on to other handlers.
                return event
        else:
            # Ignore other types of events.
            return event
