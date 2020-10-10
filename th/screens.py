from .controller import GameController


def stage(screen, game_state):
    screen.play([GameController(screen, game_state)], stop_on_resize=True)
