import math   # imports necessary packages
import random
import djitellopy
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


def tri1():  # tri functions calculate the shortest distance between the drone's current position and
    if x > wp_x:    # the target waypoint using the pythagorean theorem. It also calculates the angle the
        b = x - wp_x  # drone needs to turn using the law of cosines
    if x < wp_x:
        b = wp_x - x
    if y > wp_y:
        a = y - wp_y
    if y < wp_y:
        a = wp_y - y
    c = math.sqrt((a ** 2) + (b ** 2))  # calculates side c
    stp1 = (a ** 2) - ((b ** 2) + (c ** 2))
    stp2 = -2 * b * c
    stp3 = stp1 / stp2
    stp4 = math.degrees(math.acos(stp3))  # calculates angle A
    global turn, dis
    turn = round(180 - stp4)  # sets turn to correct angle based on flying down and to the right
    dis = round(c)  # sets flight distance to c


def tri2():  # same as tri1 but modified for different flight direction
    if x > wp_x:
        b = x - wp_x
    if x < wp_x:
        b = wp_x - x
    if y > wp_y:
        a = y - wp_y
    if y < wp_y:
        a = wp_y - y
    c = math.sqrt((a ** 2) + (b ** 2))
    stp1 = (a ** 2) - ((b ** 2) + (c ** 2))
    stp2 = -2 * b * c
    stp3 = stp1 / stp2
    stp4 = math.degrees(math.acos(stp3))
    global turn, dis
    turn = round(-1 * (180 - stp4))  # sets turn to correct angle based on flying down and to the left
    dis = round(c)


def tri3():  # same as tri1 but modified for different flight direction
    if x > wp_x:
        b = x - wp_x
    if x < wp_x:
        b = wp_x - x
    if y > wp_y:
        a = y - wp_y
    if y < wp_y:
        a = wp_y - y
    c = math.sqrt((a ** 2) + (b ** 2))
    stp1 = (a ** 2) - ((b ** 2) + (c ** 2))
    stp2 = -2 * b * c
    stp3 = stp1 / stp2
    stp4 = math.degrees(math.acos(stp3))
    global turn, dis
    turn = round(stp4 * -1)  # sets turn to correct angle based on flying up and to the left
    dis = round(c)


def tri4():  # same as tri1 but modified for different flight direction
    if x > wp_x:
        b = x - wp_x
    if x < wp_x:
        b = wp_x - x
    if y > wp_y:
        a = y - wp_y
    if y < wp_y:
        a = wp_y - y
    c = math.sqrt((a ** 2) + (b ** 2))
    stp1 = (a ** 2) - ((b ** 2) + (c ** 2))
    stp2 = -2 * b * c
    stp3 = stp1 / stp2
    stp4 = math.degrees(math.acos(stp3))
    global turn, dis
    turn = round(stp4)  # sets turn to correct angle based on flying up and to the right
    dis = round(c)


def special():  # used in the new waypoint
    get_flight()


def get_flight():  # chooses a new waypoint and executes the calculations needed for fly() function
    global turn, dis
    choose = random.randint(1, 8)  # chooses a random waypoint
    if choose == 1:  # sets random waypoint
        wp_1()
        print("Drone: Heading to waypoint 1")
    if choose == 2:
        wp_2()
        print("Drone: Heading to waypoint 2")
    if choose == 3:
        wp_3()
        print("Drone: Heading to waypoint 3")
    if choose == 4:
        wp_4()
        print("Drone: Heading to waypoint 4")
    if choose == 5:
        wp_5()
        print("Drone: Heading to waypoint 5")
    if choose == 6:
        wp_6()
        print("Drone: Heading to waypoint 6")
    if choose == 7:
        wp_7()
        print("Drone: Heading to waypoint 7")
    if choose == 8:
        wp_8()
        print("Drone: Heading to waypoint 8")
    if x == wp_x and y == wp_y:  # tests where the new waypoint is relative to drone's current position and uses the
        special()                # correct function to do calculations
        print("New waypoint is same as current position - selecting new waypoint")
    if x < wp_x and y >= wp_y:
        tri1()
        print("Drone: Target waypoint diagonal to current position - calculating shortest route to target waypoint")
    if x > wp_x and y >= wp_y:
        tri2()
        print("Drone: Target waypoint diagonal to current position - calculating shortest route to target waypoint")
    if x < wp_x and y <= wp_y:
        tri3()
        print("Drone: Target waypoint diagonal to current position - calculating shortest route to target waypoint")
    if x > wp_x and y <= wp_y:
        tri4()
        print("Drone: Target waypoint diagonal to current position - calculating shortest route to target waypoint")
    if x > wp_x and y == wp_y:
        turn = -90
        dis = x - wp_x
    if x < wp_x and y == wp_x:
        turn = 90
        dis = wp_x - x
    if x == wp_x and y > wp_y:
        turn = 180
        dis = y - wp_y
    if x == wp_x and y < wp_y:
        turn = 0
        dis = wp_y - y


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


def go_home():  # sends the drone back to the launch pad and lands it
    global dis
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
        dis = x - wp_x
    if x < wp_x and y == wp_x:
        turn = 90
        dis = wp_x - x
    if x == wp_x and y > wp_y:
        turn = 180
        dis = y - wp_y
    if x == wp_x and y < wp_y:
        turn = 0
        dis = wp_y - y
    print("Drone: Heading home")
    fly()
    time.sleep(0.5)
    print("Drone: Landing")
    drone.move_down(170)
    time.sleep(0.5)
    drone.land()


wp_home()  # sets the waypoint as home
drone.takeoff()  # drone takes off
print("Drone: Taking off")
time.sleep(.5)
drone.move_up(170)  # drone gets to altitude
wp_3()  # sends drone to waypoint 3 to ensure drone enters area required for assignment.
tri1()
time.sleep(.5)
fly()
print("Drone: Heading to waypoint 3")
for _ in itertools.repeat(None, 16):  # loops get flight and fly
    get_flight()
    fly()
    time.sleep(.5)
go_home()  # brings the drone home
print("Drone: Finished")  # indicates finished process.
