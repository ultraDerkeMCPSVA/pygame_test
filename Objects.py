#==============================================================
#   BASE_ENTITIES.PY
#   Entities and Sprite Objects for use in "ABUSE"
#
#   MAR-12-26: Created
#   MAR-16-26: Fixed some errors...
#==============================================================

import Globals

#=========================================
#   Sprite Object class: Loads a sprite based on
#   the provided spritename, and crops sprites according
#   to the mins and maxs we provided for x and y.
#=========================================

class SpriteObject:
    def __init__(self, idx=0, x_min=0, y_min=0, x_max=0, y_max=0):
        self.image = None
        self.x_min = x_min;
        self.y_min = y_min;
        self.x_max = x_max;
        self.y_max = y_max;

    def get_idx(name):
        count = 0
        for i in sprites:
            sprites.append(pygame.image.load(name))
            count += 1
        return count

#=========================================
#   Basic Entity
#=========================================

class Entity:
    def __init__(self):
        self.health = 0
        self.takedamage = 0
        self.solid = 0
        self.size = Globals.Vector2D(0, 0)
        self.org = Globals.Vector2D(0, 0)
        self.vel = Globals.Vector2D(0, 0)
        self.frame = 0
        self.classname = ""
        self.nextthink = 0.0
        self.free = False

    #==============================================
    # spawn() - Cycle through the Global entity list to see
    # if we can nab a free entity. If the entity is free, un-free
    # it and return it's pointer.
    #==============================================
    def spawn():
        for ent in Globals.GameGlobals.ent_list:
            if ent.free == True:
                ent.free = False
                return ent
        return -1

    #==============================================
    # think() - This function is what makes entities perform tasks.
    # To make an entity think, you must update the entity's "nextthink"
    # field, so the game will know when to make an entity think again.
    #==============================================
    def think():
        pass

    #==============================================
    # touch() - When an entity is touched by another entity, this function
    # is called.
    #==============================================
    def touch(other):
        pass
    
    def exec_think():
        if gGlobals.time > self.nextthink:
            think()
