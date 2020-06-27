from asciimatics.effects import Print
from asciimatics.renderers import FigletText, StaticRenderer, Box
from asciimatics.scene import Scene
from asciimatics.screen import Screen


class Fretboard(StaticRenderer):
    """
    Renders a simple box using ASCII characters.  This does not render in
    extended box drawing characters as that requires non-ASCII characters in
    Windows and direct access to curses in Linux.
    """

    def __init__(self, width, height, uni=False):
        """
        :param width: The desired width of the box.
        :param height: The desired height of the box.
        :param uni: Whether to use unicode box characters or not.
        """
        super(Fretboard, self).__init__()
        if uni:
            box = ""
            for _ in range(height - 2):
                box += u"│" + u" " * (width - 2) + u"│\n"
        else:
            box = ""
            for _ in range(height - 2):
                box += "|" + " " * (width - 2) + "|\n"
        self._images = [box]


class Button(StaticRenderer):
    """
    Renders a simple box using ASCII characters.  This does not render in
    extended box drawing characters as that requires non-ASCII characters in
    Windows and direct access to curses in Linux.
    """

    def __init__(self, width, height, uni=False):
        """
        :param width: The desired width of the box.
        :param height: The desired height of the box.
        """
        super(Button, self).__init__()
        box = u"." + u"-" * (width - 2) + u".\n"
        for _ in range(height - 2):
            box += u"|" + u"#" * (width - 2) + u"|\n"
        box += u"." + u"-" * (width - 2) + u".\n"
        self._images = [box]


def demo(screen):
    effects = [
        Print(screen, Fretboard(int(screen.width / 2), screen.height, uni=True), 0),
        Print(screen, Button(9, 3), int(screen.height - 5), x=int(screen.width / 2)),
    ]
    screen.play([Scene(effects, 500)])


Screen.wrapper(demo)
