class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def write_ppm(self, file_obj):
        def to_bytes(c):
            return round(max(min(c * 255, 255), 0))

        file_obj.write(f"P3 {self.width} {self.height}\n255\n")

        for row in self.pixels:
            for color in row:
                file_obj.write(
                    f"{to_bytes(color.x)} {to_bytes(color.y)} {to_bytes(color.z)} "
                )
            file_obj.write("\n")
