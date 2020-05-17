class Ray:
    """
    Half-Line with an origin and a normalized direction
    """
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalized()