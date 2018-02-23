import discord #for discord client
import asyncio #for async
import random #for random gen
import time #time framework

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

classes = [
	"CSC137": "CSC 137 - Computer Organization",
	"CSC133": "CSC 133 - Computer Graphics for Gaming",
	"ENGR17": "ENGR 017 - Intro to Elec Engineering",
	"MATH30": "MATH 30: Calculus 1-Differential Calculus",
	"CSC28": "CSC 28 - Discrete Structures in Computer Science",
	"CSC135": "CSC 135 - Computer Theory and Programming Languages",
	"PHYS11A": "Physics 11A: Mechanics",
	"CSC60": "CSC 60 -UNIX SYSTEMS",
	"CSC35": "CSC 35/CIS 20 (in x86): Assembly Programming + System Architecture",
	"CSC20": "CSC 20/CIS 23 (in JAVA): Data Structures and Algos 1/PM2",
	"CPE64": "CPE64/EEE64- Intro To Logic Design",
	"CPE185": "CPE 185 Advanced Logic Design",
	"CSC15": "CSC 15 (CIS 22+CIS 35) - Programming I",
	"MATH45": "Math 45-02",
	"PHYS11C": "Physics 11C: Electromagnetism",
	"EEE117": "EEE 117 + EEE 117: Network Analysis",
	"CSC134": "CSC 134 - Database Management Systems",
	"CSC138": "CSC 138 - Computer Networks and Internetz",
	"CSC130": "CSC 130 - Data Structures",
	"CSC131": "CSC 131 - Data Structures EXTREME!!!",
	"CPE166": "CPE 166: Hardware Design",
	"EEE180": "EEE 180"
]

#this gets called when Discord client comes "alive"
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------------')

#this gets called when a user sends a message
@client.event
async def on_message(message):
	
	#DEBUGGING MODE: use this to dump list of all roles in server
	if message.content.startswith('+roles'):
		for each in client.get_server("355086293501214730").roles:
			print(each)

	#command to list all classes that can be added by member
	if message.content.startswith('+classes'):
		print("nothing")

	#command to get class role added
	if message.content.startswith('+class'):
		print("nothing")

#this gets called when a new member joins server
@client.event
async def on_member_join(member):
	server = member.server #get reference to server
	random.seed(time.time()) #use time for seed
	greeting = random.choice(greetings) #pick random greeting
	fmt = '{0} {1.mention}\nYou\'ll have to set the classes you belong to, to get access to the class channels. You do this by using the +class command. Example:```+class CSC60 CSC130```To see a full class list, you can use ```+classes```To avoid clutter, please DM me these commands :)' #message string
	channel_id = discord.Object(id="373286303418155010")
	await client.send_message(channel_id, fmt.format(greeting, member))
	
#token for Discord bot. Redacted for security.
client.run('API_TOKEN_REDACTED')
