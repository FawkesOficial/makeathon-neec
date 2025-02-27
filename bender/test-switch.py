from switch import Switch

s = Switch(pin=21)

while True:
    if s.is_flipped():
        print("\nFLIPPED!")
