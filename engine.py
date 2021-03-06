from image import Image
from point import Point
from ray import Ray
from color import Color


class RenderEngine:
    """Renders 3D objects as 2D using raytracing"""
    def render(self, scene):
        width = scene.width
        height = scene.height
        aspect_ratio = float(width / height)
        x_0 = -1.0
        x_1 = +1.0
        x_step = (x_1 - x_0) / (width - 1)

        y_0 = -1.0 / aspect_ratio
        y_1 = +1.0 / aspect_ratio
        y_step = (y_1 - y_0) / (height - 1)

        camera = scene.camera
        pixels = Image(width, height)

        for j in range(height):
            y = y_0 + j * y_step
            for i in range(width):
                x = x_0 + i * x_step
                ray = Ray(camera, Point(x, y) - camera)
                pixels.set_pixel(i, j, self.ray_trace(ray, scene))
            print("{:3.0f}%".format(float(j)/float(height) * 100), end="\r")

        return pixels

    def ray_trace(self, ray, scene):
        color = Color(0, 0, 0)
        # Find the nearest object hit by the ray in the scene
        dist_hit, obj_hit = self.find_nearest(ray, scene)

        if obj_hit is None:
            return color

        hit_pos = ray.origin + ray.direction * dist_hit
        hit_normal = obj_hit.normal(hit_pos)
        color += self.color_at(obj_hit, hit_pos, hit_normal, scene)
        return color

    def find_nearest(self, ray, scene):
        dist_min = None
        obj_hit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (obj_hit is None or dist < dist_min):
                dist_min = dist
                obj_hit = obj

        return (dist_min, obj_hit)

    def color_at(self, obj_hit, hit_pos, hit_normal, scene):
        material = obj_hit.material
        obj_color = material.color_at(hit_pos)
        to_cam = scene.camera - hit_pos
        specular_k = 50
        color = material.ambient * Color.from_hex("#000000")
        for light in scene.lights:
            to_light = Ray(hit_pos, light.position - hit_pos)
            # Lambert Shading
            color += (
                obj_color
                * material.diffuse
                * max(hit_normal.dot(to_light.direction), 0)
            )

            # Specular Shading
            half_vector = (to_light.direction + to_cam).normalized()
            color += (
                light.color
                * material.specular
                * max(hit_normal.dot(half_vector), 0) ** specular_k
            )
        return color
