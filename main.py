from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

API_ID = "15806487"
API_HASH = "c7c7fbd61954591c16599a8330faa2e3"
BOT_TOKEN = "5434454921:AAH0X5jkEx6-RDB24rHcYxiJ3Avveo3NsBo"


VINESH = Client(
    name="VineshNew",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@VINESH.on_message(filters.command("about"))
async def about_cmd(client, message):
    await message.reply_text("Bot status")

@VINESH.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("**Fuck off** My main sex commands are here as follows /start /about /help ")

@VINESH.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text("```ಹೋಗಿ ಹುಡ್ಗೀರ್ ತುಲ್ಲು ನೆಕ್ಕು  ಸೂಲೆಮಗನೇ```")

@VINESH.on_message(filters.command("love"))
async def love_cmd(client, message):
    await message.reply_text("```I HATE YOU```")

@VINESH.on_message(filters.command("code"))
async def code_cmd(client, message):
    await message.reply_text("```Error Code ninn appan thord```")

@VINESH.on_message(filters.("hi"))
async def hi(client, message):
    await message.reply_text("```HELLO```")
    
print("Bot started")

VINESH.run()
