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
import signal
import sys

try:
    check = open("reminders.txt","r+")
    print("reminders.txt succesfully found")
except IOError:
    f = open("reminders.txt","w+")
    f.close()
    print('File "reminders.txt" created')
    print('Is this your first time running me? Or did I move to a new location without my reminders.txt?')

def getTime(): #Logging uses
    return datetime.datetime.now().strftime("\n[%H:%M:%S] ")
def getDate(): #getFormattedDate
    return datetime.datetime.today().strftime("[%y-%m-%d-%H%M%S]-")
def getDay(): #Used in discord functionality
    return datetime.datetime.today()
logDate = getDate()
try:
    check = open(logDate+"log.txt","r+")
except IOError:
    log = open(logDate+"log.txt","w+")
    print(logDate+"log.txt succesfully created")
    log.close()

def signal_handler(sig, frame):
    print("Program exited with CTRL+C.")
    time.sleep(3)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    #await client.change_presence(game=discord.Game(name='[7/28] - Finished updates for now.'))
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

def addReminder(time, Vvalue, chanID):
    lines = [line.rstrip('\n') for line in open('reminders.txt','r+')]
    value = re.sub("'", '', Vvalue)
    addline("{'Time': '"+str(time)+"','Reminder': '"+str(value)+"','Channel': '"+str(chanID)+"'}")
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
            addReminder(i.get('Time'),i.get('Reminder'),i.get('Channel'))
    f.close()

def remindme(time, timeType, note, chanID):
    if timeType == 'h':
        key = getDay() + datetime.timedelta(hours=time)
        addReminder(str(key)[:19], str(note), chanID)
    if timeType == 'd':
        key = getDay() + datetime.timedelta(days=time)
        addReminder(str(key)[:19], str(note), chanID)
    if timeType == 'm':
        key = getDay() + datetime.timedelta(minutes=time)
        addReminder(str(key)[:19], str(note), chanID)
    if timeType == 's':
        key = getDay() + datetime.timedelta(seconds=time)
        addReminder(str(key)[:19], str(note), chanID)

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
            await client.send_message(discord.Object(id=str(i['Channel'])), str(i['Reminder']))
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

def getChanID(channel):
    chanID = discord.utils.get(client.get_all_channels(), name=str(channel))
    return chanID.id

