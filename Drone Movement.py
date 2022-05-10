import djitellopy
from djitellopy import tello

from time import sleep

drone = tello.Tello()
drone.connect()

print(me.get_battery())
