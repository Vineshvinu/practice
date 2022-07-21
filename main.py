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
    await message.reply_text("```ಮಿಡಿಲ್ ಕ್ಲಾಸ್ ಹುಡುಗ 2022 - ಕನ್ನಡ ಡಬ್ #HDRip

250MB
https://rocklinks.net/Rl4FFOja

400MB
https://rocklinks.net/shvL

720p 800MB
https://rocklinks.net/dv7ICGB9

1080p 1.3GB
https://rocklinks.net/5B7hCoX

✅👇👇 How to download or watch movie 
https://t.me/mdisk_kannada_movie/11

MXPlayer App ಮೂಲಕ ಯಾವುದೇ ಅಡೆ ತಡೆ ಇಲ್ಲದೆ ವೀಕ್ಷಿಸಿ ಅಥವಾ  ಡೌನಲೋಡ್ ಮಾಡಿ```")

    
print("Bot started")

VINESH.run()
