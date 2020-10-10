from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import StopApplication
from asciimatics.widgets import PopUpDialog

from .constants import HELP
from .renderers import FretboardDynamic, Button, ScoreBoard, StarPower
from .effects import ButtonEffect


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
            ButtonEffect(
                screen,
                self._state.button_1,
                key="a",
                x=17,
                y=36,
                colour=Screen.COLOUR_GREEN,
            ),
            ButtonEffect(
                screen,
                self._state.button_2,
                key="s",
                x=22,
                y=36,
                colour=Screen.COLOUR_RED,
            ),
            ButtonEffect(
                screen,
                self._state.button_3,
                key="d",
                x=27,
                y=36,
                colour=Screen.COLOUR_YELLOW,
            ),
            ButtonEffect(
                screen,
                self._state.button_4,
                key="f",
                x=32,
                y=36,
                colour=Screen.COLOUR_BLUE,
            ),
            ButtonEffect(
                screen,
                self._state.button_5,
                key="g",
                x=37,
                y=36,
                colour=Screen.COLOUR_MAGENTA,
            ),
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
            elif c in (ord("h"), ord("H")):
                self.add_effect(PopUpDialog(self._screen, HELP, ["OK"]))
            else:
                # Not a recognised key - pass on to other handlers.
                return event
        else:
            # Ignore other types of events.
            return event
