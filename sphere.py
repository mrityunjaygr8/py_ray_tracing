from math import sqrt


class Sphere:
    """
    This is the only 3D shape implented.
    Has center, radius and material.
    """

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray):
        """
        Checks if ray intersects the sphere.
        Returns distance to intersection.
        None if ray does not intersect.
        """
        sphere_to_ray = ray.origin - self.center
        b = 2 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 * c
        if discriminant >= 0:
            dist = (-b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist
        return None

    def normal(self, surface_point):
        """
        Returns surface normal to the point
        """
        return (surface_point - self.center).normalized()

