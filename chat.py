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

messages = []
timeDict = {}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!stove'):
        log = {
            'role': 'user',
            'content': message.content[7:]
        }
        messages.append(log)
        
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            max_tokens=2048
        )
        print('response', response)
        messageResponse = {
            'role': 'assistant',
            'content': response.choices[0].message.content
        }
        messages.append(messageResponse)

        await message.channel.send(response.choices[0].message.content)


client.run(TOKEN)