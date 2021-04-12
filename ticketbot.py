import api
import discord
import json
import time
from discord.ext.commands import Bot
import asyncio
from discord.ext import commands
import random
from discord.utils import get
import random
import string


bot = commands.Bot(command_prefix='/', case_insensitive=True)
bot.remove_command('help')

def randomDigits():
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(10))

@bot.event
async def on_ready():
    activity = discord.Game(name="Tickets")
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print('-' * 30)
    print('Logged in as: ')
    print(bot.user)
    print('-' * 30)
    channel = bot.get_channel(784901893121769503)
    embed=discord.Embed(title=f"Create a purchase ticket", color=0x021ff7)
    embed.add_field(name="**Ticket creations**", value=f"React to this message to open a purchase ticket", inline=False)
    msg = await channel.send(embed=embed)
    await msg.add_reaction('💰')
    await asyncio.sleep(2)
    while True:
        reaction, reactor = await bot.wait_for('reaction_add')
        if str(reaction.emoji) == '💰':
            buyer = reactor
            await msg.remove_reaction('💰', buyer)
            guild = bot.get_guild(784901809604264016)
            await asyncio.sleep(1.5)
            adminRole = get(guild.roles, name="Admin")
            everyoneRole = get(guild.roles, name="@everyone")
            memberRole = get(guild.roles, name="Member")
            buyerRole = get(guild.roles, name="Buyer")

            overwrites = {
                everyoneRole: discord.PermissionOverwrite(read_messages=False),
                memberRole: discord.PermissionOverwrite(read_messages=False),
                buyerRole: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True),
                adminRole: discord.PermissionOverwrite(read_messages=True),
                ecBot: discord.PermissionOverwrite(read_messages=True),
                reactor: discord.PermissionOverwrite(read_messages=True)
            }
            digits = randomDigits()
            buyerChannel = f'{digits}'
            channell = await guild.create_text_channel(buyerChannel, overwrites=overwrites)
            newChannel = bot.get_channel(int(channell.id))
            await newChannel.send('Please wait for a admin')


@bot.command()
async def done(ctx):

    await ctx.channel.delete()


bot.run(TOKEN)
