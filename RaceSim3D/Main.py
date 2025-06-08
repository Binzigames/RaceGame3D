# -------------> Importing
import pyray as pr
from DATA.Config import debug , curent_map
from DATA.Game import *
from DATA.map import find_payer_start
import DATA.Config as con
import DATA.SceneManager as sm
# -------------> Window settings
WIDTH = 800
HEIGHT = 600

# -------------> Initialize window
pr.init_window(WIDTH, HEIGHT, "RaceSim3D")
pr.set_target_fps(35)

# -------------> camera setup
camera = pr.Camera3D()


def camera_init():
    global camera
    camera = pr.Camera3D()
    camera.up = pr.Vector3(0, 5, 10)
    camera.fovy = 90.0 * con.PSpeed
    camera.projection = pr.CAMERA_PERSPECTIVE


import math

def update_camera():
    behind_distance = 4
    height_offset = 3


    angle_rad = math.radians(con.PAngle)

    behind_offset = pr.Vector3(
        -behind_distance * math.cos(angle_rad),
        height_offset,
        -behind_distance * math.sin(angle_rad)
    )

    camera.position = pr.Vector3(
        con.Px + behind_offset.x,
        con.Py + behind_offset.y,
        con.Pz + behind_offset.z
    )
    camera.target = pr.Vector3(con.Px, con.Py, con.Pz)
    camera.up = pr.Vector3(0, 1, 0)


# -------------> Game loop
con.Scolor = pr.GOLD
con.Fcolor = pr.BLACK
con.SkyColor =pr.SKYBLUE
camera_init()
find_payer_start(con.curent_map)
while not pr.window_should_close():
    update_camera()
    pr.begin_drawing()
    sm.handle_sm()
    # > SM shit
    if con.IsInGame == True:
        pr.begin_mode_3d(camera)
        Game_ui_draw()
        pr.end_mode_3d()
    pr.end_drawing()

# -------------> Cleanup
pr.close_window()
