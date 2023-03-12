import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('WATCHER_TOKEN')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message_edit(before, after):
    if before.author == client.user:
        return
    
    await before.channel.send(f'I see all in the universe. `{before.author.display_name}` originally said `{before.content}`, not `{after.content}`!')

@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return
    
    await message.channel.send(f'I see all in the universe. `{message.author.display_name}` said `{message.content}`, before deleting!')

client.run(TOKEN)