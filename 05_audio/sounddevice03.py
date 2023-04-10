import sounddevice as sd
import soundfile as sf
from io import BytesIO

fs = 16000 # Sample rate
seconds = 3 # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait() 

mem_wav = BytesIO()
sf.write(mem_wav, myrecording, fs, format="wav") # Save as WAV file 
mem_wav.seek(0)

# mem_wav 전송