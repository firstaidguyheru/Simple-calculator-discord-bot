from asyncio import sleep
import discord
from discord.ext import commands
import random
import math
from dotenv import load_dotenv


load_dotenv()


client = commands.AutoShardedBot(commands.when_mentioned_or('!'))


@client.event
async def on_ready():
	print('Ready.')

def add(n: float, n2: float):
	return n + n2

def sub(n: float, n2: float):
	return n - n2

def rando(n: int, n2: int):
	return random.randint(n, n2)

def div(n: float, n2: float):
	return n / n2

def sqrt(n: float):
	return math.sqrt(n)

def mult(n: float, n2: float):
	return n * n2

@client.command()
async def mathadd(ctx, x: float, y: float):
	try:
		result = add(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathsub(ctx, x: float, y: float):
	try:
		result = sub(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathrando(ctx, x: int, y: int):
	try:
		result = rando(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathdiv(ctx, x: float, y: float):
	try:
		result = div(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathmult(ctx, x: float, y: float):
	try:
		result = mult(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathsqrt(ctx, x: float):
	try:
		result = sqrt(x)
		await ctx.send(result)

	except:
		pass

client.run(os.getenv("TOKEN"))
