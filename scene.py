class Scene:
    """
    Container for all the information needed by the ray tracing engine
    """

    def __init__(self, camera, objects, width, height):
        self.camera = camera
        self.objects = objects
        self.width = width
        self.height = height
