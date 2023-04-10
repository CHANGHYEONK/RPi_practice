from gtts import gTTS

from pydub import AudioSegment
from pydub.playback import play

text = "Hello, 안녕하세요."

tts = gTTS(text=text, lang='ko')
tts.save('hi.mp3')

song = AudioSegment.from_file('hi.mp3', format="mp3")
play(song)