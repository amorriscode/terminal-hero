from asciimatics.effects import Effect
from asciimatics.event import KeyboardEvent
from asciimatics.screen import Screen
from .renderers import Button


class ButtonEffect(Effect):
    def __init__(self, screen, state, key, x, y, colour):
        super(ButtonEffect, self).__init__(screen)
        self._screen = screen
        self._button_state = state
        self._key = key
        self._x = x
        self._y = y
        self._colour = colour
        self._button_text = "( )"

    def _update(self, _):
        text_weight = Screen.A_BOLD if self._button_state else Screen.A_NORMAL
        self._screen.print_at(
            self._button_text,
            colour=self._colour,
            x=self._x,
            y=self._y,
            attr=text_weight,
        )

        self._button_state = False

    def process_event(self, event):
        if isinstance(event, KeyboardEvent):
            c = event.key_code
            if c == ord(self._key):
                self._button_state = True
                return None
            else:
                return event
        else:
            return event

    @property
    def frame_update_count(self):
        # No animation required.
        return 0

    @property
    def stop_frame(self):
        # No specific end point for this Effect.  Carry on running forever.
        return 0

    def reset(self):
        # Nothing special to do.  Just need this to satisfy the ABC.
        pass
