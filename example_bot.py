# This example requires the 'message_content' intent.
import os
from dotenv import load_dotenv

load_dotenv()

discord_token = os.getenv('TOKEN')
import discord
import os
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$MURALI'):
        await message.channel.send('tu chutiya hai re saale')

client.run(discord_token)
