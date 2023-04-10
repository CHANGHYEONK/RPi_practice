from pydub import AudioSegment
from pydub.playback import play
import io
import reqeusts

with open('test.wav', 'rb') as f:
    wavMem = io.BytesIO(f.read())

mp3Mem = io.BytesIO()
sound = AudioSegment.from_file(wavMem, format="wav")
sound.export(mp3Mem, format="mp3", codec="libmp3lame")

print(mp3Mem.tell()) # 파일 크기 출력
mp3Mem.seek(0)

song = AudioSegment.from_mp3(mp3Mem)
play(song)

# mp3Mem 준비
mp3Mem.seek(0) # 파일 읽기 위치를 첫 부분으로 이동
upload = {'file': ('audio.mp3', mp3Mem)} # (파일명, 파일객체)
res = requests.post('http://127.0.0.1:8080/test', files = upload)