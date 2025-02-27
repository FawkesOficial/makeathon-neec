import RPi.GPIO as GPIO


# Pin configurations
SWITCH_PIN = 4
RED_BUTTON_PIN = 5
BLUE_BUTTON_PIN = 6
# JOYSTICK_X_PIN = 10
# JOYSTICK_Y_PIN = 9
# JOYSTICK_SW_PIN = 11


class InputHandler:
    """Handles all button, sensor, etc inputs"""

    def __init__(self, event_handler):
        self.event_handler = event_handler
        self.switch = False

        GPIO.setmode(GPIO.BCM)

        # Setup input pins
        GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(RED_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BLUE_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.setup(JOYSTICK_X_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # GPIO.setup(JOYSTICK_Y_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # GPIO.setup(JOYSTICK_SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Register interrupt callbacks
        GPIO.add_event_detect(SWITCH_PIN, GPIO.RISING, callback=self.switch_flipped, bouncetime=300)
        GPIO.add_event_detect(RED_BUTTON_PIN, GPIO.FALLING, callback=self.red_button_pressed, bouncetime=300)
        GPIO.add_event_detect(BLUE_BUTTON_PIN, GPIO.FALLING, callback=self.blue_button_pressed, bouncetime=300)
        # GPIO.add_event_detect(JOYSTICK_X_PIN, GPIO.BOTH, callback=self.joystick_moved, bouncetime=100)
        # GPIO.add_event_detect(JOYSTICK_Y_PIN, GPIO.BOTH, callback=self.joystick_moved, bouncetime=100)
        # GPIO.add_event_detect(JOYSTICK_SW_PIN, GPIO.FALLING, callback=self.joystick_button_pressed, bouncetime=300)

    def switch_flipped(self, channel):
        self.switch = not self.switch
        if self.switch:
            print("[+] Switch flipped!")
            self.event_handler.trigger_event("switch_flip")

    def red_button_pressed(self, channel):
        print("[+] Red Button pressed!")
        self.event_handler.trigger_event("red_button_press")

    def blue_button_pressed(self, channel):
        print("[+] Blue Button pressed!")
        self.event_handler.trigger_event("blue_button_press")

    # def joystick_button_pressed(self, channel):
    #     print("[+] Joystick Button pressed!")
    #     self.event_handler.trigger_event("button_press")
    # 
    # def joystick_moved(self, channel):
    #     x_state = GPIO.input(JOYSTICK_X_PIN)
    #     y_state = GPIO.input(JOYSTICK_Y_PIN)
    #     print(f"[+] Joystick moved! X={x_state}, Y={y_state}")
    #     self.event_handler.trigger_event("joystick_move", x_state, y_state)

