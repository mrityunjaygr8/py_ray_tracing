from color import Color


class Light:
    """
    Represents a point light source of a certain color
    """

    def __init__(self, position, color=Color.from_hex("#FFFFFF")):
        self.position = position
        self.color = color
