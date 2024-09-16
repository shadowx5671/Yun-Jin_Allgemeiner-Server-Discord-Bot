import json
import logging
import os
import random
import discord
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

log = logging.getLogger('BOT-MAIN')

# Replace with the channel ID
CHANNEL_ID = 123456789012345678

bot = commands.Bot(
    command_prefix='!j!',
    intents=discord.Intents.all(),
    activity=discord.Activity(type=discord.ActivityType.streaming, name="I'm back! Starting...",
                              url="https://www.twitch.tv/jellyshadow50"),
    sync_commands=True,
    delete_not_existing_commands=True,
)


@bot.event
async def on_ready():
    # Waiting until the bot is ready
    await bot.wait_until_ready()
    # Starting the loop
    change_activity.start()


@tasks.loop(seconds=15)
async def change_activity():
    global randomStatus

    game = iter(
        [
            "discord.py v2.4 | Python v3.12",
            "/help | V0.1.3 Beta",
            "Ayakas privater Bot!",
        ]
    )  # Every line above ^^ is one new status the bot can have
    for randomStatus in range(random.randint(1, 3)):
        randomStatus = next(game)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=randomStatus,
                                                        url="https://www.twitch.tv/jellyshadow50"))


@bot.event
async def on_guild_join(guild):

    try:
        with open("./data/servers.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    server_id = guild.id

    # Access or update user data based on server and user IDs
    if str(server_id) not in data:
        data[str(server_id)] = {"level-system": False,
                                "level-nickname": False,
                                "server-invite": f'{(await guild.create_invite()).url}'}

    with open("./data/servers.json", "w") as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    log.info('Starting bot...')

    cogs = [file.stem for file in Path('cogs').glob('**/*.py') if not file.name.startswith('__')]
    log.info(f'Loading {len(cogs)} cogs...')

    for cog in cogs:
        bot.load_extension(f'cogs.{cog}')
        log.info(f'Loaded cog {cog}')

    token = os.getenv('TEST_BOT_TOKEN')
    bot.run(token)
