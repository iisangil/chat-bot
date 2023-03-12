import os
import openai
import time

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('CHATTER_TOKEN')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

openai.api_key = os.getenv('OPENAI_API_KEY')

userDict = {}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!gary help':
        helpMessage = 'Hello! I am Gary Poppy Terbuson 3.5.\n I am a Discord bot that allows users to easily create and message AI assistants.'
        helpMessage += '\n\nUsage:\n\n`!gary help` -- return this help message\n`!gary create <name>` -- create a new AI assistant named `<name>`\n`!gary message <name> <message>` -- send a message to the AI assistant named `<name>`'

        await message.channel.send(helpMessage)

    if message.content == '!gary create':
        user = message.author

    if message.content.startswith('!gary'):
        messageContent = message.content[6:]

client.run(TOKEN)