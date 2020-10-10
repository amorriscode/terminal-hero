from asciimatics.renderers import StaticRenderer, DynamicRenderer


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
