from asciimatics.exceptions import ResizeScreenError
from asciimatics.screen import Screen
from th.state import GameState
from th.screens import stage

if __name__ == "__main__":
    game_state = GameState()
    while True:
        try:
            Screen.wrapper(stage, catch_interrupt=False, arguments=[game_state])
            sys.exit(0)
        except ResizeScreenError:
            pass
