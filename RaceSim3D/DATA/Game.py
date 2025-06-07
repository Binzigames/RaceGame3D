#------------->importing
import pyray as pr
import DATA.Player as pl
import DATA.UI as ui
import DATA.Config as con
from DATA.map import draw_map

#-------------> cycles
def Game_cycle_draw():
    pl.draw_player()
    draw_map(con.curent_map)
def Game_ui_draw():
    keys = pr.KeyboardKey
    ui.draw_speedometer(int(con.PSpeed * 10))
    ui.draw_minimap(con.curent_map)
    ui.draw_laps_ui()
    if pr.is_key_down(keys.KEY_TAB):
        ui.draw_debug_menu()

def Game_controls_update():
    keys = pr.KeyboardKey
    # >movement
    if pr.is_key_down(keys.KEY_W):
        pl.accelerate()
    if pr.is_key_down(keys.KEY_S):
        pl.reverse()
    if pr.is_key_down(keys.KEY_A):
        pl.steer_left()
    elif pr.is_key_down(keys.KEY_D):
        pl.steer_right()
    if pr.is_key_down(keys.KEY_SPACE):
        pl.brake()
    else:
        pl.straighten_wheel()
    pl.update_movement()


