from gtts import gTTS
from io import BytesIO
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play

while True:
    text = input("입력: ")
    if text == "exit":
        break

    # text를 BytesIO를 이용하여 음성 합성으로 출력
    f = BytesIO()
    tts = gTTS(text=text, lang='ko')
    tts.save2(f)
    f.seek(0)

    song = AudioSegment.from_mp3(f)
    play(song)