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


@VINESH.on_message(filters.command("LIVE"))
async def live_cmd(client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/c747f9fd6721860623ee1.jpg",
        caption="Hello {}  I am Rolex")


@VINESH.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/c747f9fd6721860623ee1.jpg",
        caption="Hello {}  I am Rolex")
        reply_Markup=InlineKeyboardMarkup(
            [[
                "HELP 🤗", "VINU ❤️", "ABOUT ⚙️"
            ],[
                "JOIN MY CHANNEL"
            ]],
            resize_Keyboard=True,
            one_time_Keyboard=True
        )
    )

@VINESH.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton('📜 Support Group', url='https://t.me/cinemapranthanmaar'),
        InlineKeyboardButton('Owner ♻️', url='https://t.me/shijilraj')
    ],[
        InlineKeyboardButton('SouceCode 💡', url='https://github.com/Sh-Jil/Forwardit')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.START_TXT.format(
                message.from_user.first_name),
        parse_mode="html")


@VINESH.on_message(filters.regex("HELP 🤗"))
async def help_keyboard(client, message):
   await message.reply_text(
       reply_text="HELP KEYBOARD"
   )

    

print("Bot started")

VINESH.run()
