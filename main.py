import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

my_secret = os.environ['chave']

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '%', intents=intents)

@client.command()
async def load(ctx, extension):
  try:
    if ctx.author.id == 521802585401720883:
      client.load_extension(f'cogs.{extension}')
      await ctx.send(f'{extension} carregada.')
  except:
    await ctx.send('Você não tem esse poder!')

@client.command()
async def unload(ctx, extension):
  try:
    if ctx.author.id == 521802585401720883:
      client.unload_extension(f'cogs.{extension}')
      await ctx.send(f'{extension} descarregada.')
  except:
    await ctx.send('Você não tem esse poder!')

@client.command()
async def reload(ctx, extension):
  try:
    if ctx.author.id == 521802585401720883:
      client.unload_extension(f'cogs.{extension}')
      client.load_extension(f'cogs.{extension}')
      await ctx.send(f'{extension} recarregada.')
  except:
    await ctx.send('Você não tem esse poder!')

@client.command()
async def ping(ctx):
  await ctx.send(f'Ping: {round(client.latency*1000)}ms')

for filename in os.listdir('./cogs'): 
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

keep_alive()
client.run(my_secret)