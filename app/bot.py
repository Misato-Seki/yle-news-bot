import discord
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_summary_message():
    await client.wait_until_ready()

    channel = client.get_channel(CHANNEL_ID)
    if channel:
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1))
        await channel.send(f"Here is the summary of YLE news for {yesterday.strftime('%m/%d')}: https://misato-seki.github.io/yle-news-bot/{yesterday.strftime('%Y-%m-%d')}.html")
    await client.close()