#
# Copyright (C) 2021-2022 by TeamStar@Github, < https://github.com/DaRrKNneSs_1 >.
#
# This file is part of < https://github.com/DaRrkNneSs1/STAR_MUSIC > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DaRrkNneSs1/STAR_MUSIC/blob/master/LICENSE >
#
# All rights reserved.

from StarMusic.core.bot import StarBot
from StarMusic.core.dir import dirr
from StarMusic.core.git import git
from StarMusic.core.userbot import Userbot
from StarMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = StarBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
