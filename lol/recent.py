import sys
sys.path.append("..")
import main

@main.bot.command()
async def lol(ctx, arg):
    await ctx.send(f'Command input received: {arg}')
    if(arg == 'recent'):
        await ctx.send(f'Finding recent match history...')