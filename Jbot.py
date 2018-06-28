import discord
from discord.ext.commands import Bot
from discord.ext import commands
import datetime
from time import localtime, strftime
import asyncio
import time
import os
import threading
import re

try:
    check = open("reminders.txt","r+")
    print("reminders.txt succesfully found")
except IOError:
    f = open("reminders.txt","w+")
    f.close()
    print('File "reminders.txt" created')
    print('Is this your first time running me? Or did I move to a new location without my reminders.txt?')

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Jbot is ready!")

### REMINDER FUNCTIONS HERE ###
def readFile():             
    d = []
    with open("reminders.txt") as infile:
        for i in infile:
            d.append(eval(i))
    infile.close()
    return d
def addline(string):        
    f = open('reminders.txt','a')
    f.write(string+'\n')
    f.close()

def addReminder(time, Vvalue):
    lines = [line.rstrip('\n') for line in open('reminders.txt','r+')]
    value = re.sub("'", '', Vvalue)
    addline("{'Time': '"+str(time)+"','Reminder': '"+str(value)+"'}")
    #print(lines)
    return "Reminder added"
def removeReminder(time, value): 
    f = open('reminders.txt','r+')
    d = readFile()
    f.close()
    matches = []
    for i in d:
        if i['Time'] == time and i['Reminder'] == value:
            matches.append(i)
    open('reminders.txt','w').close()  #DELETES EVERYTHING IN THE TEXT FILE
    f = open('reminders.txt','a+')
    for i in d:
        if  i != matches[0]:
            addReminder(i.get('Time'),i.get('Reminder'))
    f.close()
    
def getDay():
    return datetime.datetime.today()
    
def remindme(time, timeType, note):
    if timeType == 'h':
        key = getDay() + datetime.timedelta(hours=time)
        addReminder(str(key)[:19], str(note))
    if timeType == 'd':
        key = getDay() + datetime.timedelta(days=time)
        addReminder(str(key)[:19], str(note))
    if timeType == 'm':
        key = getDay() + datetime.timedelta(minutes=time)
        addReminder(str(key)[:19], str(note))
    if timeType == 's':
        key = getDay() + datetime.timedelta(seconds=time)
        addReminder(str(key)[:19], str(note))
    
async def reminder():
    await client.wait_until_ready()
    while(1):
        d = readFile()
        time = str(getDay())[:19]
        matches = []
        for i in d:
            if i['Time'] == time:
                matches.append(i)
        for i in matches:
            await client.send_message(discord.Object(id='461245192180072448'), str(i['Reminder']))
            removeReminder(i['Time'], i['Reminder'])
        #print("checking: "+str(time))
        await asyncio.sleep(1)

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
        t = string.split()[2]
        vT = string.split()[3:]
        v = ' '.join(vT)
        if str(t) == 'h':
            if int(k) > 24:
                await client.send_message(message.channel, "BLYAT, use d for times over 24 hours! дерьмовый разработчик")
            else:
                userID = message.author.id
                value = ("<@%s> " % (userID)) + str(v)
                remindme(int(k), 'h', str(value))
                await client.send_message(message.channel, 'You will be reminded of message: "'+str(v)+'" in '+str(k)+' hour(s) in the #reminders channel.')
        elif str(t) == 'd':
            if int(k) > 365:
                await client.send_message(message.channel, "I'll allow it, but I'll probably be dead by the time I get to reminding you...")
                userID = message.author.id
                value = ("<@%s> " % (userID)) + str(v)
                remindme(int(k), 'd', str(value))
                await client.send_message(message.channel, 'You will be reminded of message: "'+str(v)+'" in '+str(k)+' day(s) in the #reminders channel.')
            else:
                userID = message.author.id
                value = ("<@%s> " % (userID)) + str(v)
                remindme(int(k), 'd', str(value))
                await client.send_message(message.channel, 'You will be reminded of message: "'+str(v)+'" in '+str(k)+' day(s) in the #reminders channel.')
        elif str(t) == 'm':
            if int(k) > 59:
                await client.send_message(message.channel, "BLYAT, use 'h' for hours!")
            else:
                userID = message.author.id
                value = ("<@%s> " % (userID)) + str(v)
                remindme(int(k), 'm', str(value))
                await client.send_message(message.channel, 'You will be reminded of message: "'+str(v)+'" in '+str(k)+' minute(s) in the #reminders channel.')
        elif str(t) == 's':
            if int(k) > 59:
                await client.send_message(message.channel, "BLYAT, use 'm' for minutes!")
            else:
                userID = message.author.id
                value = ("<@%s> " % (userID)) + str(v)
                remindme(int(k), 's', str(value))
                await client.send_message(message.channel, 'You will be reminded of message: "'+str(v)+'" in '+str(k)+' seconds(s) in the #reminders channel, глупый идиот.')

        else:
            await client.send_message(message.channel, 'Use h, m, s, or d to denote the length of reminder.  "Example: !remindme 3 d Make a better bot."')
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
        await client.send_message(message.channel, "!remindme [time] [timetype] [note] and I'll give you a reminder after the time you designated has passed!")
        await client.send_message(message.channel, "I also curse at you in russian when certain commands are entered, and help administrate things.")
        await client.send_message(message.channel, "A more up to date/detailed list may be found here with my source code: https://github.com/Sp4zzy/Jbot-for-Discord/blob/master/README.md")
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


client.run("C H A N G E")

