# Jbot-for-Discord
Jbot is a very basic discord bot, meant to be modified and changed to your own needs.  You will need your own server / computer to run the bot.  If you need help modifying let me know, and I will help as much as I can.  Seriously, just leave me a comment or get in touch with me somehow.  I love coding and am always looking for new projects.

# Adding Jbot to your discord

Jbot can be added by going to this link: https://discordbots.org/bot/454730166816604180

The Jbot support discord can be joined here: https://discord.gg/BgWqV6F -- This will allow you to get in touch with me for assistance, feature requests, and anything else you might need related to this project.

This bot requires you to give it a group to work.  If you want to use the admin commands, make sure it has administrative privilege.
I don't have it auto-generating a group because 1. I just haven't done it yet, and 2. some people might not want the bot to have admin access, so you can limit it's ability to function based on the group you give it.

# Jbot's current commands

!help -- gives list of all possible commands

!yt [link] -- plays a youtube link

!stop -- stops youtube link playback & makes bot leave channel -- Having this & !youcango caused bot to hang around in voice channel after playback was stopped, and made it impossible to start a new playback.

~~!youcango -- makes bot leave playback voice channel~~

!purge -- removes all non-pinned messages in a channel (Admin command)

!clear X -- removes X amount of messages from a channel (Admin command)

!remindme [time] [d,h,m,s (time type)] [note] -- Sends a message in the "reminder" channel (Will need to specify in your own code) after a certain time designated by user.  (supports days, hours, minutes, and seconds, this is PERSISTENT NOW)

- EX: !remindme 5 h Code something useful!
- EX2: !remindme 300 d This reminder is gonna take a while
- EX3: !remindme 500 d Why?
- EX4: !remindme 5 s peabrain
- EX5: !remindme 5 m Get food

!remindother -- !remindother [time] [dhms] [othername] [note] -- (Admin command)

- EX: !remindother 5 d sp4zzy Add more bot commands!

!announce -- !announce [time] [dhms] [channel] [note] -- (Admin command)

- EX: !announce 1 h announcements Server restarting now!

!hello -- basic information

~~!ping -- tests that the bot is working~~ -- No longer needed, use !hello to check if bot works

!checkadmin -- Lets user know whether or not they're admin and can run certain commands the bot allows.

!alexjones -- Jbot will join your voice channel and play a random Alex Jones rant / freakout, because who doesn't love an Alex Jones rant?

!roll [sides] -- Jbot  rolls a dice for you! Try to get a nat 20!

Some other kinda-secret admin ones that I haven't updated this page with, (assuming you're just adding him to your server, ask me about them so you can potentially mess with your discord patrons)

More to come, open to suggestions.

FUTURE TODO:

- Multiple files for easy reading
- More comments for easier implementation of code to other projects.
- Check if message is from bot itself to prevent shit like this https://i.imgur.com/R9v4Hyg.png

# Legal Disclaimer Surrounding GDPR

By using this bot on your server, you should be made aware that I am logging when commands are done through the bot.  The exact log is as follows: 

[HH:MM:SS] COMMAND TYPE issued by USER ---- FULL COMMAND TYPED (including invalid syntax) ==== SERVER NAME

So for example, this command: "!yt https://www.youtube.com/watch?v=iywaBOMvYLI"

Is logged as such: "[15:33:28] !yt command issued by AmericanLegend#6969 ---- !yt https://www.youtube.com/watch?v=iywaBOMvYLI ==== Jbot Support"

This information is purely for diagnostic use to debug errors that occur during run-time.  So if a user says "Hey, I used the !remindme command and it never reminded me!" I can get specific information, check the logs, and see what went wrong.

I do not distribute, sell, or use this information for anything else.  If you have any issues with this, don't use the bot.
