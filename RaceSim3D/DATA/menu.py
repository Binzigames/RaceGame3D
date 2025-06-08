#-------------> importing
import pyray as pr
from math import sin, cos
from DATA.Config import Curent_scene_index
#-------------> draw function
buttons = ["ARCADE MODE", "TUTORIAL", "SETINGS" , "AUTHOR" , "EXIT"]
game_name = "RACE Sim 3d"


button_width = 150
button_height = 40
button_padding = 10

def draw_main_menu():
    global Curent_scene_index
    pr.draw_text(game_name, 10, 10, 60, pr.ORANGE)

    pr.draw_rectangle(0, pr.get_screen_height() - 100, pr.get_screen_width(), 300, pr.ORANGE)


    total_width = len(buttons) * button_width + (len(buttons) - 1) * button_padding
    start_x = pr.get_screen_width() // 2 - total_width // 2
    y = pr.get_screen_height() - 90

    mouse_pos = pr.get_mouse_position()
    mouse_x = mouse_pos.x
    mouse_y = mouse_pos.y

    for i, label in enumerate(buttons):
        x = start_x + i * (button_width + button_padding)
        is_hovered = (
            x <= mouse_x <= x + button_width and
            y <= mouse_y <= y + button_height
        )
        color = pr.DARKGRAY if is_hovered else pr.LIGHTGRAY

        pr.draw_rectangle(x, y, button_width, button_height, color)


        text_size = pr.measure_text(label, 20)
        pr.draw_text(label, x + button_width // 2 - text_size // 2, y + 15, 20, pr.BLACK)


        if is_hovered and pr.is_mouse_button_pressed(pr.MOUSE_LEFT_BUTTON):
            if label == "ARCADE MODE":
                Curent_scene_index = 1
                print("starting the game")
            #elif label == "EXIT":
