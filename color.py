from vector import Vector


class Color(Vector):
    """Stores the RGB triplet values. Alias of Vector"""
    @classmethod
    def from_hex(cls, hex_color):
        x = int(hex_color[1:3], 16) / 256.0
        y = int(hex_color[3:5], 16) / 256.0
        z = int(hex_color[5:7], 16) / 256.0

        return cls(x, y, z)
