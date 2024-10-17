import os
import speech_recognition as sr


if not os.path.exists('temp_audio'):
    os.makedirs('temp_audio')


def transcribe_video(video_path):
    # Extract the audio from the video file
    audio_path = "temp_audio/temp_audio.wav"
    extract_audio(video_path, audio_path)

    # Transcribe the audio
    text = transcribe_audio(audio_path)

    # Clean up the temporary audio file
    os.remove(audio_path)

    return text


def transcribe_audio(file_path):
    transcriber = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        audio = transcriber.record(source)
    
    # Recognize the speech
    try:
        text = transcriber.recognize_google(audio)
    except sr.UnknownValueError:
        print("Can't understand audio")
        text = ""
    except sr.RequestError as e:
        print("Google Service request failed; {0}".format(e))
        text = ""

    return text


def extract_audio(video_path, audio_path):
    # Extract the audio from the video file
    ffmpeg_path = r"dependencies\ffmpeg-7.1-essentials_build\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe"  # Replace this with the full path to the ffmpeg executable on your system
    command = f"{ffmpeg_path} -i {video_path} -f wav -ac 1 -ar 16000 {audio_path}"
    os.system(command)


if __name__ == "__main__":
    for folder in os.listdir("youtube_videos"):
        for video in folder:
            print(video)
            video_path = os.path.join("youtube_videos", folder)
            # text = transcribe_audio(video_path)
            caption_file = os.path.join(video_path, f"{video}.txt")
            with open(caption_file, "w") as txt_file:
                txt_file.write("tezta")

