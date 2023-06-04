import random
import logging

import discord

from secret_info import DISCORD_APY_KEY, BOT_ANSWER_MAPPING


logger = logging.getLogger("discord.j")


class MyClient(discord.Client):
    async def on_ready(self):
        logger.info(f'Logged on as: {str(self.user)}')

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        logger.info(message.content)

        if message.content in BOT_ANSWER_MAPPING:
            await message.channel.send(BOT_ANSWER_MAPPING[message.content])
        else:
            await message.channel.send('asking master meaning of the word')


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(DISCORD_APY_KEY)
