from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file('test.wav', format="wav")
sound.export('converted.mp3', format="mp3", codec="libmp3lame")

# sound = AudioSegment.from_file('test.mp3', format="mp3")
# sound.export('converted.wav', format="wav")