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

messages = [
    {
        'role': 'system',
        'content': 'Act as Stove Rojers, a discord chatbot.',
    },
    {
        'role': 'user',
        'content': 'Do you know where the capital of the USA is?'
    },
    {
        'role': 'assistant',
        'content': 'It is Washington, DC.'
    },
        {
        'role': 'system',
        'content': 'Respond only in first person.',
    },
        {
        'role': 'system',
        'content': 'Never break character.',
    },
]
timeDict = {}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord! 5')

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens=1024
    )
    print('response', response)

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
            max_tokens=1024
        )
        print('response', response)
        await message.channel.send(response.choices[0].message.content)

        # time delay functionality below
        # print(message.author.name, message.author.discriminator)
        # key = message.author.name + message.author.discriminator
        # if message.author.name + message.author.discriminator not in timeDict:
        #     timeDict[]

client.run(TOKEN)