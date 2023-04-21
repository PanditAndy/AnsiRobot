from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from AnsiRobot import OWNER_ID, dispatcher
from AnsiRobot import pbot as client

Ansi = "https://te.legra.ph/file/ab836a124f9484c367697.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Ansi,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

**» ♥️ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [𝐀𝐧𝐚𝐧𝐝](https://t.me/Brahman_Anand)
**» ♥️ᴩʏᴛʜᴏɴ  :** `{y()}`
**» ♥️ʟɪʙʀᴀʀʏ  :** `{o}` 
**» ♥️ᴛᴇʟᴇᴛʜᴏɴ  :** `{s}` 
**» ♥️ᴘʏʀᴏɢʀᴀᴍ  :** `{z}`

**❦𝙰𝚗𝚜𝚒࿐​​​​​​​​​​  sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•𝐁𝐫𝐚𝐡𝐦𝐚𝐧_𝐀𝐧𝐚𝐧𝐝",f"https://t.me/pandit_Andy"
                    ),
                    InlineKeyboardButton(
                        "• ʀᴇᴘᴏ •",
                        url="https://github.com/BadshahAk/AnsiRobot",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "♦️ Rᴇᴩᴏ ♦️"
_help__ = """
 /repo  ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 
 /source ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
"""
