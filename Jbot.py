import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Jbot is ready!")

@client.event
async def on_message(message):
    if message.content.upper() == "!HELLO":
        await client.send_message(message.channel, ":wave: Sup dude. I'm a bot with limited commands.  If you want me to have some functionality, get in touch with Jboi.")
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!CLEAR'):
        #if message.author.id == "93141711059968000":
        if "400365260990578691" in [role.id for role in message.author.roles]:
            if len(str(message.content)) >= 8:
                m = str(message.content)
                number = int(m[7:])
                msg = []
                async for i in client.logs_from(message.channel, limit = number+1):
                    msg.append(i)
                await client.delete_messages(msg)
            else:
                await client.send_message(message.channel, "Oops, you forgot to tell me how many to delete!")
        else:
            await client.send_message(message.channel, "You're not a Supreme Commander...")


client.run("NDU0NzMwMTY2ODE2NjA0MTgw.Dfx1uQ.ZCygg0nIlVsTZ4d7ra_GY81F-Yo")

