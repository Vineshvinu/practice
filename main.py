from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
 

API_ID = "15806487"
API_HASH = "c7c7fbd61954591c16599a8330faa2e3"
BOT_TOKEN = "5351190742:AAHgoJ3qT7WgJNCakq1pxe4sRerHYH783W8"


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
    await message.reply_text("**Hello {message.from_user.first_name} My main  commands are here as follows /start /about /help /love**")

@VINESH.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text("```I think you are genius and you can't get any help from others```")

@VINESH.on_message(filters.command("love"))
async def love_cmd(client, message):
    await message.reply_text("```ME 2 ❤️ you```")

@VINESH.on_message(filters.command("code"))
async def code_cmd(client, message):
    await message.reply_text("```Coding in process.............99%```")


print("Bot started")

VINESH.run()
