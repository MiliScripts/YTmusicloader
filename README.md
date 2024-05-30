# YouTube Music Auto Downloader and Telegram Bot 🎵🤖

This bot automatically fetches the latest liked song from YouTube Music, downloads it, and sends it to a specified Telegram channel. 

## Features ✨
- Fetches the latest liked song from YouTube Music.
- Downloads the audio of the song from YouTube.
- Sends the downloaded song to a specified Telegram channel with its thumbnail and details.

## Requirements 📋

- Python 3.6+
- A Telegram bot token (you can create one by talking to [@BotFather](https://t.me/BotFather))
- OAuth credentials for YouTube Music (follow the instructions [here](https://ytmusicapi.readthedocs.io/en/latest/setup.html) to set up OAuth)

## Installation 🛠️

1. **Clone the repository**

    ```sh
    git clone https://github.com/MiliScripts/YTmusicloader.git
    cd YTmusicloader
    ```

2. **Create and activate a virtual environment (optional but recommended)**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up OAuth for YouTube Music**

    Follow the instructions [here](https://ytmusicapi.readthedocs.io/en/latest/setup.html) to set up OAuth and download the `oauth.json` file to the project directory.

5. **Configure the Telegram bot**

    Open `bot.py` and update the following lines with your Telegram bot API details:

    ```python
    mili_song_bot = Client(
        name='milisong',
        api_id=YOUR_API_ID,
        api_hash="YOUR_API_HASH",
        bot_token="YOUR_BOT_TOKEN"
    )
    ```

## Running the Bot ▶️

Run the bot using the following command:

```sh
python bot.py
