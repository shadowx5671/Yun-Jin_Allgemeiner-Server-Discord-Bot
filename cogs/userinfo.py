import discord
from discord.ext import commands


class UserInfoCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.slash_command(name='userinfo', description='Zeigt Informationen über einen Nutzer des Servers an.')
    async def userinfo_command(self, ctx, user: discord.Member = None):
        user = user or ctx.author

        roles = [role.mention for role in user.roles if role != user.guild.default_role]
        roles_string = ', '.join(roles) if roles else 'None'

        if user.guild_permissions.administrator:
            adminrights = "Ja"
        else:
            adminrights = "Nein"

        embed = discord.Embed(title=f'User Info - {user.display_name} ({user.name})',
                              color=discord.Color.from_rgb(155, 66, 245))
        embed.set_thumbnail(url=user.display_avatar_url)
        embed.add_field(name='ID <:StarkClueless:1220266338736537642>', inline=False, value=user.id)
        embed.add_field(name='Username <:maomaoproud:1226606732806066297>', inline=False, value=user)
        embed.add_field(name='Account erstellt <:StarkPoint:1220266411440472114>', inline=False,
                        value=discord.utils.styled_timestamp(user.created_at, style=discord.TimestampStyle.relative))
        embed.add_field(name='Server beigetreten <:cooljoe:1219565568747896842>', inline=False,
                        value=discord.utils.styled_timestamp(user.joined_at, style=discord.TimestampStyle.relative))
        embed.add_field(name='Server Rollen <:carzyicarus:1219565239599890452>', inline=False, value=roles_string)
        embed.add_field(name='Admin Rechte <:GabiLETSGO:1232317332060373132>', inline=False, value=adminrights)
        embed.add_field(name='Level <:NezuHappy:1225714729335656508>', value='Soon')
        embed.set_footer(text=f"Requested by {ctx.author} ♡ Ayakas Gruft ♡ https://discord.gg/vPJ8Jsv7",
                         icon_url="https://cdn.discordapp.com/attachments/1111005524591398983/1285149342872633407"
                                  "/0c330bf689777f2437ecc889a7154929_1.gif?ex=66e93818&is=66e7e698&hm"
                                  "=d05fb87af87c813c4e5b5f9614a697c429b779515c498bd2ade057afacf73710&")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1111005524591398983/1285605148525072445/userinfo"
                            ".png?ex=66eae098&is=66e98f18&hm=6daae7037db5e180394781cb11feceb4b13daaf9695b9100bb3038b92c239ba3&")
        await ctx.respond(embed=embed, hidden=False)


def setup(bot):
    bot.add_cog(UserInfoCommand(bot))
