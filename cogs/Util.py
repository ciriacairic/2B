import discord
from discord.ext import commands
from datetime import date

from listas import dias_da_semana
from listas import drives
from listas import anti_embed

class Util(commands.Cog):

    def __init__(self, client):
      self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.author == self.client.user:
        if any(word in message.content for word in anti_embed):
          await message.edit(suppress=True)
        return

    @commands.Cog.listener()
    async def on_ready(self):
      print('2B ready.')

    @commands.command()
    async def aula(self, ctx):
      data = date.today()
      data = data.weekday()
      await ctx.send(dias_da_semana[data])

    @commands.command()
    async def seg(self, ctx):
      await ctx.send(dias_da_semana[0])

    @commands.command()
    async def ter(self, ctx):
      await ctx.send(dias_da_semana[1])

    @commands.command()
    async def qua(self, ctx):
      await ctx.send(dias_da_semana[2])

    @commands.command()
    async def qui(self, ctx):
      await ctx.send(dias_da_semana[3])

    @commands.command()
    async def sex(self, ctx):
      await ctx.send(dias_da_semana[4])

    @commands.command()
    async def flag(self, ctx):
      await ctx.send('Glória à humanidade.')

    @commands.command()
    async def acervo(self, ctx):
      await ctx.send('https://www.notion.so/O-Grande-Acervo-a60cdade73824bf5a444f601f8e3d589')

    @commands.command()
    async def drive(self, ctx):
      await ctx.send(drives)

    @commands.command()
    async def colinha(self, ctx):
      await ctx.send('Ninguém é de ferro\nhttps://replit.com/@MarioGhio/HelpingHelper-Bot')

def setup(client):
  client.add_cog(Util(client))