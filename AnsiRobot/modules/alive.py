import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from AnsiRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID

PHOTO = [
    "https://te.legra.ph/file/95b4d7a9a6cc9c7a191ac.jpg",
    "https://te.legra.ph/file/d5f6796456709ff9ec758.jpg",
    "https://te.legra.ph/file/b7ce8731d34ad225d72d3.jpg",
    "https://te.legra.ph/file/bea1baad55af57a7e7f2f.jpg",
    "https://te.legra.ph/file/dd94180292e8e6e4cda4c.jpg",
]

Ansi = [
    [
        InlineKeyboardButton(text="♥️𝑳𝒐𝑽𝒆♥️", url=f"https://t.me/Brahman_Anand"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="🎈α∂∂ мє ιη уσυ ¢нαт🎈",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

lol = "https://te.legra.ph/file/d5f6796456709ff9ec758.jpg"


@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("♥️")
    await asyncio.sleep(0.5)
    await accha.edit("💜")
    await asyncio.sleep(0.5)
    await accha.edit("💚")
    await asyncio.sleep(0.5)
    await accha.edit("💛")
    await asyncio.sleep(0.5)
    await accha.edit("🧡")
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await m.reply_sticker(
        "CAACAgEAAxkBAAEIoBJkPoGRb2FOxEkHXt8xENeLHk6znAAC-gADUSkNORIJSVEUKRrhLwQ"
    )
    await umm.delete()
    await asyncio.sleep(0.2)
    await m.reply_photo(
        lol,
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ♥️ 『[❦𝙰𝚗𝚜𝚒࿐​​​​​​​​​​ ](f"t.me/{BOT_USERNAME}")』**
   ♥️💛💚💜🧡♥️💜💛💚💛♥️💛
  » ᴍʏ ᴏᴡɴᴇʀ : [Anand](https://t.me/Brahman_Anand)
  
  
  » ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : {tver}
  
  » ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : {pver}
  
  » ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : {pyver()}
   ♥️💛💚💜🧡♥️💜💛💚💛♥️💛""",
        reply_markup=InlineKeyboardMarkup(Ansi),
    )
__mod_name__ = "♦️ ᴀʟɪᴠᴇ ♦️"
__help__ = """
 ©️ [ᴍᴜᴋᴇsʜ] (f"tg://user?id={OWNER_ID}"))

*ᴜsᴇʀ ᴄᴏᴍᴍᴀɴᴅs*:
» /alive*:* ᴛᴏ ᴄʜᴇᴀᴋ ❓  ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ?"""
