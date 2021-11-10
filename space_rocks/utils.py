from pygame.image import load
from pygame.math import Vector2


def load_sprite(name, with_alpha=True):
    path = f"/Users/anmoljandaur/Projects/ajandaur/asteroid_game/assets/sprites/{name}.png"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()


def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    # use modulo operator to never leave area of surface
    return Vector2(x % w, y % h)
