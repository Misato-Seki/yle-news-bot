import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_summary_message(summary_message):
    await client.wait_until_ready()

    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(summary_message)
    await client.close()


def format_summary(article, summary):
    return (
        f"**Title:** {article['title']}\n"
        f"**URL:** {article['url']}\n"
        f"**Date:** {article['date']}\n"
        f"**Summary:** {summary}\n"
        f"\n"
    )