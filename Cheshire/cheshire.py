import discord
import asyncio

client = discord.Client()

greetingQuotes = [
	"Hello, sunshine!"
	"Howdy, partner!"
	"Hey, howdy, hi!"
	"Whats kickin, little chicken?"
	"Peek-a-boo!"
	"Howdy-doody!"
	"Hey there, freshman!"
	"My name's Cheshire, and I'm a bad guy."
	"Hi, mister!"
	"I come in peace!"
	"Put that cookie down!"
	"Ahoy, matey!"
	"Hiya!"
	"Ello, gov'nor!"
	"Top of the mornin' to ya!"
	"Whats crackin?"
	"GOOOOOD MORNING, VIETNAM!"
	"Sup, homeslice?"
	"This call may be recorded for training purposes."
	"Howdy, howdy, howdy!"
	"Im Batman"
	"At least, we meet for the first time for the last time!",
]


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------------')

client.run('TOKEN_REDACTED')