@client.event
async def on_message(message):
    log = open(logDate+"log.txt","a", encoding='utf-8')
    if message.content.upper().startswith("!CHECKADMIN"):
        log.write(getTime()+"!checkadmin command issued by "+str(message.author)+"----"+str(message.content)+"===="+str(message.server))
        await client.send_message(message.channel, str(message.author.server_permissions.administrator))
    if message.content.upper().startswith("!REMINDME"):
        log.write(getTime()+"!remindme command issued by "+str(message.author)+"----"+str(message.content)+"===="+str(message.server))
        try:
            string = str(message.content)
            k = string.split()[1]
            try:
                int(k)
            except (SyntaxError, ValueError) as error:
                await client.send_message(message.channel, "That's not proper usage for this command, see !help, your 1st argument isn't an integer")
            t = string.split()[2]
            if t not in ['h','d','m','s']:
                await client.send_message(message.channel, "I need 'h','d','m', or 's' as the 2nd argument, see !help")
            vT = string.split()[3:]
            v = ' '.join(vT)
            userID = message.author.id
            chanID = message.channel.id
            if str(t) == 'h':
                if int(k) > 24:
                    await client.send_message(message.channel, "BLYAT, use d for times over 24 hours! дерьмовый разработчик")
                else:
                    value = ("<@%s> " % (userID)) + str(v)
                    remindme(int(k), 'h', str(value), chanID)
                    await client.send_message(message.channel, 'You will be reminded of message: "'+str(v)+'" in '+str(k)+' hour(s).')
            elif str(t) == 'd':
                if int(k) > 365:
                    await client.send_message(message.channel, "I'll allow it, but I'll probably be dead by the time I get to reminding you...")
                    value = ("<@%s> " % (userID)) + str(v)
                    remindme(int(k), 'd', str(value), chanID)
                    await client.send_message(message.channel, 'You will be reminded of message: "'+str(v)+'" in '+str(k)+' day(s).')
                else:
                    value = ("<@%s> " % (userID)) + str(v)
                    remindme(int(k), 'd', str(value), chanID)
                    await client.send_message(message.channel, 'You will be reminded of message: "'+str(v)+'" in '+str(k)+' day(s).')
            elif str(t) == 'm':
                value = ("<@%s> " % (userID)) + str(v)
                remindme(int(k), 'm', str(value), chanID)
                await client.send_message(message.channel, 'You will be reminded of message: "'+str(v)+'" in '+str(k)+' minute(s).')
            elif str(t) == 's':
                if int(k) > 59:
                    await client.send_message(message.channel, "BLYAT, use 'm' for minutes!")
                else:
                    value = ("<@%s> " % (userID)) + str(v)
                    remindme(int(k), 's', str(value), chanID)
                    await client.send_message(message.channel, 'You will be reminded of message: "'+str(v)+'" in '+str(k)+' seconds(s).  глупый идиот.')
        except (AttributeError, IndexError) as error:
            await client.send_message(message.channel, "Improper usage of command, you're missing/misusing arguments, see !help")
    if message.content.upper().startswith("!REMINDOTHER"):
        log.write(getTime()+"!remindother command issued by "+str(message.author)+"----"+str(message.content)+"===="+str(message.server))
        try:
            string = str(message.content)
            k = string.split()[1]
            t = string.split()[2]
            c = string.split()[3]
            vT = string.split()[4:]
            v = ' '.join(vT)
            for i in client.get_all_members():
                if c.upper() == str(str(i).split('#')[0]).upper():
                    userID = str(i.id)
            chanID = message.channel.id
            if message.author.server_permissions.administrator == True:
                value = "<@%s> "%userID + str(v)
                if str(t) == 'h':
                    if int(k) > 24:
                        await client.send_message(message.channel, "BLYAT, use d for times over 24 hours! дерьмовый разработчик")
                    else:
                        remindme(int(k), 'h', str(value), chanID)
                        await client.send_message(message.channel, 'I will do the reminder for "'+str(v)+'" in '+str(k)+' hour(s).')
                elif str(t) == 'd':
                    if int(k) > 365:
                        await client.send_message(message.channel, "I'll allow it, but I'll probably be dead by the time I get to reminding you...")
                        remindme(int(k), 'd', str(value), chanID)
                        await client.send_message(message.channel, 'I will do the reminder for "'+str(v)+'" in '+str(k)+' day(s).')
                    else:
                        remindme(int(k), 'd', str(value), chanID)
                        await client.send_message(message.channel, 'I will do the reminder for "'+str(v)+'" in '+str(k)+' day(s).')
                elif str(t) == 'm':
                    if int(k) > 59:
                        await client.send_message(message.channel, "BLYAT, use 'h' for hours!")
                    else:
                        remindme(int(k), 'm', str(value), chanID)
                        await client.send_message(message.channel, 'I will do the reminder for "'+str(v)+'" in '+str(k)+' minute(s).')
                elif str(t) == 's':
                    if int(k) > 59:
                        await client.send_message(message.channel, "BLYAT, use 'm' for minutes!")
                    else:
                        remindme(int(k), 's', str(value), chanID)
                        await client.send_message(message.channel, 'I will do the reminder for "'+str(v)+'" in '+str(k)+' seconds(s).  глупый идиот.')
                else:
                    await client.send_message(message.channel, 'Use h, m, s, or d to denote the length of reminder.  "Example: !remindme 3 d Make a better bot."')
            else:
                await client.send_message(message.channel, "Sorry, only server administrators can use this command!")
        except (AttributeError, IndexError) as error:
            await client.send_message(message.channel, "Improper usage of command, you're missing/misusing arguments, see !help")
    if message.content.upper().startswith("!ANNOUNCE"):
        log.write(getTime()+"!announce command issued by "+str(message.author)+"----"+str(message.content)+"===="+str(message.server))
        try:
            string = str(message.content)
            k = string.split()[1]
            t = string.split()[2]
            c = string.split()[3]
            vT = string.split()[4:]
            v = ' '.join(vT)
            userID = '@everyone'
            chanID = discord.utils.get(client.get_all_channels(),
                                       server__name=str(message.server),
                                       name=str(c))
            if message.author.server_permissions.administrator == True:
                if str(t) == 'h':
                    if int(k) > 24:
                        await client.send_message(message.channel, "BLYAT, use d for times over 24 hours! дерьмовый разработчик")
                    else:
                        value = ("%s " % (userID)) + str(v)
                        remindme(int(k), 'h', str(value), chanID.id)
                        await client.send_message(message.channel, 'You will be reminded of message: "'+str(v)+'" in '+str(k)+' hour(s).')
                elif str(t) == 'd':
                    if int(k) > 365:
                        await client.send_message(message.channel, "I'll allow it, but I'll probably be dead by the time I get to reminding you...")
                        value = ("%s " % (userID)) + str(v)
                        remindme(int(k), 'd', str(value), chanID.id)
                        await client.send_message(message.channel, 'I\'ll announce the message: "'+str(v)+'" in '+str(k)+' day(s).')
                    else:
                        value = ("%s " % (userID)) + str(v)
                        remindme(int(k), 'd', str(value), chanID.id)
                        await client.send_message(message.channel, 'I\'ll announce the message: "'+str(v)+'" in '+str(k)+' day(s).')
                elif str(t) == 'm':
                    if int(k) > 59:
                        await client.send_message(message.channel, "BLYAT, use 'h' for hours!")
                    else:
                        value = ("%s " % (userID)) + str(v)
                        remindme(int(k), 'm', str(value), chanID.id)
                        await client.send_message(message.channel, 'I\'ll announce the message: "'+str(v)+'" in '+str(k)+' minute(s).')
                elif str(t) == 's':
                    if int(k) > 59:
                        await client.send_message(message.channel, "BLYAT, use 'm' for minutes!")
                    else:
                        value = ("%s " % (userID)) + str(v)
                        remindme(int(k), 's', str(value), chanID.id)
                        await client.send_message(message.channel, 'I\'ll announce the message: "'+str(v)+'" in '+str(k)+' seconds(s).  глупый идиот.')
                else:
                    await client.send_message(message.channel, 'Use h, m, s, or d to denote the length of reminder.  "Example: !remindme 3 d Make a better bot."')
            else:
                await client.send_message(message.channel, "Sorry, only server administrators can use this command!")
        except (AttributeError, IndexError) as error:
            await client.send_message(message.channel, "Improper usage of command, you're missing/misusing arguments, see !help")
    if message.content.upper() == "HI BOT":
        await client.send_message(message.channel, ":wave: hi bot")
    if message.content.upper() == "!HELP":
        await client.send_message(message.channel, "Sup, I play music using !yt, and stop using !stop")
        await client.send_message(message.channel, "!remindme [time] [timetype] [note] and I'll give you a reminder after the time you designated has passed!")
        await client.send_message(message.channel, "I also curse at you in russian when certain commands are entered, and help administrate things.")
        await client.send_message(message.channel, "A more up to date/detailed list may be found here with my source code: https://github.com/Sp4zzy/Jbot-for-Discord/blob/master/README.md")
    if message.content.upper() == "!HELLO":
        await client.send_message(message.channel, ":wave: Sup dude. I'm a basic bot with some cool features here and there.  Use !help to see them!")
    if message.content.upper().startswith('!CLEAR'):
        log.write(getTime()+"!clear command issued by "+str(message.author)+"----"+str(message.content)+"===="+str(message.server))
        if message.author.server_permissions.administrator == True:
            try:
                m = str(message.content)
                number = int(m[7:])
                msg = []
                async for i in client.logs_from(message.channel, limit = number+1):
                    msg.append(i)
                await client.purge_from(message.channel, limit = number+1, check = is_pinned)#after = datetime.date(2018,6,1))
            except ValueError:
                await client.send_message(message.channel, "You didn't tell me how many to clear!")
        else:
            await client.send_message(message.channel, "You're not a Supreme Commander...")
    if message.content.upper().startswith('!PURGE'):
        log.write(getTime()+"!purge command issued by "+str(message.author)+"----"+str(message.content)+"===="+str(message.server))
        if message.author.server_permissions.administrator == True:
                await client.purge_from(message.channel, check = is_pinned)#after = datetime.date(2018,6,1))
        else:
            await client.send_message(message.channel, "You're not a Supreme Commander...")
            log.write(getTime()+"!purge command failed by "+str(message.author)+"----"+str(message.content)+"===="+str(message.server))
    if message.content.upper().startswith('!YT'):
        log.write(getTime()+"!yt command issued by "+str(message.author)+"----"+str(message.content)+"===="+str(message.server))
        try:
            try:
                vc = await client.join_voice_channel(message.author.voice_channel)
                player = await vc.create_ytdl_player(str(message.content)[4:])
                await client.send_message(message.channel, "Hey, I'm gonna play "+str(message.content)[4:]+" on the request of "+str(message.author))
                player.start()
            except discord.errors.InvalidArgument:
                await client.send_message(message.channel, "You're not in a voice channel!")
        except AttributeError:
            await client.send_message(message.channel, "You didn't give me a link to play...")
    if message.content.upper().startswith('!STOP'):
        log.write(getTime()+"!stop command issued by "+str(message.author)+"----"+str(message.content)+"===="+str(message.server))
        await client.send_message(message.channel, "пока!")
        #os.system("taskkill /f /im ffmpeg.exe")
        try:
            for x in client.voice_clients:
                if(x.server == message.server):
                    await x.disconnect()
        except RuntimeError:
            log.write(getTime()+"RuntimeError: dictionary changed size during iteration -- for x in client.voice_clients:")
    if "nikita" in message.content.lower():
        await client.send_message(message.channel, "<:IsThisA:451079458460532736> папа?")
    if "cheeki breeki" in message.content.lower():
        await client.send_message(message.channel, "<:cheeki:400365545385361408> А ну, чики-брики и в дамки! One two, you're on top! <:breeki:400367609402490890>")
    if "cyka blyat" in message.content.lower():
        await client.send_message(message.channel, "<:scav:400367157361377300> приходите сюда мудак! (prikhodite syuda mudak)")
    if "i hate russians" in message.content.lower():
        await client.send_message(message.channel, "<:scav2:400367971115073537> трахать тебя мудак!")
    if "fuck fuck" in message.content.lower():
        await client.send_message(message.channel, "Нахуя дахуя нахуярил? Выхуяривай нахуй")
    log.close()


client.run("----")

