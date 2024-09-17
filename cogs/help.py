import json
import os

import discord
from discord import ComponentInteraction
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.slash_command(name='help', description='Rufe Yun Jin zu Hilfe!')
    async def help_command(self, ctx):
        embed = discord.Embed(title=f'Yun Jin ッ Hilfe <:GabiLETSGO:1232317332060373132>',
                              description="Hier findest du Hilfe zu den Befehlen von unserem privaten Bot Yun Jin! "
                                          "<:StarkClueless:1220266338736537642>"
                                          "\n<:Platzhalter:1262407815750877267>",
                              color=discord.Color.from_rgb(155, 66, 245))
        embed.add_field(name="> Speziell für Ayakas Gruft designed! <a:happyCat:1219565785530503258>",
                        value="Alle meine Befehle wurde speziell für diesen Server erstellt und können nur dort "
                              "verwendet werden!",
                        inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1111005524591398983/1285589251928494202"
                            "/yunjinhilfe.png?ex=66ead1ca&is=66e9804a&hm"
                            "=e291f9a7b4f9cb6e22d4ff1346037c7704b03523f0a011bcc28ac4f5e4332617&")
        embed.set_footer(text="Ayakas Gruft ♡ https://discord.gg/vPJ8Jsv7",
                         icon_url="https://cdn.discordapp.com/attachments/1111005524591398983/1285149342872633407"
                                  "/0c330bf689777f2437ecc889a7154929_1.gif?ex=66e93818&is=66e7e698&hm"
                                  "=d05fb87af87c813c4e5b5f9614a697c429b779515c498bd2ade057afacf73710&")

        await ctx.respond(embed=embed, hidden=False, components=[
            discord.SelectMenu(placeholder="Wähle eine Kategorie aus.",
                               custom_id="help-selection",
                               max_values=1,
                               options=[
                                   discord.SelectOption(label="Informationen",
                                                        description="Befehle die Informationen über den Bot oder User "
                                                                    "ausgeben.",
                                                        emoji="<:bunnyLurk:1219565898055159899>",
                                                        value="informationen"),
                               ])
        ])

    @commands.Cog.on_select(custom_id="help-selection")
    async def help_selection(self, ctx: ComponentInteraction, _):
        global embed
        selected_text = ctx.data.values

        if selected_text[0] == "informationen":
            embed = discord.Embed(title="Informationen <:StarkPoint:1220266411440472114>",
                                  description="Hier sind alle Befehle die Informationen über den Bot oder User "
                                              "ausgeben aufgelistet.\n\n"
                                              "`/userinfo [user]` ~ Gibt verschiedene Informationen über den User in "
                                              "einem Embed zurück.\n"
                                              "<:Platzhalter:1262407815750877267>",
                                  color=discord.Color.from_rgb(155, 66, 245))
            embed.set_footer(text="Ayakas Gruft ♡ https://discord.gg/vPJ8Jsv7",
                             icon_url="https://cdn.discordapp.com/attachments/1111005524591398983/1285149342872633407"
                                      "/0c330bf689777f2437ecc889a7154929_1.gif?ex=66e93818&is=66e7e698&hm"
                                      "=d05fb87af87c813c4e5b5f9614a697c429b779515c498bd2ade057afacf73710&")

        await ctx.respond(embed=embed, hidden=True)


def setup(bot):
    bot.add_cog(HelpCommand(bot))
