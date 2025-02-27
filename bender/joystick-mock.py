import RPi.GPIO as GPIO
import time

# Pin Definitions
VRx_PIN = 2  # Joystick X-axis
VRy_PIN = 3  # Joystick Y-axis

VRx_PIN = 27  # Joystick X-axis
VRy_PIN = 17  # Joystick Y-axis

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(VRx_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(VRy_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def detect_joystick_movement():
    last_state_x = GPIO.input(VRx_PIN)
    last_state_y = GPIO.input(VRy_PIN)

    while True:
        current_state_x = GPIO.input(VRx_PIN)
        current_state_y = GPIO.input(VRy_PIN)

        if current_state_x != last_state_x or current_state_y != last_state_y:
            print("Joystick moved!")
            print("x:", current_state_x, "y:", current_state_y)
            last_state_x = current_state_x
            last_state_y = current_state_y

        time.sleep(0.05)  # Small delay to avoid excessive CPU usage

try:
    print("Detecting joystick movement...")
    detect_joystick_movement()
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    GPIO.cleanup()

