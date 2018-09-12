from discord.ext import commands


def setup(bot):
    bot.add_cog(Loop(bot))


class Loop:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['lp'])
    async def loop(self, ctx):
        player = self.bot.lavalink.players.get(ctx.guild.id)

        player.repeat = not player.repeat

        await ctx.send('🔂 | Loop ' + ('enabled' if player.repeat else 'disabled'))
