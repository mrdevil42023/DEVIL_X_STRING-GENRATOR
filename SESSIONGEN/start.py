from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID

# Renaming the filter function to avoid conflict with built-in names
def command_filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(command_filter("start"))
async def start(bot: Client, msg: Message):
    me = (await bot.get_me()).mention  # Changed variable name to avoid shadowing built-in function name 'me'
    await msg.reply_text(
        text=f"""ʜᴇʏ {msg.from_user.mention},

ᴛʜɪs ɪs {me},
ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴀʟʟ ᴛʏᴘᴇ ᴏғ sᴇssɪᴏɴs..
ᴄʟɪᴄᴋ ᴏɴ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ!

ᴍᴀᴅᴇ ʙʏ: [𝙈𝙍 𝘿𝙀𝙑𝙄𝙇](http://t.me/mrdevil12) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="𖤍 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 𖤍", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("ꨄ︎ sᴜᴘᴘᴏʀᴛ ꨄ︎", url="https://t.me/devilbotsupport"),
                    InlineKeyboardButton("ఌ︎ ᴄʜᴀɴɴᴇʟ ఌ︎", url="https://t.me/devilbots971")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
