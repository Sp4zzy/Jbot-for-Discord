## 10/15/18

Sup, so this is just gonna be a blog-style post for Jbot's development to keep people informed (assuming anyone cares).

So with the !requestfeature command I've gotten a lot of good suggestions for improvements & features for Jbot.  My current list of "things to do"
is as follows:

* Add/remove/change emojis commands
* Rolls needs updating to new format / layout
* Allow server admins to change Jbot's command prefix at whim, essentially !, @, #, $, etc.
* Add some games to Jbot (quiz / trivia maybe?)

That's listed from high -> low priority, but will be completed in any order.

The add/remove/change emojis command will be done with:

create_custom_emoji(server, *, name, image)
delete_custom_emoji(emoji)
edit_custom_emoji(emoji, *, name)

Which will allow people with the proper group for the server to add emojis via a URL (I believe).

New Rolls is something that D&D Bot & Jbot will use, which is essentially a TIMESdSIDES, so 1d20 is 1 20 sided dice roll.  This will allow
people to roll multiple dice, at the same time and still select the number of sides.  Although this feature is largely unused on Jbot,
it will be a useful addition to D&D Bot, and since Jbot already has a !roll command, I mine as well give it to both of them.

Allowing server admins to change command prefix, is a bit of a tall order.  The way I have Jbot's commands structured is pretty $#!+.  I've
been working on a re-write using discord.py 1.0.0a but haven't made too much progress.  I have some ideas about how this can be done
though without the rewrite, and will work on this pretty soon, since this feature has been requested for both Jbot & D&D Bot.

As for the games, feel free to give me some suggestions using !featurerequest.  I have some ideas for how I could do a TicTacToe game, trivia
and others.  It might be a fun little side project for Jbot to have some small games here and there.

That sums it up for now.  Back to work!
