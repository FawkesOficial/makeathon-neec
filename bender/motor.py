import time
import RPi.GPIO as GPIO


PWM_PERIOD_HZ: int = 1000

# note: the `foward()` and `backward()` methods required a little trick
#       of going in the opposite direction in order to gain some speed

class MotorController:
    """
    L298N controller 
    
    datasheet: https://www.handsontec.com/dataspecs/module/L298N%20Motor%20Driver.pdf
    """

    def __init__(self, enA_pin:int, in1_pin: int, in2_pin, speed: int = 30):
        self.enA_pin = enA_pin
        self.in1_pin = in1_pin
        self.in2_pin = in2_pin
        self.speed = speed

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.enA_pin, GPIO.OUT)
        GPIO.setup(self.in1_pin, GPIO.OUT)
        GPIO.setup(self.in2_pin, GPIO.OUT)

        # default speed low and foward
        GPIO.output(self.in1_pin, GPIO.LOW)
        GPIO.output(self.in2_pin, GPIO.LOW)

        self.pwm = GPIO.PWM(self.enA_pin, PWM_PERIOD_HZ)
        self.pwm.start(25)

    def set_speed(self, speed: int) -> None:
        self.speed = speed
        self.pwm.ChangeDutyCycle(self.speed)

    def foward(self) -> None:
        # go backwards for 300ms
        GPIO.output(self.in1_pin, GPIO.LOW)
        GPIO.output(self.in2_pin, GPIO.HIGH)
        time.sleep(0.3)

        # actually go foward
        GPIO.output(self.in1_pin, GPIO.HIGH)
        GPIO.output(self.in2_pin, GPIO.LOW)

    def backward(self) -> None:
        # go foward for 300ms
        GPIO.output(self.in1_pin, GPIO.HIGH)
        GPIO.output(self.in2_pin, GPIO.LOW)
        time.sleep(0.3)

        # actually go backwards
        GPIO.output(self.in1_pin, GPIO.LOW)
        GPIO.output(self.in2_pin, GPIO.HIGH)

    def stop(self) -> None:
        GPIO.output(self.in1_pin, GPIO.LOW)
        GPIO.output(self.in2_pin, GPIO.LOW)
    

    def cleanup(self) -> None:
        self.pwm.stop()
        GPIO.cleanup()

