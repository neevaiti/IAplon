import discord
from discord.ext import commands

class AnnoucementCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_role(['Formateur', 'Administration'])
    async def annonce(self, ctx, role: discord.Role, *, message):
        """Announce a message to a role"""
        if role is None:
            await ctx.send("Le rôle mentionné n'existe pas.")
            return
        for member in ctx.guild.members:
            if role in member.roles:
                try:
                    await member.send(message)
                except:
                    pass 
        await ctx.send(f"Message envoyé à tous les membres ayant le rôle {role.name}.")

def setup(bot):
    bot.add_cog(AnnoucementCog(bot))
