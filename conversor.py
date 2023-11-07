from moviepy.editor import *

def conversor_mp4_para_mp3(arquivo):
    video = VideoFileClip(arquivo)
    video.audio.write_audiofile(filename=f'{arquivo}.mp3')