Wall of Text Bot Readme

Miseong Kong (themagicbean) 2018 / GPL 3.0

Tired of reading posts that just go on and on, without any visual break?

On mobile, you keep scrolling down, and it just ... keeps going.  Like, do people not know where their enter keys are?

This bot is here to help.

Bot scans hot posts to Reddit, finds those with excessive sentences per paragraph and comments.

Depends on NLTK and PRAW in addition to standard Python libraries (os, datetime)

Bot file does not include Praw.ini file.  You must add a Bot1 to the praw.ini file and place it in the proper location.
https://www.pythonforengineers.com/build-a-reddit-bot-part-1/
Location: Ususally next to the bot file.  For me, I also added it to appdata/roaming as PRAW looks there for the .ini file.

Running: Windows Task Scheduler:
Set timing as you please and run python.exe with the argument being the bot file location.

Known issue:
Bot will comment on the same post multiple times.  I decided to just label this a feature instead of a bug.  Two reasons:
(1)  I haven't figured out how to fix it, and I want to be done with this project.
(2)  If you type a wall of text, then ignore a bot telling you that you typed a wall of text, you deserve another bot comment.


