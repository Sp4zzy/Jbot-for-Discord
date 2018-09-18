# Jbot-for-Discord
Jbot is a very basic discord bot, meant to be modified and changed to your own needs.  You will need your own server / computer to run the bot.  If you need help modifying let me know, and I will help as much as I can.  Seriously, just leave me a comment or get in touch with me somehow.  I love coding and am always looking for new projects.

# Adding Jbot to your discord

Jbot can be added by going to this link: https://discordbots.org/bot/454730166816604180

The Jbot support discord can be joined here: https://discord.gg/BgWqV6F -- This will allow you to get in touch with me for assistance, feature requests, and anything else you might need related to this project.

This bot has various commands requiring various levels of power.  (Admin command) denotes a command only people with the admin permission can use.  See-> https://i.imgur.com/unQfmf0.png
To check if you have the ability to run those commands, use !checkadmin

Permissions for Jbot himself are listed as (Jbot needs .... )

# Jbot's current commands

!help -- gives list of all possible commands (Jbot needs message permissions)

!8ball [question] -- gives you an answer to a yes or no question

!bsgtime [number] [day/hour/min/whatever] [OPTIONAL: item they're promising in that timeframe] -- joke command

!valvetime [number] [day/hour/min/whatever] [OPTIONAL: item they're promising in that timeframe] -- joke command

!yt [link] -- plays a youtube link (Jbot needs voice channel join power)

!active & !inactve -- if you have a tag for "active" users on your server, you can have jbot assign and unassign that tag.  This is useful for gaming servers, where you might want to be pingable by other people, or maybe not pingable.  In the future, I will make it possible to assign your own custom server-role for this.

!stop -- stops youtube link playback & makes bot leave channel -- Having this & !youcango caused bot to hang around in voice channel after playback was stopped, and made it impossible to start a new playback. 

~~!youcango -- makes bot leave playback voice channel~~

!purge -- removes all non-pinned messages in a channel (Admin command) / (Jbot needs message deleting permissions)

!clear [number] -- removes that number of messages from a channel (Admin command) / (Jbot needs message deleting permissions)

!remindme [time] [d,h,m,s (time type)] [note] -- Sends a message in the "reminder" channel (Will need to specify in your own code) after a certain time designated by user.  (supports days, hours, minutes, and seconds, this is PERSISTENT NOW) (Jbot needs message permissions and @)

- EX: !remindme 5 h Code something useful!
- EX2: !remindme 300 d This reminder is gonna take a while
- EX3: !remindme 500 d Why?
- EX4: !remindme 5 s peabrain
- EX5: !remindme 5 m Get food

!remindother -- !remindother [time] [dhms] [othername] [note] -- (Admin command) (Jbot needs message permissions and @)

- EX: !remindother 5 d sp4zzy Add more bot commands!

!announce -- !announce [time] [dhms] [channel] [note] -- (Admin command) (Jbot needs message permissions for channel needing announcement)

- EX: !announce 1 h announcements Server restarting now!

!hello -- basic information (Jbot needs message permissions)

~~!ping -- tests that the bot is working~~ -- No longer needed, use !hello to check if bot works

!checkadmin -- Lets user know whether or not they're admin and can run certain commands the bot allows. (Jbot needs message permissions)

!alexjones -- Jbot will join your voice channel and play a random Alex Jones rant / freakout, because who doesn't love an Alex Jones rant? (Jbot needs message permissions / voice channel join power)

!roll [sides] -- Jbot  rolls a dice for you! Try to get a nat 20! (Jbot needs message permissions)

!toto -- Be in a voice channel :)

Like alexa, Jbot can also "play despacito" if you want it to.

More to come, open to suggestions.

FUTURE TODO:

- Multiple files for easy reading
- More comments for easier implementation of code to other projects.

# Legal Disclaimer Surrounding GDPR

By using this bot on your server, you should be made aware that the bot has access to see EVERY message you send in ANY channel that it has access to.  All discord.py bots have this capability, and I am constantly updating my logging techniques to better handle bugs that occur.  If you are uncomfortable with that, you have the option of not using this bot.

**I do not distribute, sell, or use this information for anything other than debugging.**

Again, If you have any issues with this, don't use the bot, or contact me if you need clarification on what I'm logging.

# Recent Bot Breach & Safety Information When Using Bots

I stumbled upon a bot breach on reddit, where the bot in question went and deleted a bunch of server channels.  This breach occurred because the bot's token was publicly listed on it's github.  If you notice in Jbot's source code I **DO NOT** reveal the token.  I keep the token secure, and if I notice or even **suspect** it may have leaked, I change it.  I note next to all the commands what specific permissions Jbot needs to perform each.  Do not give him more than he needs!
