import math   # imports necessary packages
import random
import time
import itertools
from djitellopy import tello
drone = tello.Tello()
drone.connect()
x = 90  # designates global variables
y = 870
wp_x = 0
wp_y = 0
turn = 0
dis = 0
cos = 0


def wp_home():  # wp stands for waypoint. Each wp function sets the coordinates of the new target waypoint
    global wp_x, wp_y
    wp_x = 90
    wp_y = 870


def wp_1():
    global wp_x, wp_y
    wp_x = 100
    wp_y = 800


def wp_2():
    global wp_x, wp_y
    wp_x = 500
    wp_y = 800


def wp_3():
    global wp_x, wp_y
    wp_x = 500
    wp_y = 100


def wp_4():
    global wp_x, wp_y
    wp_x = 100
    wp_y = 100


def wp_5():
    global wp_x, wp_y
    wp_x = 200
    wp_y = 700


def wp_6():
    global wp_x, wp_y
    wp_x = 400
    wp_y = 700


def wp_7():
    global wp_x, wp_y
    wp_x = 400
    wp_y = 200


def wp_8():
    global wp_x, wp_y
    wp_x = 200
    wp_y = 200


def tri_body():
    global cos, dis
    if x > wp_x:  # finds legs b and a
        b = x - wp_x
    if x < wp_x:
        a = wp_x - x
    if y > wp_y:
        b = y - wp_y
    if y < wp_y:
        a = wp_y - y
    c = math.sqrt((a ** 2) + (b ** 2))  # calculates side c
    cos = math.degrees(math.acos((((c ** 2) + (b ** 2)) - (a ** 2)) / (2 * b * c)))  # gets angle 'A' of
    dis = round(c)


def tri1():  # tri functions call the tri_body function then set turn based on where the waypoint is
    global turn
    tri_body()
    turn = round(180 - cos)  # sets turn to correct angle based on flying down and to the right
    time.sleep(.5)


def tri2():  # same as tri1 but modified for different flight direction
    global turn
    tri_body()
    turn = round(-1 * (180 - cos))  # sets turn to correct angle based on flying down and to the left
    time.sleep(.5)


def tri3():  # same as tri1 but modified for different flight direction
    tri_body()
    global turn
    turn = round(cos * -1)  # sets turn to correct angle based on flying up and to the left
    time.sleep(.5)


def tri4():  # same as tri1 but modified for different flight direction
    global turn
    tri_body()
    turn = round(cos)  # sets turn to correct angle based on flying up and to the right


def special():  # used in the new waypoint
    get_flight()


def get_flight():  # chooses a random waypoint
    global turn
    choose = random.randint(1, 8)
    if choose == 1:
        wp_1()
    if choose == 2:
        wp_2()
    if choose == 3:
        wp_3()
    if choose == 4:
        wp_4()
    if choose == 5:
        wp_5()
    if choose == 6:
        wp_6()
    if choose == 7:
        wp_7()
    if choose == 8:
        wp_8()
    if x == wp_x and y == wp_y:  # tests where the new waypoint is relative to drone's current position and uses the
        special()  # correct function to do calculations
    if x < wp_x and y >= wp_y:
        tri1()
    if x > wp_x and y >= wp_y:
        tri2()
    if x < wp_x and y <= wp_y:
        tri3()
    if x > wp_x and y <= wp_y:
        tri4()
    if x > wp_x and y == wp_y:
        turn = -90
    if x < wp_x and y == wp_x:
        turn = 90
    if x == wp_x and y > wp_y:
        turn = 180
    if x == wp_x and y < wp_y:
        turn = 0


def fly():  # executes flying the drone
    global x, y
    cw = False
    ccw = False
    if turn > 0:
        drone.rotate_clockwise(turn)  # determines whether drone needs to rotate clockwise or counterclockwise
        cw = True
        time.sleep(.5)
    if turn < 0:
        drone.rotate_counter_clockwise(abs(turn))
        ccw = True
        time.sleep(.5)
    if dis > 500:  # if the drone's path is more than 5 meters creates an if loop with remainder
        rep = math.floor(dis / 500)
        rem = dis % 500
        for _ in itertools.repeat(None, rep):
            drone.move_forward(500)
        drone.move_forward(rem)
        time.sleep(.5)
    if dis < 500:
        drone.move_forward(dis)
        time.sleep(.5)
    if cw is True:  # rotates the drone back to forward position
        drone.rotate_counter_clockwise(turn)
        time.sleep(.5)
    if ccw is True:
        drone.rotate_clockwise(turn)
        time.sleep(.5)
    x = wp_x
    y = wp_y
    time.sleep(.5)


def go_home():  # sends the drone back to the launch pad and lands it
    wp_home()
    if x < wp_x and y > wp_y:
        tri1()
    if x > wp_x and y > wp_y:
        tri2()
    if x < wp_x and y < wp_y:
        tri3()
    if x > wp_x and y < wp_y:
        tri4()
    if x > wp_x and y == wp_y:
        global turn
        turn = -90
    if x < wp_x and y == wp_x:
        turn = 0
    if x == wp_x and y > wp_y:
        turn = 180
    if x == wp_x and y < wp_y:
        turn = 0
    fly()
    drone.move_down(200)
    drone.land()


wp_home()  # sets the waypoint as home
drone.takeoff()  # drone takes off
time.sleep(.5)
drone.move_up(200)  # drone gets t altitude
for _ in itertools.repeat(None, 16):  # loops get flight and fly
    get_flight()
    time.sleep(.5)
    fly()
    time.sleep(.5)
go_home()  # brings the drone home
print("finished")  # indicates finished process.
