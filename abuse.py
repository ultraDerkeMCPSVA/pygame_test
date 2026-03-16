#==============================================================
#   ABUSE.PY
#
#   my attempt to make a clone of 1996 video game ""Abuse""
#   to learn the PyGame library.
#
#   Version History:
#
#   MAR-6-26: Started project. Added Vec2d, SpriteObject, and Entity classes.
#
#   MAR-12-26: Moved stuff to their own files.
#
#   MAR-16-26: Fixed some errors... now it doesn't crash pygame. i haven't fully
#   figured out sprite objects yet, so nothing's on the screen yet.
#==============================================================

import pygame
import Globals
import Objects

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("abuse clone")

exit = False

gGlobals = Globals.GameGlobals
Vec2D = Globals.Vector2D

# Initalize entity list w/ free entities
for i in range(0, Globals.MAX_ENTITIES):
    gGlobals.entities.append(Objects.Entity())

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
            
    for ent in gGlobals.entities:
        # Check for thinking..
        ent.exec_think()
        
        # Update origin
        ent.org.x += gGlobals.frametime * ent.vel.x
        ent.org.y += gGlobals.frametime * ent.vel.y

    
    pygame.display.update()
