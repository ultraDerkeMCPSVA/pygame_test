#==============================================================
#   ABUSE.PY
#
#   my attempt to make a clone of 1996 video game ""Abuse""
#   to learn the PyGame library.
#
#   Version History:
#   MAR-6-26: Started project. Added Vec2d, SpriteObject, and Entity classes.
#   MAR-12-26: Moved stuff to their own files.
#==============================================================

import pygame
import GLOBALS
import BASE_ENTITIES

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("abuse clone")

exit = False

gGlobals = GLOBALS.GameGlobals
Vec2D = GLOBALS.Vector2D
    

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
            
    # TODO: add transformation and collision checks in here
    for ent in gGlobals.ent_list:
        ent.org.x += gGlobals.frametime * ent.vel.x
        ent.org.y += gGlobals.frametime * ent.vel.y
        ent.exec_think()

    
    pygame.display.update()
