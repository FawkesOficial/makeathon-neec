from distance_sensor import DistanceSensor


sensor = DistanceSensor(trigger_pin=23, echo_pin=24)

sensor.get_distance()
