#-------------> importing (WOW again)
import pyray as pr
import DATA.Config as con
import os
#> map draw
def draw_map(current_map, cell_size=con.Cell_size, height=con.Ground_high):
    if not isinstance(current_map, list):
        print("Map data is not a list!")
        return

    for y in range(len(current_map)):
        row = current_map[y]
        if not isinstance(row, list):
            print(f"Row {y} is not a list!")
            continue

        for x in range(len(row)):
            tile = row[x]
            if tile == 1 or tile == 1.1:
                position = pr.Vector3(
                    x * cell_size + cell_size / 2,
                    height / 2,
                    y * cell_size + cell_size / 2
                )
                size = pr.Vector3(cell_size, height, cell_size)
                pr.draw_cube_v(position, size, con.Fcolor)
                pr.draw_cube_wires_v(position, size, con.Scolor)
            elif tile == 1.2 :
                position = pr.Vector3(
                    x * cell_size + cell_size / 2,
                    height / 2,
                    y * cell_size + cell_size / 2
                )
                size = pr.Vector3(cell_size, height+ 0.1, cell_size)
                pr.draw_cube_v(position, size, con.Scolor)

            else:
                pass


#-------------> colision shit
def handle_lap_tile():
    con.Lcounter += 1
    con.Ltriggered = True
    print(f"Lap: {con.Lcounter}")

def is_correct_direction(prev_x, prev_z, x, z, allowed_axis="z", direction=1):

    if allowed_axis == "z":
        return (z - prev_z) * direction > 0.1
    elif allowed_axis == "x":
        return (x - prev_x) * direction > 0.1
    return False

def is_walkable(map_data, x, z, debug=con.debug, cell_size=con.Cell_size, height=con.Ground_high):
    map_x = int(x // cell_size)
    map_z = int(z // cell_size)

    in_bounds = 0 <= map_z < len(map_data) and 0 <= map_x < len(map_data[map_z])
    if not in_bounds:
        return False

    tile = map_data[map_z][map_x]
    walkable = tile in (1, 1.1, 1.2)

    if tile == 1.2:
        if not con.Ltriggered and is_correct_direction(con.prev_x, con.prev_z, x, z, allowed_axis="z", direction=1):
            handle_lap_tile()
    else:
        con.Ltriggered = False


    con.prev_x = x
    con.prev_z = z

    if debug:
        cube_pos = pr.Vector3(
            map_x * cell_size + cell_size / 2,
            height / 2,
            map_z * cell_size + cell_size / 2
        )
        cube_size = pr.Vector3(cell_size, height, cell_size)
        color = pr.GREEN if walkable else pr.RED
        pr.draw_cube_v(cube_pos, cube_size, color)
        pr.draw_cube_wires_v(cube_pos, cube_size, pr.BLACK)

    return walkable

#-------------> find_player_start

def find_payer_start(current_map):
    cell_size = con.Cell_size
    height = con.Ground_high

    if not isinstance(current_map, list):
        print("Map data is not a list!")
        return

    for y in range(len(current_map)):
        row = current_map[y]
        if not isinstance(row, list):
            print(f"Row {y} is not a list!")
            continue

        for x in range(len(row)):
            tile = row[x]
            if tile == 1.1:
                world_x = x * cell_size
                world_y = height
                world_z = y * cell_size

                con.Py = world_y
                con.Pz = world_z
                con.Px = world_x
                con.prev_z = world_z
                con.prev_x = world_x
                print(f"Player start found at tile ({x}, {y}) -> world coords ({world_x}, {world_y}, {world_z})")


