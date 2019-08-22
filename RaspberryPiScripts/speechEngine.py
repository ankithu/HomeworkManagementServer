from gtts import gTTS
import os
def say(text):
	tts = gTTS(text=text, lang='en')
	tts.save("text.mp3")
	os.system("mpg321 text.mp3")
