# Jbot-for-Discord
Jbot is a very basic discord bot, meant to be modified and changed to your own needs.  You will need your own server / computer to run the bot.  If you need help modifying let me know, and I will help as much as I can.  Seriously, just leave me a comment or get in touch with me somehow.  I love coding and am always looking for new projects.

!help -- gives list of all possible commands

!yt [link] -- plays a youtube link

!stop -- stops youtube link playback

!youcango -- makes bot leave playback voice channel

!purge -- removes all non-pinned messages in a channel (Admin command)

!clear X -- removes X amount of messages from a channel (Admin command)

!remindme [time] [d,h,m,s (time type)] [note] -- Sends a message in the "reminder" channel (Will need to specify in your own code) after a certain time designated by user.  (supports days, hours, minutes, and seconds)

- EX: !remindme 5 h Add persistent storage
- EX2: !remindme 300 d This reminder is gonna take a while
- EX3: !remindme 500 d Why?
- EX4: !remindme 5 s peabrain
- EX5: !remindme 5 m Get food

!remindother -- !remindother [time] [dhms] [othername] [note]

- EX: !remindother 5 d sp4zzy Add more bot commands!

!announce -- !announce [time] [dhms] [note]

- EX: !announce 1 h Server restarting now!

!hello -- basic information

!ping -- tests that the bot is working

More to come, open to suggestions.

FUTURE TODO:

- Multiple files for easy reading
- More comments for easier implementation of code to other projects.
- Error handling on !yt and other commands
- Check if message is from bot itself to prevent shit like this https://i.imgur.com/R9v4Hyg.png
