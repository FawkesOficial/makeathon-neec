import RPi.GPIO as GPIO
import time


PWM_PERIOD_HZ: int = 50


class ServoController:
    """
    SG90 Micro Servo controller 
    
    datasheet: http://www.ee.ic.ac.uk/pcheung/teaching/DE1_EE/stores/sg90_datasheet.pdf
    """

    def __init__(self, pin: int):
        self.pin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        
        self.pwm = GPIO.PWM(self.pin, PWM_PERIOD_HZ)
        self.pwm.start(0)

        # self.set_angle(60)

    def set_angle(self, angle_deg: int) -> None:
        """Convert angle to duty cycle and move servo"""

        duty = 2 + (angle_deg / 18)
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(0.5)
        self.pwm.ChangeDutyCycle(0)

    def flip_switch(self) -> None:
        """Move arm to flip switch back"""

        self.move_up()
        time.sleep(0.3)
        self.move_down()

    def move_up(self) -> None:
        self.set_angle(170)
    
    def move_down(self) -> None:
        self.set_angle(10)

    def cleanup(self) -> None:
        self.pwm.stop()
        GPIO.cleanup()

