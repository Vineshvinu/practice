from pyrogram import Client, filters

API_ID = "15806487"
API_HASH = "c7c7fbd61954591c16599a8330faa2e3"
BOT_TOKEN = "5434454921:AAH0X5jkEx6-RDB24rHcYxiJ3Avveo3NsBo"


VINESH = Client(
    name="VineshNew",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

print("Bot started")

VINESH.run()
