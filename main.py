#!/usr/bin/env python3
from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine


def main():
    WIDTH = 320
    HEIGHT = 200
    camera = Vector(0, 0, -1)

    objects = [
        Sphere(Point(0, -0.25, 0), 0.1, Color.from_hex("#FF0000")),
        Sphere(Point(0, 0, 0), 0.1, Color.from_hex("#FFFF00")),
        Sphere(Point(0, 0.25, 0), 0.1, Color.from_hex("#00FF00")),
    ]
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()

    image = engine.render(scene)

    with open("black.ppm", "w+") as f:
        image.write_ppm(f)


if __name__ == '__main__':
    main()
