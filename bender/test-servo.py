import time
from servo import ServoController


servo = ServoController(4)

servo.set_angle(0)

time.sleep(2)

servo.set_angle(180)
