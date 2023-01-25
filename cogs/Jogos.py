import discord
from discord.ext import commands

class Jogos(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def velha(self, ctx, membro1 : discord.Member, membro2 : discord.Member):
    velha = False
    aux = 0
    matrix = [['⠀', '⠀', '⠀'], ['⠀', '⠀', '⠀'], ['⠀', '⠀', '⠀']]
    jogadas = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']
    venceu = False

    mensagem_init = (f"{membro1.mention} é o X\n{membro2.mention} é o O")
    await ctx.send(mensagem_init)
    message = await ctx.send(f"{matrix[0][0]}|{matrix[0][1]}|{matrix[0][2]}\n-------\n{matrix[1][0]}|{matrix[1][1]}|{matrix[1][2]}\n-------\n{matrix[2][0]}|{matrix[2][1]}|{matrix[2][2]}")
    
    while not velha:

      if aux % 2 == 0:
        jogador = 'X'
      else:
        jogador = 'O'
      
      
      

      def check(m):
        if m.author.id == membro1.id and aux%2 == 0:
          cont = True
        elif m.author.id == membro2.id and aux%2 != 0:
          cont = True
        else: 
          cont = False
        if cont == True:
          pass
          if m.content in jogadas:
            player = True
            jogadas.remove(m.content)
            linha, coluna = map(int, m.content.split())
            linha, coluna = linha - 1, coluna - 1
            matrix[linha][coluna] = jogador
          else:
            player = False
          
        return cont and player and m.channel == ctx.channel
      if aux != 0:
        await ctx.channel.purge(limit = 1)
    
      await self.client.wait_for("message", check=check)
      

      aux += 1
      await message.edit(content=f"{matrix[0][0]}|{matrix[0][1]}|{matrix[0][2]}\n-------\n{matrix[1][0]}|{matrix[1][1]}|{matrix[1][2]}\n-------\n{matrix[2][0]}|{matrix[2][1]}|{matrix[2][2]}")

      for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == jogador:
            venceu = True

      for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == jogador:
            venceu = True

      if (matrix[0][0] == matrix[1][1] == matrix[2][2] == jogador) or (matrix[0][2] == matrix[1][1] == matrix[2][0] == jogador):
            venceu = True

      
      if aux == 9 or venceu:
        if venceu:
          if jogador == 'X':
            await ctx.send(f'{membro1.mention} venceu!!')
          if jogador == 'O':
            await ctx.send(f'{membro2.mention} venceu!!')
        elif aux == 9:
          await ctx.send('Deu velha!')
        break
  @commands.command()
  async def conecta(self, ctx, membro1 : discord.Member, membro2 : discord.Member):
    ok = False
    matrix = [['⠀', '⠀', '⠀', '⠀', '⠀', '⠀', '⠀'], ['⠀', '⠀', '⠀', '⠀', '⠀', '⠀', '⠀'], ['⠀', '⠀', '⠀', '⠀', '⠀', '⠀', '⠀'], ['⠀', '⠀', '⠀', '⠀', '⠀', '⠀', '⠀'], ['⠀', '⠀', '⠀', '⠀', '⠀', '⠀', '⠀'], ['⠀', '⠀', '⠀', '⠀', '⠀', '⠀', '⠀']]
    jogadas = ['1', '2', '3', '4', '5', '6', '7']
    aux = 0
    message = await ctx.send(f'{matrix[0][0]}|{matrix[0][1]}|{matrix[0][2]}|{matrix[0][3]}|{matrix[0][4]}|{matrix[0][5]}|{matrix[0][6]}\n-----------------\n{matrix[1][0]}|{matrix[1][1]}|{matrix[1][2]}|{matrix[1][3]}|{matrix[1][4]}|{matrix[1][5]}|{matrix[1][6]}\n-----------------\n{matrix[2][0]}|{matrix[2][1]}|{matrix[2][2]}|{matrix[2][3]}|{matrix[2][4]}|{matrix[2][5]}|{matrix[2][6]}\n-----------------\n{matrix[3][0]}|{matrix[3][1]}|{matrix[3][2]}|{matrix[3][3]}|{matrix[3][4]}|{matrix[3][5]}|{matrix[3][6]}\n-----------------\n{matrix[4][0]}|{matrix[4][1]}|{matrix[4][2]}|{matrix[4][3]}|{matrix[4][4]}|{matrix[4][5]}|{matrix[4][6]}\n-----------------\n{matrix[5][0]}|{matrix[5][1]}|{matrix[5][2]}|{matrix[5][3]}|{matrix[5][4]}|{matrix[5][5]}|{matrix[5][6]}')


    while True:
      
      if aux % 2 == 0:
        piece = 'X'
      else:
        piece = 'O'
      def check(m):
        if m.author.id == membro1.id and aux%2 == 0:
          cont = True
        elif m.author.id == membro2.id and aux%2 != 0:
          cont = True
        else:
          cont = False
        if cont == True:
          pass
          if m.content in jogadas:
            player = True
            p = int(m.content)
            p -= 1
            for i in range(5, -1, -1):
              if matrix[i][p] == '⠀':
                matrix[i][p] = piece
                break
          else: 
            player = False
          
        return cont and player and m.channel == ctx.channel
      if aux != 0:
        await ctx.channel.purge(limit = 1)
    
      await self.client.wait_for("message", check=check)

      aux += 1



      for c in range(3):
        for r in range(6):
          if matrix[r][c] == piece and matrix[r][c+1] == piece and matrix[r][c+2] == piece and matrix[r][c+3] == piece:
            ok = True

      for c in range(7):
        for r in range(3):
          if matrix[r][c] == piece and matrix[r+1][c] == piece and matrix[r+2][c] == piece and matrix[r+3][c] == piece:
            ok = True

      for c in range(4):
        for r in range(3, 6):
          if matrix[r][c] == piece and matrix[r-1][c+1] == piece and matrix[r-2][c+2] == piece and matrix[r-3][c+3] == piece:
            ok = True

      for c in range(4):
        for r in range(3):
          if matrix[r][c] == piece and matrix[r+1][c+1] == piece and matrix[r+2][c+2] == piece and matrix[r+3][c+3] == piece:
            ok = True

      await message.edit(content=f'{matrix[0][0]}|{matrix[0][1]}|{matrix[0][2]}|{matrix[0][3]}|{matrix[0][4]}|{matrix[0][5]}|{matrix[0][6]}\n-----------------\n{matrix[1][0]}|{matrix[1][1]}|{matrix[1][2]}|{matrix[1][3]}|{matrix[1][4]}|{matrix[1][5]}|{matrix[1][6]}\n-----------------\n{matrix[2][0]}|{matrix[2][1]}|{matrix[2][2]}|{matrix[2][3]}|{matrix[2][4]}|{matrix[2][5]}|{matrix[2][6]}\n-----------------\n{matrix[3][0]}|{matrix[3][1]}|{matrix[3][2]}|{matrix[3][3]}|{matrix[3][4]}|{matrix[3][5]}|{matrix[3][6]}\n-----------------\n{matrix[4][0]}|{matrix[4][1]}|{matrix[4][2]}|{matrix[4][3]}|{matrix[4][4]}|{matrix[4][5]}|{matrix[4][6]}\n-----------------\n{matrix[5][0]}|{matrix[5][1]}|{matrix[5][2]}|{matrix[5][3]}|{matrix[5][4]}|{matrix[5][5]}|{matrix[5][6]}')

      if ok or aux == 42:
        if piece == 'X':
          await ctx.send(f'{membro1.mention} venceu!!')
        if piece == 'O':
          await ctx.send(f'{membro2.mention} venceu!!')
        if aux == 42:
          await ctx.send('WhatsApp!')
        break

def setup(client):
  client.add_cog(Jogos(client))