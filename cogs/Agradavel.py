import discord
from discord.ext import commands

from listas import links_marimba
import random


class Agradavel(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Agradavel ready.')

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.client.user:
      return
    
    if '```' in message.content:
      await message.add_reaction('👏')

    if '2B' in message.content:
      if message.content.lower().startswith('bom dia'):
        await message.channel.send(f'Bom dia {message.author.mention}, {message.author.roles[-1]}')
      
      if message.content.lower().startswith('boa tarde'):
        await message.channel.send(f'Boa tarde {message.author.mention}, {message.author.roles[-1]}')

      if message.content.lower().startswith('boa noite'):
        await message.channel.send(f'Boa noite {message.author.mention}, {message.author.roles[-1]}')

  @commands.command()
  async def marimba(self, ctx):
    await ctx.send(random.choice(links_marimba))

def setup(client):
  client.add_cog(Agradavel(client))