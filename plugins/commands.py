"""
RadioPlayerV2, Telegram Voice Chat Bot
Copyright (C) 2021  Asm Safone <https://t.me/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = " **ＨＥＹ  ʙɪᴛᴄʜ  [{}](tg://user?id={})**,\n

🎵 𝗜  𝗔𝗺 𝗔 𝗨𝗹𝘁𝗿𝗮 𝗠𝘂𝘀𝗶𝗰 𝗣𝗹𝗮𝘆𝗲𝗿 ♠️\n\n❍ 𝐌𝐚 𝐍𝐚𝐦𝐞 ➭ **[𝗠𝗛𝗗'𝗦 𝗦𝗢𝗡𝗚 𝗕𝗢𝗧](https://t.me/mhd_creation_4_bot)**\n\n❍ 𝐌𝐚 𝐎𝐧𝐰𝐞𝐫 ➭ **[𝗠𝗛𝗗_𝗧𝗛𝗔𝗡𝗭𝗘𝗘𝗥](https://t.me/mhd_thanzeer)**/n🌈𝐇𝐢𝐭 𝐌𝐞 **/help** 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐏𝐨𝐰𝐞𝐫 🌈"
HELP = """🏷️ **Need Help?** 🤔
Onwer : @mhd_thanzeer

🏷️ **Common Commands**:
\u2022 `/play` reply to an audio to play or queue it
\u2022 `/help` shows help for commands
\u2022 `/playlist` shows the playlist
\u2022 `/current` shows playing time of current track
\u2022 `/song` [song name] download the song as audio

🏷️ **Admin Commands**:
\u2022 `/skip` [n] skip current or n where n >= 2
\u2022 `/join` join voice chat of current group
\u2022 `/leave` leave current voice chat
\u2022 `/vc` check which VC is joined
\u2022 `/stop` stop playing music
\u2022 `/radio` start radio stream
\u2022 `/stopradio` stop radio stream
\u2022 `/replay` play from the beginning
\u2022 `/clean` remove unused RAW PCM files
\u2022 `/pause` pause playing music
\u2022 `/resume` resume playing music
\u2022 `/mute` mute the VC userbot
\u2022 `/unmute` unmute the VC userbot
\u2022 `/restart` restart the bot

🏷️ **Developer: [𝗠𝗛𝗗_𝗧𝗛𝗔𝗡𝗭𝗘𝗘𝗥](https://t.me/mhd_thanzeer)** 👑
"""


@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('🤑 𝐌𝐎𝐕𝐈𝐄𝐒 𝐆𝐑𝐎𝐔𝐏 🤑', url='https://t.me/wolfpackmedia'),
        ],
        [

        InlineKeyboardButton('🤘 𝐒𝐄𝐑𝐈𝐄𝐒 𝐆𝐑𝐎𝐔𝐏 🤘', url='https://t.me/wolfpackseries'),

        ],

    
        
        
    [
        InlineKeyboardButton('⚙️ HELP ⚙️', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
