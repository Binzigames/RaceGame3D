#------------->importing
import pyray as pr
import DATA.menu as m
import DATA.Game as g
from DATA.Config import *

#-------------> draw_handler
def handle_sm():
    global Curent_scene_index , IsInGame
    if Curent_scene_index == -1:
        print("loading")
    if Curent_scene_index == 0:
        m.draw_main_menu()
        IsInGame = False
    elif Curent_scene_index == 1:
        pr.clear_background(SkyColor)
        # >3D mode
        g.Game_cycle_draw()
        g.Game_controls_update()
        IsInGame = True

#> defs

def change_scene(int):
    global Curent_scene_index
    Curent_scene_index = int
    print(f"changing scene to : {int}")