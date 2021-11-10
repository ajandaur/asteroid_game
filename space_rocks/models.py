from pygame.math import Vector2
# update drawing of Spaceship
from pygame.transform import rotozoom

from utils import load_sprite, wrap_position

UP = Vector2(0, -1)


class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self, surface):
        self.position = wrap_position(self.position + self.velocity, surface)

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius


class Spaceship(GameObject):
    MANUVERABILITY = 3
    ACCELERATION = 0.25

    def __init__(self, position):
        # make copy of the original UP vector
        self.direction = Vector2(UP)

        super().__init__(position, load_sprite("spaceship"), Vector2(0))

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANUVERABILITY * sign
        # rotate_ip() rotates objet in place by given angle in degrees
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        # calculate angle by which one vector needs to be rotated to point in
        # direction of other vector
        angle = self.direction.angle_to(UP)
        # takes original image, angle it should rotate, and scale and applies to sprite
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        # return a vector with half the length of the original
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION

class Asteroid(GameObject):
    def __init__(self, position):
        super().__init__(position, load_sprite("asteroid"), (0, 0))
