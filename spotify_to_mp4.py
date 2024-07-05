import os
import tkinter as tk
from tkinter import messagebox
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube
import yt_dlp as youtube_dl  # Use yt-dlp instead of youtube-dl
import imageio_ffmpeg as ffmpeg
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Debugging: Print the environment variables to verify they are loaded correctly
print("SPOTIPY_CLIENT_ID:", os.getenv('SPOTIPY_CLIENT_ID'))
print("SPOTIPY_CLIENT_SECRET:", os.getenv('SPOTIPY_CLIENT_SECRET'))

# Spotify API credentials
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

if not SPOTIPY_CLIENT_ID or not SPOTIPY_CLIENT_SECRET:
    raise Exception("Spotify API credentials not set. Please check your .env file.")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
))

# Directory to save downloaded songs
DOWNLOAD_DIRECTORY = "/Users/liamwalton/DevelopmentLocal/spotify_to_mp4/Downloaded Songs"

if not os.path.exists(DOWNLOAD_DIRECTORY):
    os.makedirs(DOWNLOAD_DIRECTORY)

def download_playlist():
    url = entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a Spotify URL")
        return

    try:
        # Extract ID and type from the URL
        print(f"Original URL: {url}")  # Debugging: Print the original URL
        if "spotify.com/playlist/" in url:
            spotify_id = url.split("spotify.com/playlist/")[-1].split("?")[0]
            spotify_type = "playlist"
        elif "spotify.com/album/" in url:
            spotify_id = url.split("spotify.com/album/")[-1].split("?")[0]
            spotify_type = "album"
        else:
            raise ValueError("Invalid URL format")
        
        print(f"Extracted ID: {spotify_id}, Type: {spotify_type}")  # Debugging: Print the extracted ID and type

        # Fetch details based on type
        if spotify_type == "playlist":
            results = sp.playlist(spotify_id)
            tracks = results['tracks']['items']
        elif spotify_type == "album":
            results = sp.album(spotify_id)
            tracks = results['tracks']['items']
        
        # Debugging: Print the details
        print(f"Details: {results}")

        for item in tracks:
            track = item['track'] if spotify_type == "playlist" else item
            search_and_download(track['name'], track['artists'][0]['name'])
        messagebox.showinfo("Success", f"{spotify_type.capitalize()} downloaded successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_and_download(song_name, artist_name):
    query = f"{song_name} {artist_name} audio"
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(DOWNLOAD_DIRECTORY, f"{song_name}.%(ext)s")
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch:{query}"])

root = tk.Tk()
root.title("Spotify to MP4")

tk.Label(root, text="Spotify URL:").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Download", command=download_playlist).pack(pady=20)

if __name__ == "__main__":
    root.mainloop()