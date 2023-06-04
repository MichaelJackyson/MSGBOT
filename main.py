import random
import logging

import discord

from secret_info import DISCORD_APY_KEY


logger = logging.getLogger("discord.j")


messages = ["hello", "abc", "999999999999"]

class MyClient(discord.Client):
    async def on_ready(self):
        logger.info(f'Logged on as: {str(self.user)}')

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        logger.info(message.content)

        if message.content == 'ping':
            await message.channel.send('pong')
        elif message.content == "hi":
            await message.channel.send(random.choice(messages))
        elif message.content == "deez":
            await message.channel.send('nuts')
        elif message.content == "who is your mom":
            await message.channel.send(' not u')
        elif message.content == "lol":
            await message.channel.send('whats so funny?')
        elif message.content == "lmao":
            await message.channel.send('uhhhhhh okay tell me whats too funny?')
        elif message.content == "bye":
            await message.channel.send('im glad u are out of my face')
        elif message.content == "best football team?":
            await message.channel.send('MAN CITY and Bayern tied')
        elif message.content == "best international football team?":
            await message.channel.send('GERMANY')
        elif message.content == "best trio of all time(in soccer)":
            await message.channel.send('Ronaldo, Bale, Benzema or Neymar, Suarez Messi (TIED)')
        elif message.content == "who wrote this bot?":
            await message.channel.send('OpenAI 2.0')
        elif message.content == "cap":
            await message.channel.send('your mom is cap')
        elif message.content == "no u":
            await message.channel.send('*gets destroyed by 3 letters and 1 space*')
        elif message.content == "best instrument":
            await message.channel.send('the saxophone')
        elif message.content == "bestify quiz for allison c?":
            await message.channel.send('its here : https://bestiefy.com/q?=SqYur')
        elif message.content == "bestify quiz for bread?":
            await message.channel.send('idk ask him urself')
        elif message.content == "bestify quiz for aaron h?":
            await message.channel.send('https://bestiefy.com/q?=fjmd5')
        elif message.content == "balls":
            await message.channel.send('deez nuts')
        elif message.content == "thx":
            await message.channel.send('np')
        elif message.content == "bruh":
            await message.channel.send('https://tenor.com/view/facepalm-really-stressed-mad-angry-gif-16109475')
        elif message.content == "thanks":
            await message.channel.send('no problem')
        elif message.content == "ur mom":
            await message.channel.send('i dont have a mom')
        elif message.content == "shut up":
            await message.channel.send('no u x 3')
        elif message.content == "thats sus":
            await message.channel.send('your mom is sus')
        elif message.content == "if ur dumb, ur dumb":
            await message.channel.send('ur also dumb')
        else:
            await message.channel.send('asking master meaning of the word ')


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(DISCORD_APY_KEY)
