import discord
import math
import random
from discord.ext import commands

#permisos
intents = discord.Intents.default()
intents.message_content = True

#prefijo
bot = commands.Bot(command_prefix = "/" , intents = intents)

@bot.command(name = "saluda")
async def saludar(ctx):
    await ctx.send("Bienvenido!")


@bot.command(name = "suma")
async def suma(ctx, n1: int , n2: int): 
    resultado = n1 + n2
    await ctx.send(f"Resultado = {resultado}")

@bot.command(name = "potencia")
async def potencia(ctx, n1: int , n2: int): 
    resultado = n1 ** n2
    await ctx.send(f"Resultado = {resultado}")

@bot.command(name = "raiz")
async def raiz(ctx, n1: int): 
    resultado = math.sqrt(n1)
    await ctx.send(f"Resultado = {resultado}")

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command(name = "despedir")
async def despedir(ctx):
    await ctx.send("Hasta luego!")

bot.run("")
