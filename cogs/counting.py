import asyncio
import json
import os
import discord
from discord.ext import commands


class Counting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 1285613986955395082:
            # Load the stored data from a JSON file
            try:
                with open("./data/counting_data.json", "r") as f:
                    data = json.load(f)
                    lastuser = data.get("LAST_USER", None)
                    number = data.get("NUMBER", "1")
            except FileNotFoundError:
                lastuser = 0
                number = "1"

            if message.author.bot:
                if message.author.id != 1056581712500494467:
                    await message.delete()
                return

            if not message.content.isdigit():
                embed = discord.Embed(
                    title="Dies ist keine Nummer! <:FernAnnoyed:1220264866791690240>",
                    description="Dieser Kanal ist nicht zum Chatten gedacht.",
                    color=discord.Color.from_rgb(155, 66, 245)
                )
                await message.channel.send(f"<@{message.author.id}>", embed=embed, delete_after=5)
                await message.delete()
                return

            if message.author.id == int(lastuser):
                embed = discord.Embed(
                    title="Du kannst nicht zweimal hintereinander zählen! <:FernAnnoyed:1220264866791690240>",
                    description="Nutzer müssen nacheinander zählen. Als nächstes ist jemand anderes dran.",
                    color=discord.Color.from_rgb(155, 66, 245)
                )
                await message.channel.send(f"<@{message.author.id}>", embed=embed, delete_after=5)
                await message.delete()
                return

            if message.content != number:
                embed = discord.Embed(
                    title="Diese Nummer stimmt nicht! <:FernAnnoyed:1220264866791690240>",
                    description=f"Die nächste Nummer ist: {(int(number)+1)}.",
                    color=discord.Color.from_rgb(155, 66, 245)
                )
                await message.channel.send(f"<@{message.author.id}>", embed=embed, delete_after=5)
                await message.delete()
                return

            await message.add_reaction("✅")
            await asyncio.sleep(5)
            await message.remove_reaction("✅", self.bot.user)

            # Save the updated data to the JSON file
            data = {
                "LAST_USER": str(message.author.id),
                "NUMBER": str(int(number) + 1)
            }
            with open("./data/counting_data.json", "w") as f:
                json.dump(data, f)

def setup(client):
    client.add_cog(Counting(client))
