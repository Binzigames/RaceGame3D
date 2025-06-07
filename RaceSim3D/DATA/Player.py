#-------------> Importing
import pyray as pr
import DATA.Config as con
from math import cos, sin, radians

import DATA.map
from DATA.loader import load_3d_obj


#-------------> Functions
player_model = None

def draw_player():
    global player_model
    if player_model is None:
        player_model = load_3d_obj("DATA/3D/Car/Car.obj")

    player_position = pr.Vector3(con.Px, con.Py, con.Pz)
    player_rotation_axis = pr.Vector3(0, 1, 0)

    player_rotation_angle = -con.PAngle  - 90

    pr.draw_model_ex(
        player_model,
        player_position,
        player_rotation_axis,
        player_rotation_angle,
        pr.Vector3(1, 1, 1),
        pr.WHITE
    )


    #pr.draw_cube(pr.Vector3(con.Px , con.Py , con.Pz) , 5 , 2 , 2, pr.DARKPURPLE)



def accelerate():
    max_speed = con.PmaxSpeed
    acceleration = 0.2
    if con.PSpeed < max_speed:
        con.PSpeed += acceleration

def brake():
    if con.PSpeed > 0:
        con.PSpeed -= 0.3
        if con.PSpeed < 0:
            con.PSpeed = 0
def reverse():
    min_speed = -5.0
    reverse_acceleration = 0.15

    if con.PSpeed > min_speed:
        con.PSpeed -= reverse_acceleration


def update_movement():

    friction = 0.05
    if con.PSpeed > 0:
        con.PSpeed -= friction
        if con.PSpeed < 0:
            con.PSpeed = 0

    turning_radius = 3.0
    con.PAngle += con.Steering * (con.PSpeed / turning_radius)

    angle_rad = radians(con.PAngle)
    dx = cos(angle_rad) * con.PSpeed * 0.1
    dz = sin(angle_rad) * con.PSpeed * 0.1

    next_x = con.Px + dx
    next_z = con.Pz + dz
    # >colision shit X2
    if DATA.map.is_walkable(con.curent_map, next_x, next_z):
        con.Px = next_x
        con.Pz = next_z
    else:
        brake()


def steer_left():
    steer_speed = 0.15
    max_steering = 1.5
    con.Steering = max(-max_steering, con.Steering - steer_speed)

def steer_right():
    steer_speed = 0.15
    max_steering = 1.5
    con.Steering = min(max_steering, con.Steering + steer_speed)

def straighten_wheel():
    straighten_rate = 0.1
    deadzone = 0.01

    if con.Steering > deadzone:
        con.Steering -= straighten_rate
    elif con.Steering < -deadzone:
        con.Steering += straighten_rate
    else:
        con.Steering = 0.0
    #bro con is realy dead...