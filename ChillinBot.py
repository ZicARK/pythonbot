import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '~')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hi , Welcome to Chillin Discord please @ who invited u so he rank u then check #rules & #roles to choose ur own ranks')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content.startswith('~Help'):
        await client.send_message(message.channel,'Hi cutie <@%s> Please try my commands "~Chillininfo" "~whomadeyou"'  %(message.author.id))
    if message.content == '~whomadeyou':
        await client.send_message(message.channel,'Zic is my dad , he made so I can help yall with knowing Chillin .... Thx daddy zic and mommy Chup')
    if message.content == '~Chillininfo':
        await client.send_message(message.channel,'Chillin owner is Silver ( ID : S_ily ) Chillin is not like the other tribes , In Chillin we dont have the slaving system and members get admin if we trust them and that what make us special !! ')
    if message.content.startswith('~Help'):
        await client.send_message(message.channel,'Hi cutie <@%s> Please try my commands "~Chillininfo" , "~whomadeyou" , "~Chillininfo"'  %(message.author.id))
client.run('NjkwMTkzMjQwOTE3NTQxMDMx.XsjSSg.dt84msUfcBILOoLmW4GGNY9EJd0')
