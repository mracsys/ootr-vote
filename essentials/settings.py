import discord

from essentials.secrets import SECRETS


class Settings:
    def __init__(self):
        self.color = discord.Colour(int('7289da', 16))
        self.title_icon = "https://i.imgur.com/UzQSrg6.png" #PM
        self.author_icon = "https://i.imgur.com/j2oKAtd.png" #tag
        self.report_icon = "https://i.imgur.com/UzQSrg6.png" #report
        self.owner_id = 351917416596373506
        self.msg_errors = False
        self.log_errors = True
        self.invite_link = \
            'https://discordapp.com/api/oauth2/authorize?client_id=688363641271091229&permissions=8&scope=bot'

        self.load_secrets()

    def load_secrets(self):
        # secret
        self.dbl_token = SECRETS.dbl_token
        self.mongo_db = SECRETS.mongo_db
        self.bot_token = SECRETS.bot_token
        self.mode = SECRETS.mode


SETTINGS = Settings()
