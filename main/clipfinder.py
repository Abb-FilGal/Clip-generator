import speech_recognition as sr
import os
import moviepy.editor as mp
import datetime

def get_audio_file(file):
    if file.endswith('.mp4'):
        video = mp.VideoFileClip(file)
        audio = video.audio
        audio.write_audiofile('temp.wav')
        return 'temp.wav'
    elif file.endswith('.wav'):
        return file

def get_segments(file):
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = r.record(source)
        text = r.recognize_google(audio, show_all=True)
        words = text['results'][0]['alternatives'][0]['words']
        segments = []
        start_time = 0
        for word in words:
            if word['case'] == 'notitle':
                segments.append((start_time, word['start']))
                start_time = word['start']
        segments.append((start_time, words[-1]['end']))
        return segments

def cut_clips(segments, file):
    for i, (start, end) in enumerate(segments):
        if end - start > 60:
            continue
        clip = mp.VideoFileClip(file).subclip(start, end)
        clip.write_videofile(f'clips/clip{i}.mp4', codec='libx264', audio_codec='aac')
