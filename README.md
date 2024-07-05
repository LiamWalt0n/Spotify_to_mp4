


# Spotify to MP4

A simple desktop GUI application that allows you to download songs from a Spotify playlist or album and convert them to MP3 format.

## Features

- Download songs from Spotify playlists and albums
- Convert downloaded songs to MP3 format
- Simple and intuitive GUI

## Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

## Setup

1. Clone the Repository

First, clone the repository to your local machine:

git clone https://github.com/LiamWalt0n/Spotify_to_mp4.git
cd Spotify_to_mp4

2. Create a Virtual Environment and Install Dependencies

Use Pipenv to create a virtual environment and install the necessary dependencies:
pipenv install

3. Create a .env File

Create a .env file in the root directory of the project and add your Spotify API credentials. You can obtain these credentials by creating a new application in the Spotify Developer Dashboard.

SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret

Replace your_spotify_client_id and your_spotify_client_secret with your actual Spotify API credentials.

4. Run the Application

Use Pipenv to run the application:

pipenv run python spotify_to_mp4.py

Usage

	1.	Open the application.
	2.	Enter the Spotify playlist or album URL.
	3.	Click “Download” to download the songs and convert them to MP3 format.

Troubleshooting

Common Issues

	•	Invalid Client: Ensure that your Spotify API credentials are correctly set in the .env file.
	•	Unable to Extract Uploader ID: Make sure you have the latest version of yt-dlp. You can update it using:

pip install --upgrade yt-dlp

FAQ

	•	How do I find my Spotify API credentials?
	•	Go to the Spotify Developer Dashboard, create a new application, and you will find your Client ID and Client Secret.
	•	Where are the downloaded songs saved?
	•	The songs are saved in the Downloaded Songs directory within the project folder.

Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

License

This project is licensed under the MIT License. See the LICENSE file for details.

You can copy and paste this markdown content into your `README.md` file in your project directory.
