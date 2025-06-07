Map_debug = [
    [1, 1, 1, 1 , 1, 1, 1, 1 , 1, 1, 1, 1 , 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1.2, 1.2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1.1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

#>game
#size
Cell_size = 40
Ground_high = 0
#debug
debug = False
#tiles
TILE_NORMAL = 1
TILE_START = 1.1
TILE_LAP = 1.2

#lap sys
Lcounter = 0
LMaxCounter = 3
Ltriggered = False

#map sys
curent_map = Map_debug
Fcolor = None
Scolor = None
SkyColor = None
#>Player options
Px = 0
Py = 0
Pz = 0
prev_x = 0
prev_z = 0

PSpeed = 1
PmaxSpeed = 25
PAngle = 0.0
Steering = 0.0


