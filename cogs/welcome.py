import discord
from discord.ext import commands


class Welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcomemessage_channel = self.bot.get_channel(1219308439927263272)

        embed = discord.Embed(description=f"Naa {member.display_name}, wir wünschen dir viel Spaß auf unserem Server. "
                                          f"Du bist der {len(member.guild.members)}. User auf unserem Server!",
                              color=discord.Color.from_rgb(170, 0, 0))
        embed.set_author(name=f"Herzlich Willkommen auf {member.guild}!",
                         icon_url="https://images-ext-1.discordapp.net/external/2wsdPOmGiXxbzIv"
                                  "-zD0L0zHb5khkAam88idINjlXC0A/https/cdn-longterm.mee6.xyz/plugins/welcome/images"
                                  "/1112299603082100826"
                                  "/c0198bcda90dbb5805c4b5a801fb5858f1154c8da96b69c5a16bd5fb964de02d.png")
        embed.add_field(name="<:FernLurk:1220307142263832656> Was dich hier erwartet: ",
                        value="<:pfeil:1219584472534618112> Nitro Giveaways und Events in <#1219549261688078396>. \n"
                              "<:pfeil:1219584472534618112> Viele Minigames in <#1227502433882607686>. \n"
                              "<:pfeil:1219584472534618112> Eine aktive Community! <#1219308439927263272>.")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"User ID: {member.id} | By Kiyo ッ | https://discord.gg/c7JnVjHr9g",
                         icon_url="https://cdn.discordapp.com/attachments/1111005524591398983/1260580712113897503"
                                  "/Screenshot_2024-07-10_091341.png?ex=668fd6c6&is=668e8546&hm"
                                  "=d077dc0a13c923367c3ba39e4d7f3ef2e86f62a9964d5e7aa9dfd281db7e0846&")


        if member.guild.id == 1219308282016174212:
            await welcomemessage_channel.send(member.mention, embed=embed)


def setup(bot):
    bot.add_cog(Welcomer(bot))
