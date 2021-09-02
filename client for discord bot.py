import datetime
from logging import error
import discord
import asyncio
import random
from discord import Embed
from discord import role
from discord.client import _ClientEventTask
from discord.ext import commands
from asyncio import sleep as s
from discord.ext.commands.core import has_permissions
from discord.message import Attachment
from discord.utils import get
from discord_components import DiscordComponents, Button, ButtonStyle



client = commands.Bot(command_prefix = '!')
dbb = DiscordComponents(client)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #COMMANDS

@client.command() #v1
@commands.has_permissions(kick_members=True)
async def alert(ctx, *, msg): #COMMAND NAME
    for guild in client.guilds:
        role = get(guild.roles, name = 'LowFloatMomentum Alerts') # roles
        for channel in guild.channels:
            if channel.name in ('lowfloatmomentum-alerts'):  # change for the list of channel names you got in your discord server
                one = Button(style=ButtonStyle.URL, label='Twitter', url="https://twitter.com/lowfloatmomo")
                two = Button(style=ButtonStyle.URL, label='Discord', url="https://discord.gg/darfN8Kq")
                """three = Button(style=ButtonStyle.URL, label='Trading Journal', url="https://tradingjournal.com")"""
                embed=discord.Embed(title= ':money_with_wings: **Stock Alert** :money_with_wings:', description= (msg), url='https://twitter.com/lowfloatmomo', color=0x33FF9F, timestamp=datetime.datetime.utcnow())
                """embed.set_author(name="Crypto Alert", icon_url = ctx.author.avatar_url)""" #Top left name # IGNORE
                embed.set_thumbnail(url='https://c1.peakpx.com/wallpaper/344/741/154/bull-sculpture-ox-horns-animal-wallpaper.jpg')
                embed.set_footer(icon_url = ctx.author.avatar_url, text='Powered by Duck Programming',)
                await channel.send(f"{role.mention}")                 
                await channel.send(embed=embed)
                await channel.send(
                    '**  **',
                    components=[
                        [one,
                        two]
                    ]
                )  


                      

@client.command() #v1
@commands.has_permissions(kick_members=True)
async def trim(ctx, *, msg): #COMMAND NAME
    for guild in client.guilds:
        role = get(guild.roles, name = 'LowFloatMomentum Alerts') # roles
        for channel in guild.channels:
            if channel.name in ('lowfloatmomentum-alerts'):  # change for the channel names
                one = Button(style=ButtonStyle.URL, label='Twitter', url="https://twitter.com/lowfloatmomo")
                two = Button(style=ButtonStyle.URL, label='Discord', url="https://discord.gg/darfN8Kq")
                """three = Button(style=ButtonStyle.URL, label='Trading Journal', url="https://tradingjournal.com")"""
                embed=discord.Embed(title= ':scissors: **Crypto Trim** :scissors:', description= (msg), url='https://twitter.com/lowfloatmomo', color=0x33FF9F, timestamp=datetime.datetime.utcnow())
                """embed.set_author(name="Crypto Alert", icon_url = ctx.author.avatar_url)""" #Top left name # IGNORE
                embed.set_thumbnail(url='https://c1.peakpx.com/wallpaper/344/741/154/bull-sculpture-ox-horns-animal-wallpaper.jpg')
                embed.set_footer(icon_url = ctx.author.avatar_url, text='Powered by Duck Programming',)
                await channel.send(f"{role.mention}")                 
                await channel.send(embed=embed)
                await channel.send(
                    '**  **',
                    components=[
                        [one,
                        two]
                    ]
                )

