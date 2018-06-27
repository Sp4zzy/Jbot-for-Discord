import discord
from discord.ext.commands import Bot
from discord.ext import commands
import datetime
from time import localtime, strftime
import asyncio
import time
import os
import threading

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Jbot is ready!")

### REMINDER FUNCTIONS HERE ###
def getTimeSTR():
    return strftime("%H:%M", localtime())
def getTimeINT():
    return int(strftime("%H", localtime()))
def getMinSTR():
    return strftime("%M", localtime())
def getSecINT():
    return int(strftime("%S", localtime()))

RemindList = {}
    
def remindme(time, value):
    #if time >= 24: DO CHECK THIS IN THE on_message PART
        #client.send_message(message.channel,
    testTime = getTimeINT() + time
    if testTime > 24:
        newTime = str(testTime%24)+":"+getMinSTR()
    else:
        newTime = str(testTime)+":"+getMinSTR()
    RemindList[newTime] = value
    print(RemindList)
    
async def reminder():
    await client.wait_until_ready()
    while(1):
        print("Checking: "+getTimeSTR()+" against "+ str(RemindList.keys()))
        if getTimeSTR() in RemindList.keys():
            await client.send_message(discord.Object(id='461245192180072448'), RemindList[getTimeSTR()])
            del RemindList[getTimeSTR()]
        await asyncio.sleep(5)

client.loop.create_task(reminder())

### /REMINDER FUNCTIONS ###
            
### CLEAR FUNCTION ###      
def is_pinned(message):
    if message.pinned:
        return False
    else:
        return True

### /CLEAR FUNCTIONS ###

    
@client.event
async def on_message(message):
    if message.content.upper().startswith("!REMINDME"):
        string = str(message.content)
        k = string.split()[1]
        vT = string.split()[2:]
        v = ' '.join(vT)
        #await client.send_message(message.channel, "Okay here's what I got: "+str(k)+str(vT)+str(v))
        if int(k) > 24:
            await client.send_message(message.channel, "We only remind for max of 23 hours during my testing phase. дерьмовый разработчик")
        else:
            userID = message.author.id
            #RemindList[int(k)] = ("<@%s> " % (userID)) + str(v)
            value = ("<@%s> " % (userID)) + str(v)
            remindme(int(k), str(value))
            await client.send_message(message.channel, 'You will be reminded of message: "'+str(value)+'" in '+str(k)+' hour(s) in the Reminders channel.')
    if message.content.upper().startswith("!TESTREMIND"):
        string = str(message.content)
        k = string.split()[1]
        await client.send_message(message.channel, "Next time "+str(k)+" seconds comes around, I'll remind you as a test that I work.")
        userID = message.author.id
        value = ("<@%s> " % (userID)) + " I worked!"
        SECremindme(int(k), str(value))
    if message.content.upper() == "HI BOT":
        await client.send_message(message.channel, ":wave: hi bot")
    if message.content.upper() == "!HELP":
        await client.send_message(message.channel, "Sup, I play music using !yt, and stop using !stop, and will leave the voice channel with !youcango")
        await client.send_message(message.channel, "!remindme [hours] [note] and i'll give u a reminder after the hours you designated have passed!")
        await client.send_message(message.channel, "I also curse at you in russian when certain commands are entered, and help administrate things.")
        await client.send_message(message.channel, "A more up to date list may be found here: https://github.com/Sp4zzy/Jbot-for-Discord/blob/master/README.md")
    if message.content.upper() == "!HELLO":
        await client.send_message(message.channel, ":wave: Sup dude. I'm a bot with limited commands.  If you want me to have some functionality, get in touch with Jboi.")
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!CLEAR'):
        if "400365260990578691" in [role.id for role in message.author.roles]:
            if len(str(message.content)) >= 8:
                m = str(message.content)
                number = int(m[7:])
                msg = []
                async for i in client.logs_from(message.channel, limit = number+1):
                    msg.append(i)
                await client.purge_from(message.channel, limit = number+1, check = is_pinned)#after = datetime.date(2018,6,1))
            else:
                await client.send_message(message.channel, "Oops, you forgot to tell me how many to delete!")
        else:
            await client.send_message(message.channel, "You're not a Supreme Commander...")
    if message.content.upper().startswith('!PURGE'):
        #if message.author.id == "93141711059968000":
        if "400365260990578691" in [role.id for role in message.author.roles]:
                await client.purge_from(message.channel, check = is_pinned)#after = datetime.date(2018,6,1))
        else:
            await client.send_message(message.channel, "You're not a Supreme Commander...")
    if message.content.upper().startswith('!YT'):
        if len(str(message.content)) >= 5:
            vc = await client.join_voice_channel(message.author.voice_channel)
            player = await vc.create_ytdl_player(str(message.content)[4:])
            await client.send_message(message.channel, "Hey, I'm gonna play "+str(message.content)[4:]+" on the request of "+str(message.author))
            player.start()
        else:
            await client.send_message(message.channel, "You forgot to give me a youtube link!")
    if message.content.upper().startswith('!YOUCANGO'):
        await client.send_message(message.channel, "пока!")
        os.system("taskkill /f /im ffmpeg.exe")
        for x in client.voice_clients:
            if(x.server == message.server):
                await x.disconnect()
    if message.content.upper().startswith('!STOP'):
        await client.send_message(message.channel, "Stopping playback")
        os.system("taskkill /f /im ffmpeg.exe")
    if message.content.upper().startswith('!WTFILOVECOMMUNISM'):
        vc = await client.join_voice_channel(message.author.voice_channel)
        player = await vc.create_ytdl_player("https://www.youtube.com/watch?v=U06jlgpMtQs")
        await client.send_message(message.channel, "Opatchki! Finally some culture!")
        player.start()

    if "nikita" in message.content.lower():
        await client.send_message(message.channel, "<:IsThisA:451079458460532736> папа?")
    if "cheeki breeki" in message.content.lower():
        await client.send_message(message.channel, "<:cheeki:400365545385361408> А ну, чики-брики и в дамки! One two, you're on top! <:breeki:400367609402490890>")
    if "cyka blyat" in message.content.lower():
        await client.send_message(message.channel, "<:scav:400367157361377300> приходите сюда мудак! (prikhodite syuda mudak)")
    if "i hate russians" in message.content.lower():
        await client.send_message(message.channel, "<:scav2:400367971115073537> трахать тебя мудак!")


client.run("C H A N G E T H I S")

