import subprocess
import os

def convert(src, dst):
    cmd = f'ffmpeg -i {src} -vcodec libx264 -f mp4 {dst}'
    subprocess.call(cmd, shell=True)
    os.remove(src)
