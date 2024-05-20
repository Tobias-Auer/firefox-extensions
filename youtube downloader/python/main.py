from flask import Flask, request, jsonify

from pytube import YouTube
from moviepy.editor import *
import os
import subprocess

app = Flask(__name__)

@app.route('/get_video', methods=['POST'])
def receive_video():
    data = request.get_json()
    url = data.get('url')
    if url:
        print(f"Received URL: {url}")
        get_video(url)
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "error", "message": "No URL provided"}), 400

@app.route('/get_audio', methods=['POST'])
def receive_audio():
    data = request.get_json()
    url = data.get('url')
    if url:
        print(f"Received URL: {url}")
        get_audio(url)
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "error", "message": "No URL provided"}), 400

def get_audio(video_url):
    try:
        # Download the video
        video = YouTube(video_url)
        stream = video.streams.filter(only_audio=True).first()
        filename = stream.download('data\\')

        # Convert the video to MP3
        mp4 = AudioFileClip(filename)
        mp3_filename = os.path.splitext(filename)[0] + ".mp3"
        mp4.write_audiofile(mp3_filename)

        # Delete the original video file
        os.remove(filename)
        subprocess.Popen(fr'explorer /select,"{mp3_filename}"')
    except Exception as e:
        print(f"Error downloading {video_url}: {e}")
def get_video(video_url):
    filename = YouTube(video_url).streams.first().download('data\\')
    subprocess.Popen(fr'explorer /select,"{filename}"')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7868)
