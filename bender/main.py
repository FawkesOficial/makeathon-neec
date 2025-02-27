import time
import threading
import RPi.GPIO as GPIO
from event_handler import EventHandler
from input_handler import InputHandler
from servo import ServoController
from motor import MotorController
from distance_sensor import DistanceSensor
from fun import play_event_audio 


NSFW: bool = False

DIST_THRESHOLD: float = 20.0

event_handler = EventHandler()

# Initialize components
arm_servo = ServoController(pin=2)
head_motor_1 = MotorController(enA_pin=17, in1_pin=27, in2_pin=22)
head_motor_2 = MotorController(enA_pin=16, in1_pin=20, in2_pin=21)
dist_sensor = DistanceSensor(trigger_pin=23, echo_pin=24)

def nothing() -> None:
    pass

def presence_th():
    is_present: bool = False

    while True:
        # print("[DEBUG] reading distance")
        d: float = dist_sensor.get_distance()

        if d <= DIST_THRESHOLD and not is_present:
            print("[DEBUG] switched to present")
            event_handler.trigger_event("presence")
            is_present = True
            # time.sleep(10)
        elif d > DIST_THRESHOLD and is_present:
            is_present = False
            print("[DEBUG] no longer present")
            
def up():
    head_motor_1.foward()
    head_motor_2.backward()

    time.sleep(1.80)
    head_motor_1.stop()
    head_motor_2.stop()

def down():
    head_motor_1.backward()
    head_motor_2.foward()

    time.sleep(0.5)
    head_motor_1.stop()
    head_motor_2.stop()

# def toggle_back():
#     arm_servo.flip_switch()

# def toggle_back():
#     up()
#     time.sleep(1)
#     arm_servo.flip_switch()
#     down()

def toggle_back():
    arm_servo.set_angle(110)
    up()
    play_event_audio("lid_switch", nsfw=NSFW)
    arm_servo.move_up()
    time.sleep(0.5)
    down()
    arm_servo.move_down()


def handle_red():
    play_event_audio("red_button", nsfw=NSFW)
    

def handle_blue():
    play_event_audio("blue_button", nsfw=NSFW)

def handle_presence():
    play_event_audio("distance_sensor", nsfw=NSFW)


def main():
    GPIO.setmode(GPIO.BCM)
    
    # Initialize event handler
    # event_handler = EventHandler()

    # Register event actions
    event_handler.register_event("switch_flip", toggle_back)
    event_handler.register_event("red_button_press", handle_red)
    event_handler.register_event("blue_button_press", handle_blue)
    # event_handler.register_event("joystick_button_press", nothing)
    # event_handler.register_event("joystick_move", lambda x, y: print(f"Joystick state: {x}, {y}"))
    event_handler.register_event("presence", handle_presence)

    # Initialize input handler
    input_handler = InputHandler(event_handler)

    presence_thread = threading.Thread(target=presence_th)
    presence_thread.start()

    try:
        print("Useless box ready! Waiting for inputs...")
        while True:

            command: str = input("> ").strip().lower()

            match command:
                case "arm":
                    arm_servo.flip_switch()
                case "u":
                    up()
                case "d":
                    down()
                case "s":
                    head_motor_1.stop()
                    head_motor_2.stop()
                case "a":
                    toggle_back()
                case _:
                    pass

    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        # presence_thread.join()
        GPIO.cleanup()  # Cleanup GPIO on exit


if __name__ == "__main__":
    main()

