import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
print("volume:", volume)
print("rate:", rate)

# engine.setProperty("voice", "portugal")
engine.setProperty("rate", 170)

# engine.say("Isto é uma frase em português.")
engine.say("This isn't very good.")

engine.runAndWait()
engine.stop()

print("Done!")
