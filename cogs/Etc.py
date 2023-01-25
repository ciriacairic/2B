import discord
from discord.ext import commands

class Etc(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Bule ready.')

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.client.user:
      return

  @commands.command()
  async def say(self, ctx, *,message):
    await ctx.channel.purge(limit = 1)
    await ctx.send(message)

  @commands.command()
  async def cocacola(self, ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/645066505528279054/803419900038217749/cocacola.mp4')

def setup(client):
  client.add_cog(Etc(client))