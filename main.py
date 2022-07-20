from pyrogram import Client, filters

API_ID = ""
API_HASH = ""
BOT_TOKEN = ""


VINESH = Client(
    name="VineshNew",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

print("Bot started")

VINESH.run()
