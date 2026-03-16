#==============================================================
#   GLOBALS.PY
#   Globals for use in "ABUSE"
#
#   MAR-12-26: Created
#   MAR-16-26: Added defines for engine limits...
#==============================================================

import Objects

#=========================================
#   Limit Defines
#=========================================

MAX_ENTITIES = 4096
MAX_SPRITE_ENTRIES = 1024

#=========================================
#   Basic 2D Vector class
#=========================================

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = 0
        self.y = 0

#=========================================
#   Globals
#=========================================

class GameGlobals:
    # Current game time.
    time = 0

    # Delta between two frames
    frametime = 0

    # Number of active entities
    num_ents = 0

    # Entity Pool
    entities = []
    def __init__(self):
        pass
