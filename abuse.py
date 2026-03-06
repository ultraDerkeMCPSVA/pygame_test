#==============================================================
#   ABUSE.PY
#
#   my attempt to make a clone of 1996 video game ""Abuse""
#   to learn the PyGame library.
#
#   Version History:
#   MAR-6-26: Started project. Added Vec2d, SpriteObject, and Entity classes.
#==============================================================

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("abuse clone")

exit = False

#=========================================
#   Basic 2D Vector class
#=========================================

class Vec2D:
    def __init__(self, x=0, y=0):
        self.x = 0
        self.y = 0

#=========================================
#   Sprite Object class: Loads a sprite based on
#   the provided spritename, and crops sprites according
#   to the mins and maxs we provided for x and y.
#=========================================

sprites = []

# TODO: figure out why idx is out of bounds
class SpriteObject:
    def __init__(self, idx=0, x_min=0, y_min=0, x_max=0, y_max=0):
        self.sprite = sprites[idx]
        self.x_min = x_min;
        self.y_min = y_min;
        self.x_max = x_max;
        self.y_max = y_max;

    def get_idx(name):
        count = 0
        for i in sprites:
            if i != name:
                sprites.append(name)
            else:
                break
            count += 1
        return count

spr = SpriteObject;
player = spr.get_idx("player.png")

print(player)

test_guy = [
    spr(player, 0, 0, 69, 72),
    spr(player, 0, 0, 69, 72),
    spr(player, 0, 0, 69, 72)]

#=========================================
#   Basic Entity
#=========================================

IMMORTAL = 0
TAKEDAMAGE = 1

SOLID_NOT = 0
SOLID_YES = 1

num_of_ents = 0
ent_list = []

class Entity:
    def __init__(self):
        self.health = 0
        self.takedamage = 0
        self.solid = 0
        self.size = Vec2D(0, 0)
        self.org = Vec2D(0, 0)
        self.vel = Vec2D(0, 0)
        self.frame = 0
        self.classname = ""
        self.nextthink = 0.0
    def think():
        pass
    def touch(other):
        pass

# TODO: add transformation and collision checks in here
for ent in ent_list:
    pass

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()
