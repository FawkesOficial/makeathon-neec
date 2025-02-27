import time
import RPi.GPIO as GPIO


class DistanceSensor:
    """
    HC-SR04 controller 
    
    datasheet: https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf
    """

    def __init__(self, trigger_pin: int, echo_pin: int) -> None:
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def get_distance(self) -> float:
        GPIO.output(self.trigger_pin, GPIO.LOW)

        # print("Waiting for sensor to settle")

        time.sleep(2)

        # print("Calculating distance")

        GPIO.output(self.trigger_pin, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(self.trigger_pin, GPIO.LOW)

        pulse_start_time = 0
        pulse_end_time = 0
        while GPIO.input(self.echo_pin) == 0:
            pulse_start_time = time.time()
        while GPIO.input(self.echo_pin) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        # print("Distance:", distance, "cm")

        return distance