@client.command() #v1
@commands.has_permissions(kick_members=True)
async def update(ctx, *, msg): #COMMAND NAME
    for guild in client.guilds:
        role = get(guild.roles, name = 'LowFloatMomentum Alerts')  # roles
        for channel in guild.channels:
            if channel.name in ('lowfloatmomentum-alerts'):  # change for the channel names
                one = Button(style=ButtonStyle.URL, label='Twitter', url="https://twitter.com/lowfloatmomo")
                two = Button(style=ButtonStyle.URL, label='Discord', url="https://discord.gg/darfN8Kq")
                """three = Button(style=ButtonStyle.URL, label='Trading Journal', url="https://tradingjournal.com")"""
                embed=discord.Embed(title= ':warning: **Stock Update** :warning: ', description= (msg), url='https://twitter.com/lowfloatmomo', color=0x33FF9F, timestamp=datetime.datetime.utcnow())
                """embed.set_author(name="Crypto Alert", icon_url = ctx.author.avatar_url)""" #Top left name # IGNORE
                embed.set_thumbnail(url='https://c1.peakpx.com/wallpaper/344/741/154/bull-sculpture-ox-horns-animal-wallpaper.jpg')
                embed.set_footer(icon_url = ctx.author.avatar_url, text='Powered by Duck Programming',)
                await channel.send(f"{role.mention}")                 
                await channel.send(embed=embed)
                await channel.send(
                    '**  **',
                    components=[
                        [one,
                        two]
                    ]
                )

@client.command() #v1
@commands.has_permissions(kick_members=True)
async def image(ctx, *, msg): #COMMAND NAME
    for guild in client.guilds:
        role = get(guild.roles, name = 'LowFloatMomentum Alerts')  # roles
        for channel in guild.channels:
            if channel.name in ('lowfloatmomentum-alerts'):  # change for the channel names
                one = Button(style=ButtonStyle.URL, label='Twitter', url="https://twitter.com/lowfloatmomo")
                two = Button(style=ButtonStyle.URL, label='Discord', url="https://discord.gg/darfN8Kq")
                """three = Button(style=ButtonStyle.URL, label='Trading Journal', url="https://tradingjournal.com")"""
                embed=discord.Embed(title= ':money_with_wings: **Stock Alert** :money_with_wings:', description= (msg), url='https://twitter.com/lowfloatmomo', color=0x33FF9F, timestamp=datetime.datetime.utcnow())
                """embed.set_author(name="Stock Alert", icon_url = ctx.author.avatar_url)""" #Top left name # IGNORE
                embed.set_thumbnail(url='https://c1.peakpx.com/wallpaper/344/741/154/bull-sculpture-ox-horns-animal-wallpaper.jpg')
                embed.set_image(url=ctx.message.attachments[0].url)
                embed.set_footer(icon_url = ctx.author.avatar_url, text='Powered by Duck Programming',)
                await channel.send(f"{role.mention}")                 
                await channel.send(embed=embed)
                await channel.send(
                    '**  **',
                    components=[
                        [one,
                        two]
                    ]
                )

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#SERVER LIST

@client.command()
@commands.has_permissions(kick_members=True)
async def botservers(ctx):
    await ctx.send(f"**I'm currently in {len(client.guilds)} servers!** :white_check_mark:")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#ERROR MESSAGES (IGNORE)
@alert.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(":red_circle: **WEAKLING!** You have no **POWER** to command me, **MORTAL**! :red_circle:")

        
@trim.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(":red_circle: **WEAKLING!** You have no **POWER** to command me, **MORTAL**! :red_circle:")

@update.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(":red_circle: **WEAKLING!** You have no **POWER** to command me, **MORTAL**! :red_circle:")

@image.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(":red_circle: **WEAKLING!** You have no **POWER** to command me, **MORTAL**! :red_circle:")

@botservers.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(":red_circle: **WEAKLING!** You have no **POWER** to command me, **MORTAL**! :red_circle:")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#LEAVING THE SERVER

@client.command()
@commands.has_permissions(kick_members=True)
async def leaveg(ctx, *, guild_name):
    guild = discord.utils.get(client.guilds, name=guild_name) # Get the guild by name
    if guild is None:
        await ctx.send(":red_circle: No **Discord Servers** that i'm currently in with that name is **found**. :red_circle: ") # No guild found
    await ctx.send(f"**Farewell** `{guild.name}!` Contact `LowFloatMomentum` if you want my *sexy ass* back")
    await guild.leave() # Guild found



client.run('ODgyNzg2NDM0NDkzMzM3NjMw.YTAc7w.OFgjhORi2FghZDh_wuvnWx6MXm8')#token
