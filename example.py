import time

from telethon import events, utils
from telethon.sync import TelegramClient
from telethon.tl import types

from FastTelethon import download_file, upload_file

api_id: int = 
api_hash: str = ""
token = ""
client = TelegramClient("bot", api_id, api_hash)

client.start(bot_token=token)
file_to_upload = "bunny.mp4"


class Timer:
    def __init__(self, time_between=2):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False


@client.on(events.NewMessage())
async def download_or_upload(event):
    type_of = ""
    msg = None
    timer = Timer()

