import RPi.GPIO as GPIO


class Switch:
    """
    Lever switch controller 
    
    datasheet: [MISSING]
    """

    def __init__(self, pin):
        self.pin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Pull-down resistor

    def is_flipped(self):
        """Returns True if the switch is flipped"""

        return GPIO.input(self.pin) == GPIO.HIGH

