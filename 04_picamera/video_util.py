from subprocess import call
import os

def convert(src, dst):
    command = f'MP3Box -add {src} {dst}'
    call([command], shell = True)
    os.remove(src)