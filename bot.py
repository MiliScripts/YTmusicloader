from pyrogram import Client
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from ytmusicapi import YTMusic
import requests

# Telegram Bot Configuration
mili_song_bot = Client(
    name='name',
    api_id=0000,
    api_hash="Your Api Hash here",
    bot_token="Your Bot Token Here"
)

# Global Variable
last_song = ""

def download_youtube_audio(youtube_url):
    """
    Downloads the audio of a YouTube video and returns the filename, title, and duration.
    """
    try:
        yt = YouTube(youtube_url)
        audio = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        filename = f"{yt.title}.mp3"
        audio.download(filename=filename)
        return filename, yt.title, yt.length
    except RegexMatchError:
        return None, None, None

async def get_latest_liked_song():
    """
    Fetches the latest liked song from YouTube Music.
    """
    try:
        ytmusic = YTMusic("oauth.json")
        liked_song = ytmusic.get_library_songs(limit=1, order="recently_added")[0]
        return liked_song['videoId'], liked_song['thumbnails'][1]
    except Exception as e:
        print(f"Error fetching liked song: {e}")
        return None

def download_thumbnail(url, filename):
    """
    Downloads the thumbnail image from the provided URL.
    """
    try:
        response = requests.get(url['url'])
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return filename
        else:
            print(f"Failed to download thumbnail: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error downloading thumbnail: {e}")
        return None

async def job():
    """
    Main job to fetch the latest liked song, download it, and send it to the Telegram channel.
    """
    global last_song
    try:
        data = await get_latest_liked_song()
        if not data:
            return

        latest_song, thumbnail_url = data
        if latest_song != last_song:
            downloaded_song = download_youtube_audio(f"https://www.youtube.com/watch?v={latest_song}")
            if not downloaded_song[0]:
                return

            thumbnail = download_thumbnail(thumbnail_url, f"{latest_song}.jpg")
            filename, title, duration = downloaded_song

            await mili_song_bot.send_audio(
                chat_id=-1000000000, # custom channel id to send audio to
                audio=filename,
                caption="Your Custom Caption Here",
                thumb=thumbnail,
                duration=duration,
                title=title,
                performer="@imiligym"
            )

            os.remove(filename)
            os.remove(thumbnail)
            last_song = latest_song

    except Exception as e:
        print(f"An error occurred: {e}")

# Scheduler to run the job every 10 seconds
scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=10)

print("bot is running...")
scheduler.start()
mili_song_bot.run()
