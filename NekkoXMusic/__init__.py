from NekkoXMusic.core.bot import Anony
from NekkoXMusic.core.dir import dirr
from NekkoXMusic.core.git import git
from NekkoXMusic.core.userbot import Userbot
from NekkoXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
