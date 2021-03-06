from discord.ext import commands


def setup(bot):
    bot.add_cog(Move(bot))


class Move:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['mv'])
    async def move(self, ctx, *, move):
        player = self.bot.lavalink.players.get(ctx.guild.id)

        moves = move.split(' ')

        global move_song, move_to

        try:
            move_song = int(moves[0])
            move_to = int(moves[1])
        except ValueError:
            return await ctx.send('🚫 Please specify two valid positions!')

        if move_song > len(player.queue) or move_song < 1:
            return await ctx.send(f'🚫 {move_song} is not a valid!')

        if move_to > len(player.queue) or move_to < 1:
            return await ctx.send(f'🚫 {move_to} is not a valid!')

        song = player.queue[move_song - 1]
        del player.queue[move_song - 1]
        player.queue.insert((move_to - 1), song)

        await ctx.send(f'✅ Successfully moved **{song.title}** '
                       f'from position **`{move_song}`** to position **`{move_to}`**')
