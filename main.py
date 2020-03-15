from gtts import gTTS
import os
text = "Insert your text here"
speech = gTTS(text = text, lang = "en", slow = False)
speech.save("Filename.mp3")
os.system("start text.mp3")
