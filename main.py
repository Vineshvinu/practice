from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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

START_BUTTONS = [[
  InlineKeyboardButton("JOIN HERE", url="t.me/tamil_hackers_moviess")
]]

@VINESH.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/c747f9fd6721860623ee1.jpg",
        caption="Hello {}  I am Rolex")
        reply_markup=InlineKeyboardMarkup(START_BUTTONS)
    )


print("Bot started")

VINESH.run()
