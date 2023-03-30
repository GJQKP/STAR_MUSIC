#
# Copyright (C) 2021-2022 by TeamStar@Github, < https://github.com/DaRrKNneSs_1 >.
#
# This file is part of < https://github.com/DaRrkNneSs1/STAR_MUSIC > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DaRrkNneSs1/STAR_MUSIC/blob/master/LICENSE >
#
# All rights reserved.

import sys

from pyrogram import Client
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class StarBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot")
        super().__init__(
            "StarMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "Bot Started"
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()
        if config.SET_CMDS == str(True):
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("ping", "Check that bot is alive or dead"),
                        BotCommand("تشغيل", "يبدأ تشغيل الأغنية المطلوبة"),
                        BotCommand("تخطي", "ينتقل إلى المسار التالي في قائمة الانتظار"),
                        BotCommand("ايقاف", "إيقاف الأغنية الحالية قيد التشغيل مؤقتًا"),
                        BotCommand("استمر", "لإستمرار تشغيل الاغنيه"),
                        BotCommand("انهاء", "انهاء ومغادرة المحادثة الصوتيه"),
                        BotCommand("خلط", "Randomly shuffles the queued playlist."),
                        BotCommand("مود التشغيل", "ترتيب عشوائي لقائمة التشغيل في قائمة الانتظار"),
                        BotCommand("الاعدادات", "افتح إعدادات روبوت الموسيقى للدردشة.")
                        ]
                    )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "Please promote Bot as Admin in Logger Group"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"< Started as {self.name}")
