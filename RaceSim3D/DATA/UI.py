#------------->importing
import pyray as pr
import DATA.Config as con
from numpy import cos , sin

#-------------> draw_game_ui
def draw_laps_ui():
    x = pr.get_screen_width() - 250
    y = pr.get_screen_height() - 260

    pr.draw_text(f"LAP :" , x , y , 30 , pr.RED)
    pr.draw_text(f"{con.Lcounter} / {con.LMaxCounter}", x, y + 40, 20, pr.WHITE)
def draw_speedometer(speed):

    center_x = pr.get_screen_width() - 100
    center_y = pr.get_screen_height() - 100
    radius = 100

    pr.draw_circle_lines(center_x, center_y, radius, pr.GRAY)

    max_speed = con.PmaxSpeed * 10
    num_marks = 13
    for i in range(num_marks):
        angle_deg = -120 + (i * 240 / (num_marks - 1))
        angle_rad = angle_deg * (3.1416 / 180)
        x1 = int(center_x + (radius - 10) * cos(angle_rad))
        y1 = int(center_y + (radius - 10) * sin(angle_rad))
        x2 = int(center_x + radius * cos(angle_rad))
        y2 = int(center_y + radius * sin(angle_rad))
        pr.draw_line(x1, y1, x2, y2, pr.RED)


    speed = min(speed, max_speed)
    angle = -120 + (speed / max_speed) * 240
    angle_rad = angle * (3.1416 / 180)
    x_arrow = int(center_x + (radius - 20) * cos(angle_rad))
    y_arrow = int(center_y + (radius - 20) * sin(angle_rad))
    pr.draw_line(center_x, center_y, x_arrow, y_arrow, pr.RED)


    pr.draw_text(f"{int(speed)} km/h", center_x - 95, center_y - 20 , 20, pr.WHITE)

def draw_debug_menu():
    pr.draw_rectangle_gradient_v(2 , 2 , 300 , pr.get_screen_height() // 2 , pr.BLACK , pr.DARKGRAY)
    pr.draw_text("debug mode V2.0" , 5 , 3 , 30,pr.RED)
    pr.draw_text(f"fps : {pr.get_fps()} / 35", 5, 40, 20, pr.WHITE)
    pr.draw_text(f"x: {int(con.Px)} y : {int(con.Py)} z : {int(con.Pz)}", 5, 60, 20, pr.WHITE)
    pr.draw_text(f"Pspeed {int(con.PSpeed)}", 5, 80, 20, pr.WHITE)
    pr.draw_text(f"Pangle {int(con.PAngle)}", 5, 100, 20, pr.WHITE)
    pr.draw_text(f"laps : {con.Lcounter} / {con.LMaxCounter}", 5, 120, 20, pr.WHITE)
    pr.draw_rectangle_lines(2 , 2 , 300 , pr.get_screen_height() // 2 , pr.WHITE )

def draw_minimap(map_data):
    view_radius = 8
    cell_size = con.Cell_size
    minimap_size = 100
    half_map_px = minimap_size // 2

    world_x = con.Px
    world_y = con.Pz

    player_tile_x = world_x / cell_size
    player_tile_y = world_y / cell_size

    center_x = pr.get_screen_width() - 50
    center_y = pr.get_screen_height() - 260

    pr.draw_circle(center_x, center_y, half_map_px, pr.GRAY)

    scale = minimap_size / (view_radius * 2 * cell_size)

    for dy in range(-view_radius, view_radius + 1):
        for dx in range(-view_radius, view_radius + 1):
            map_x = int(player_tile_x + dx)
            map_y = int(player_tile_y + dy)

            if 0 <= map_y < len(map_data) and 0 <= map_x < len(map_data[0]):
                tile = map_data[map_y][map_x]

                rel_x = (map_x + 0.5 - player_tile_x) * cell_size
                rel_y = (map_y + 0.5 - player_tile_y) * cell_size

                draw_x = center_x + int(rel_x * scale)
                draw_y = center_y - int(rel_y * scale)

                dist_sq = (draw_x - center_x) ** 2 + (draw_y - center_y) ** 2

                if dist_sq > half_map_px ** 2:
                    continue

                color = pr.GRAY
                if tile == 1 or tile == 1.1:
                    color = pr.YELLOW
                if tile == 1.2:
                    color = pr.RED

                pr.draw_rectangle(draw_x - 2, draw_y - 2, 4, 4, color)

    rect_width = 6
    rect_height = 10
    pr.draw_rectangle(center_x - rect_width // 2, center_y - rect_height // 2, rect_width, rect_width, pr.RED)

    pr.draw_circle_lines(center_x, center_y, half_map_px, pr.DARKGRAY)


