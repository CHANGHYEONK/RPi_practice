from pydub import AudioSegment
from pydub.playback import play
from threading import Thread

song = AudioSegment.from_file('output.wav', format="wav")
# song = AudioSegment.from_wav('test.wav')

Thread(target=play, args=(song,)).start()
# play(song)
print("Main Exit")