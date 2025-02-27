import RPi.GPIO as GPIO


# not used in the final project
class Joystick:
    """
    Joystick controller 
    
    datasheet: [MISSING]
    """

    def __init__(self, vrx_pin: int, vry_pin: int, sw_pin: int):
        self.vrx_pin = vrx_pin
        self.vry_pin = vry_pin
        self.sw_pin = sw_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Pull-down resistor

    def is_flipped(self):
        """Returns True if the switch is flipped"""

        return GPIO.input(self.pin) == GPIO.HIGH

