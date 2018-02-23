import discord #for discord client
import asyncio #for async
import random #for random gen

client = discord.Client() #initialize discord client

#array of different ways to greet someone
greetings = [
	"Aloha",
	"Hola",
	"Que pasa?",
	"Bonjour",
	"Hallo",
	"Ciao",
	"Konnichiwa",
	"Ello, mate",
	"Heeey, baaaaaby",
	"Oh, yoooouhoooo!",
	"How you doin?",
	"Why, hello there!",
	"Hello, sunshine!",
	"Howdy, partner!",
	"Hey, howdy, hi!",
	"Whats kickin, little chicken?",
	"Peek-a-boo!",
	"Howdy-doody!",
	"Hey there, freshman!",
	"My name's Ralph, and I'm a bad guy.",
	"Hi, mister!",
	"I come in peace!",
	"Put that cookie down!",
	"Ahoy, matey!",
	"Hiya!",
	"Ello, gov'nor!",
	"Top of the mornin to ya!",
	"Whats crackin?",
	"GOOOOOD MORNING, VIETNAM!",
	"Sup, homeslice?",
	"This call may be recorded for training purposes.",
	"Howdy, howdy, howdy!",
	"I'm Batman.",
	"At least, we meet for the first time for the last time!",
	"Hello, who's there, I'm talking.",
	"Here's Johnny!",
	"You know who this is.",
	"Ghostbusters, whatya want?",
	"Yo!",
	"Whaddup",
	"Greetings and saluations!",
	"Doctor."
]

#this gets called when Discord client comes "alive"
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------------')

#token for Discord bot. Redacted for security.
client.run('TOKEN_REDACTED')
