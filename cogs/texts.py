import discord
from discord.ext import commands


class Texts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rules(self, ctx, user: discord.Member = None):
        user = user or ctx.author

        embed = discord.Embed(title="Unsere Regeln <:spongebobCry:1219565688935415808>",
                              description="Hier findest du die Regeln unseres Servers. Diese können jederzeit geändert "
                                          "werden.",
                              color=discord.Color.from_rgb(155, 66, 245))
        embed.add_field(name="<:pfeil:1219584472534618112> 1.) Sei höflich <:rose:1219591329106104408>",
                        inline=False,
                        value="Verhalte dich immer respektvoll und höflich gegenüber anderen! Diskriminierung, "
                              "Provokation, Hass-Reden und auch beleidigende Scherze, die auf (spezielle) "
                              "Behinderungen, Geschlecht, Herkunft oder auch Religion abzielen, sind strengstens "
                              "untersagt.")
        embed.add_field(name="<:pfeil:1219584472534618112> 2.) Verbreite keinen Spam <:cooljoe:1219565568747896842>",
                        inline=False,
                        value="Das ständige Benutzen von Caps und Spam ist verboten.")
        embed.add_field(name="<:pfeil:1219584472534618112> 3.) Keine Werbung <:konataCry:1219565423847149610>",
                        inline=False,
                        value="Werbung für dich zu betreiben ist strengstens untersagt. "
                              "Frage vorher stehts nach Erlaubnis!")
        embed.add_field(name="<:pfeil:1219584472534618112> 4.) Person Bezogene Daten <:meltyPeek:1219591764604747838>",
                        inline=False,
                        value="Das Teilen von personenbezogenen Daten ist ohne Zustimmung verboten.")
        embed.add_field(name="<:pfeil:1219584472534618112> 5.) NSFW <:BertTheFck:1219565525257027584>",
                        inline=False,
                        value="NSFW-Inhalte (Pornographie etc.) sind in allen Channeln verboten.")
        embed.add_field(name="<:pfeil:1219584472534618112> 6.) Pings <:sataniaPing:1219591895097933854>",
                        inline=False,
                        value="Das grundlose taggen / pingen / markieren von Nutzern & Benutzerrängen ist nicht "
                              "erlaubt.")
        embed.set_footer(text="Ayakas Gruft ♡ https://discord.gg/vPJ8Jsv7",
                         icon_url="https://cdn.discordapp.com/attachments/1111005524591398983/1285149342872633407"
                                  "/0c330bf689777f2437ecc889a7154929_1.gif?ex=66e93818&is=66e7e698&hm"
                                  "=d05fb87af87c813c4e5b5f9614a697c429b779515c498bd2ade057afacf73710&")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1111005524591398983/1285151775497916446/regeln"
                            ".jpg?ex=66e93a5c&is=66e7e8dc&hm"
                            "=d485129aba2fd22b1dfa9ab44568252fc886fa687ebca8c3b5767630a8f1dd20&")
        if user.id == 1051738247048478741:
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def serveroverview(self, ctx, user: discord.Member = None):
        user = user or ctx.author

        embed = discord.Embed(title="Server Overview <:bunnyHearts:1219565509968662559>",
                              description="Heyy, Willkommen in der Ayaka Gruft! Wir sind eine Genshin/Anime Community "
                                          "mit vielen aktiven Membern! In diesen Channel findest du weitere "
                                          "Informationen um dich optimal auf dem Server zurechtzufinden. Wir freuen "
                                          "uns auf dich! \n\n> **Besonderheiten:** <:bunnyLurk:1219565898055159899>",
                              color=discord.Color.from_rgb(155, 66, 245))
        embed.add_field(name="<:pfeil:1219584472534618112> Selfroles",
                        inline=False,
                        value="Auf unserem Server sind die Self Roles direkt oben in der Ansicht <id:customize>.")
        embed.add_field(name="<:pfeil:1219584472534618112> Informationen",
                        inline=False,
                        value="Alle Informationen über den Server wie die **Level Road** oder die **Booster Vorteile** "
                              "findest du bei uns im <id:guide>.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1111005524591398983/1260842936116051998/trennlinie"
                            ".png?ex=6690cafd&is=668f797d&hm"
                            "=ef843f6d04504cc0243fe841c0eb0061e07a9e1013119c7bad04f7e747c35a67&")
        embed2 = discord.Embed(description="> **Unsere Teammitglieder:** <:bunnyBlush:1219565486526828595>",
                               color=discord.Color.from_rgb(155, 66, 245))
        embed2.add_field(name="<:pfeil:1219584472534618112> ✧ 𝑂𝑤𝑛𝑒𝑟",
                        inline=False,
                        value="<@1051738247048478741>")
        embed2.add_field(name="<:pfeil:1219584472534618112> ✩ 𝐴𝑑𝑚𝑖𝑛",
                        inline=False,
                        value="<@832576034578104382>")
        embed2.add_field(name="<:pfeil:1219584472534618112> ✩ 𝑀𝑜𝑑𝑒𝑟𝑎𝑡𝑜𝑟",
                        inline=False,
                        value="<@1075466161703096361>")
        embed2.add_field(name="<:pfeil:1219584472534618112> ✩ 𝑆𝑢𝑝𝑝𝑜𝑟𝑡𝑒𝑟",
                        inline=False,
                        value="<@1112321336832966656>")
        embed2.add_field(name="<:pfeil:1219584472534618112> ✩ 𝑇-𝑆𝑢𝑝𝑝𝑜𝑟𝑡𝑒𝑟",
                        inline=False,
                        value="<@934816757166768149>")

        embed2.set_footer(text="Ayakas Gruft ♡ https://discord.gg/vPJ8Jsv7",
                         icon_url="https://cdn.discordapp.com/attachments/1111005524591398983/1285149342872633407"
                                  "/0c330bf689777f2437ecc889a7154929_1.gif?ex=66e93818&is=66e7e698&hm"
                                  "=d05fb87af87c813c4e5b5f9614a697c429b779515c498bd2ade057afacf73710&")
        embed2.set_image(url="https://cdn.discordapp.com/attachments/1111005524591398983/1285546684813807647"
                             "/server_overview.jpg?ex=66eaaa25&is=66e958a5&hm"
                             "=58562273693c89f20730f57e0dddaba8aeb890243fadf081e95b65bd7189cb1b&")
        if user.id == 1051738247048478741:
            await ctx.channel.send(embed=embed)
            await ctx.channel.send(embed=embed2)

    @commands.command()
    async def boosterperks(self, ctx, user: discord.Member = None):
        user = user or ctx.author

        embed = discord.Embed(title="Nitro Server Boosting <a:hello_kitty_dance:1234576822658662410>",
                              description="Werde Server Booster von unserem Server und profitiere von Vorteilen! "
                                          " <:bearHearts:1219566206340825138>"
                                          "\n<:Platzhalter:1262407815750877267>",
                              color=discord.Color.from_rgb(155, 66, 245))
        embed.add_field(name="> Booster Vorteile: <:mitsuLove:1225714799938113566>",
                        value="\n<:Platzhalter:1262407815750877267>"
                              "\n<:pfeil:1219584472534618112> Die <@&1219348405147406376> Rolle direkt unter unserem "
                              "Serverteam!"
                              "\n<:pfeil:1219584472534618112> Very Important Speaker in Talks!"
                              "\n<:pfeil:1219584472534618112> Medien, Links und Gifs Rechte auch im Hauptchat!"
                              "\n<:pfeil:1219584472534618112> Wir fügen drei Emoji deiner Wahl hinzu!"
                              "\n<:pfeil:1219584472534618112> Du bekommst deine eigene Rolle! Farbe und Emoji frei "
                              "wählbar!"
                              "\n<:pfeil:1219584472534618112> Wir designen einen eigenen Banner für dich!"
                              "\n<:pfeil:1219584472534618112> Ein großes Dankeschön von unserem Serverteam! "
                              "<:justMe:1222964543865618503>",
                        inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1111005524591398983/1285565042850533458"
                            "/boosterperks.jpg?ex=66eabb3e&is=66e969be&hm"
                            "=52fc9fa36efed48b58a0b4ab2c4b4749422625f5a0dc2057e876554291cb0473&")
        embed.set_footer(text="Ayakas Gruft ♡ https://discord.gg/vPJ8Jsv7",
                         icon_url="https://cdn.discordapp.com/attachments/1111005524591398983/1285149342872633407"
                                  "/0c330bf689777f2437ecc889a7154929_1.gif?ex=66e93818&is=66e7e698&hm"
                                  "=d05fb87af87c813c4e5b5f9614a697c429b779515c498bd2ade057afacf73710&")
        if user.id == 1051738247048478741:
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def levelroad(self, ctx, user: discord.Member = None):
        user = user or ctx.author

        embed = discord.Embed(title="Level Road <:bunnyLurk:1219565898055159899>",
                              description="Sobald du auf unserem Server eine bestimmte Level Stufe erreichst bekommst "
                                          "du verschiedene Vorteile! Hier sind alle aufgelistet:"
                                          "\n<:Platzhalter:1262407815750877267>",
                              color=discord.Color.from_rgb(155, 66, 245))
        embed.add_field(name="> Level Road:",
                        value="\n<:Platzhalter:1262407815750877267>"
                              "\n<:pfeil:1219584472534618112> Very Important Speaker in Talks (ab <@&1227176723045548042>)"
                              "\n<:pfeil:1219584472534618112> Medien, Links und Gifs Rechte in allen Chats "
                              "(ab <@&1227176774765641798>)"
                              "\n<:pfeil:1219584472534618112> Wir fügen drei Emoji deiner Wahl hinzu (ab "
                              "<@&1227177304296263711>)"
                              "\n<:pfeil:1219584472534618112> Beantrage deine eigene Rolle! Farbe und Emoji könnt ihr "
                              "entscheiden! (ab <@&1227177399343513692>)"
                              "\n<:pfeil:1219584472534618112> Wir designen einen eigenen Banner für dich! (ab "
                              "<@&1283880515887304754>)"
                              "\n<:pfeil:1219584472534618112> Du bekommst einen Monat Nitro Basic geschenkt! (ab "
                              "<@&1283881989312745472>)"
                              "\n<:Platzhalter:1262407815750877267>",
                        inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1111005524591398983/1285537252306456627"
                            "/level_road.jpg?ex=66eaa15d&is=66e94fdd&hm"
                            "=c46e93874782c0143437abad7cea7a37f441b4a072e0364bb7c51c656d894354&")
        embed.set_footer(text="Ayakas Gruft ♡ https://discord.gg/vPJ8Jsv7",
                         icon_url="https://cdn.discordapp.com/attachments/1111005524591398983/1285149342872633407"
                                  "/0c330bf689777f2437ecc889a7154929_1.gif?ex=66e93818&is=66e7e698&hm"
                                  "=d05fb87af87c813c4e5b5f9614a697c429b779515c498bd2ade057afacf73710&")
        if user.id == 1051738247048478741:
            await ctx.channel.send(embed=embed)



def setup(bot):
    bot.add_cog(Texts(bot))