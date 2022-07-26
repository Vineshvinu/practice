from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert

@TelegramClient.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
        𝗛𝗲𝗹𝗹𝗼 {message.from_user.first_name }
	__Ok fine What is your ambition I mean goal__
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("😎" ,url="https://t.me/All_language_movie_request_group"), 
	  InlineKeyboardButton("😍", url="https://t.me/Tamil_Hackers_Moviess")
          ],[
          InlineKeyboardButton("😳", url="https://t.me/Tamil_Hackers_Moviess")
          ]]
          )
        )
