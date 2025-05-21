import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_summary_message():
    await client.wait_until_ready()

    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Here is the latest summary of YLE news articles: http://localhost:5001/")
        # for message in summary_message:
        #     # Send each message in the list
        #     await channel.send(message)
    await client.close()


# def format_summary(articles):
#     MAX_LENGTH = 2000
#     messages = []
#     current_message = ""

#     for article in articles:
#         entry = (
#             f"**Title:** {article['title']}\n"
#             f"**URL:** {article['url']}\n"
#             f"**Date:** {article['date']}\n"
#             f"**Summary:** {article['summary']}\n\n"
#         )

#         # Check if adding this entry would exceed the max length
#         if len(current_message) + len(entry) > MAX_LENGTH: # if exceeding max length
#             # Append the current message to the list and start a new one
#             messages.append(current_message)
#             current_message = entry
#         else: # if NOT exceeding max length
#             # Add the entry to the current message
#             current_message += entry

#     # Add the last message if it exists
#     if current_message:
#         messages.append(current_message)

#     return messages

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(client.start(TOKEN)) # Start the bot using asyncio

    # async def run_bot():
    #     """
    #     Logins to Discord and connects to the gateway, then runs the bot until stopped.
    #     """
    #     await client.login(TOKEN)
    #     await client.connect()
    #     await send_summary_message()

    # asyncio.run(run_bot()) # Run the bot using asyncio