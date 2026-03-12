#==============================================================
#   GLOBALS.PY
#   Globals for use in "ABUSE"
#
#   MAR-12-26: Created
#==============================================================

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
    def __init__(self):
        self.time = 0 # current time
        self.frametime = 0 # Delta time
        self.ent_list = []
        self.num_ents = 0 # num of ents
