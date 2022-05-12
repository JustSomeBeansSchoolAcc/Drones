import math
import random
import djitellopy
import time
import itertools
from djitellopy import tello
drone = tello.Tello()
drone.connect()
x = 50
y = 50
wp_x = 0
wp_y = 0
def wp_home():
    wp_x = 50
    wp_y = 50
def wp_a():
    wp_x = 100
    wp_y = 100
def wp_b():
    wp_x = 100
    wp_y = 0
def wp_c():
    wp_X = 0
    wp_y = 0
def wp_d():
    wp_x = 0
    wp_y = 100
def tri1():
    if x >= wp_x:
        b = x - wp_x
    if x <= wp_x:
        b = wp_x - x
    if y >= wp_y:
        a = y - wp_y
    if y < wp_y:
        a = wp_y - y
    c = math.sqrt((a ** 2) + (b ** 2))
    stp1 = (a ** 2) - ((b ** 2) + (c ** 2))
    stp2 = -2 * b * c
    stp3 = (stp1) / (stp2)
    stp4 = math.degrees(math.acos(stp3))
    global turn
    turn = 180 - stp4
    global dis
    dis = c
def tri2():
    if x >= wp_x:
        b = x - wp_x
    if x <= wp_x:
        b = wp_x - x
    if y >= wp_y:
        a = y - wp_y
    if y < wp_y:
        a = wp_y - y
    c = math.sqrt((a ** 2) + (b ** 2))
    stp1 = (a ** 2) - ((b ** 2) + (c ** 2))
    stp2 = -2 * b * c
    stp3 = (stp1) / (stp2)
    stp4 = math.degrees(math.acos(stp3))
    global turn
    turn = -1 * (180 - stp4)
    global dis
    dis = c
def tri3():
    if x >= wp_x:
        b = x - wp_x
    if x <= wp_x:
        b = wp_x - x
    if y >= wp_y:
        a = y - wp_y
    if y < wp_y:
        a = wp_y - y
    c = math.sqrt((a ** 2) + (b ** 2))
    stp1 = (a ** 2) - ((b ** 2) + (c ** 2))
    stp2 = -2 * b * c
    stp3 = (stp1) / (stp2)
    stp4 = math.degrees(math.acos(stp3))
    global turn
    turn = stp4 * -1
    global dis
    dis = c
def tri4():
    if x >= wp_x:
        b = x - wp_x
    if x <= wp_x:
        b = wp_x - x
    if y >= wp_y:
        a = y - wp_y
    if y < wp_y:
        a = wp_y - y
    c = math.sqrt((a ** 2) + (b ** 2))
    stp1 = (a ** 2) - ((b ** 2) + (c ** 2))
    stp2 = -2 * b * c
    stp3 = (stp1) / (stp2)
    stp4 = math.degrees(math.acos(stp3))
    global turn
    turn = stp4
    global dis
    dis = c
def get_flight():
    choose = random.randint(1, 5)
    if choose == 1:
        wp_home()
    if choose == 2:
        wp_a()
    if choose == 3:
        wp_b()
    if choose == 4:
        wp_c()
    if choose == 5:
        wp_d()
    if x <= wp_x and y >= wp_y:
        tri1()
    if x >= wp_x and y >= wp_y:
        tri2()
    if x <= wp_x and y <= wp_y:
        tri3()
    if x >= wp_x and y <= wp_y:
        tri4()
    if x >= wp_x and y == wp_y:
        global turn
        turn = 180
    if x <= wp_x and y == wp_x:
        turn = 0
    if x == wp_x and y >= wp_y:
        turn = -90
    if x == wp_x and y <= wp_y:
        turn = 90
def fly():
    cw = False
    ccw = False
    if turn >= 0:
        tello.cw(turn)
        cw = True
    if turn <= 0:
        tello.ccw(abs(turn))
        ccw = True
    if dis >= 500:
        rep = math.floor(dis / 500)
        rem = dis % 500
        for _ in itertools.repeat(None, rep):
            tello.forward(500)
        tello.forward(rem)
    if dis <= 500:
        tello.forward(dis)
    if cw == True:
        tello.ccw(turn)
    if ccw == True:
        tello.cw(turn)
    cw = False
    ccw = False
    x = wp_x
    y = wp_y
def go_home():
    wp_home()
    if x <= wp_x and y >= wp_y:
        tri1()
    if x >= wp_x and y >= wp_y:
        tri2()
    if x <= wp_x and y <= wp_y:
        tri3()
    if x >= wp_x and y <= wp_y:
        tri4()
    if x >= wp_x and y == wp_y:
        global turn
        turn = 180
    if x <= wp_x and y == wp_x:
        turn = 0
    if x == wp_x and y >= wp_y:
        turn = -90
    if x == wp_x and y <= wp_y:
        turn = 90
    fly()
    tello.down(230)
    tello.land
wp_home()
tello.up(250)
for _ in itertools.repeat(None, 20):
    get_flight()
    fly()
go_home()
print("finished")
