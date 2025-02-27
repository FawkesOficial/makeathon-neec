from pyt2s.services import stream_elements


VOICE_MODEL = stream_elements.Voice.pt_PT_Wavenet_B.value 


text: str = input("text> ")

# Default Voice
# data = stream_elements.requestTTS("just testing")



# Custom Voice
data = stream_elements.requestTTS(text, VOICE_MODEL)

with open('output.mp3', 'wb') as file:
    file.write(data)
