'''
Created on Nov 25, 2018

@author: themagicbean (Miseong Kong)

Wall of Text Bot 0.01

'''

import praw
# import pdb was in guide file but not used
# import re was in  guide script also not used 
import os
import datetime
import ctypes

import nltk
#nltk.download("punkt")

MessageBox = ctypes.windll.user32.MessageBoxW
r = praw.Reddit('bot1')
now = str(datetime.datetime.now())
thepath = r'C:\Users\Darren\Documents\LiClipse Workspace\Wall_of_Text_Bot'
print(thepath)
os.chdir(thepath)

if not os.path.isfile('posts_replied_to.txt'):
	posts_replied_to = []
	print("Did't have initial replied to file")
	#working
	
else:
	with open('posts_replied_to.txt') as f:
		# needed to add variable f for subsequent lines
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split('\n')
		posts_replied_to = list(filter(None, posts_replied_to))
	#print("Opened the reply file.")
	#working

if not os.path.isfile('bot_runtimes.txt'):
	bot_runtimes = []
	#print("Did't have bot runtimes file")
	#working
	
else:
	with open('bot_runtimes.txt') as f:
		# needed to add variable f for subsequent lines
		bot_runtimes = f.read()
		bot_runtimes = bot_runtimes.split('\n')
		bot_runtimes= list(filter(None, bot_runtimes))
		#print("Opened the runtime file.")
		
	with open('bot_runtimes.txt', 'a') as f:   
		#print(now)
		f.write(now + '\n')
		#print("Wrote new run time to the file")

subreddit = r.subreddit('All')
for submission in subreddit.hot(limit=250):
	if submission.id not in posts_replied_to:
		# print ("Sub ID not in replied file.")
			
		data = submission.selftext
		words = data.split(" ")
		numwords = len(words)
		lines = data.split("\n")
		numlines = len(lines)
					
		if numwords > 100 and numlines == 1:
			submission.reply("""Hello, I couldn't help but notice that your submission is a very long paragraph.  Unfortunately, text without paragraph breaks, like yours, is very hard to read.
	To help more people read and enjoy your text, please use more paragraph (line) breaks.  If you're not sure where to put them, here are some good resources:

https://www2.open.ac.uk/students/skillsforstudy/dividing-your-work-into-paragraphs.php
http://www.saidsimple.com/content/100835/
http://apps.prsa.org/intelligence/tactics/articles/view/10215/1078/cut_it_down_readers_skip_long_paragraphs#.xbwhavlkjiu

Beep boop.  I'm a bot.  If you think this was in error, you can message me.  I'll probably ignore it.  Beep boop.
				""")
			#print('Bot replying type 1 to: ', submission.title)
			posts_replied_to.append(submission.id)
			MessageBox(None, 'New Type 1 Reply', 'Message', 0)
			with open('posts_replied_to.txt', 'w') as f:
				for post_id in posts_replied_to:
					f.write(post_id + '\n')
					f.write(post_id + ' type 1' + '\n')
				
		else:
			for l in lines:
				wordsperline = len(l.split(" "))
				sentencesnltk = len(nltk.sent_tokenize(l))
			
				if wordsperline > 500 or sentencesnltk > 10:
					submission.reply("""Hello, I couldn't help but notice that at least one of your paragraphs is very long.  Unfortunately, text without paragraph breaks, like yours, is very hard to read.
	To help more people read and enjoy your text, please use more paragraph (line) breaks.  If you're not sure where to put them, here are some good resources:

https://www2.open.ac.uk/students/skillsforstudy/dividing-your-work-into-paragraphs.php
http://www.saidsimple.com/content/100835/
http://apps.prsa.org/intelligence/tactics/articles/view/10215/1078/cut_it_down_readers_skip_long_paragraphs#.xbwhavlkjiu

Beep boop.  I'm a bot.  If you think this was in error, you can message me.  I'll probably ignore it.  Beep boop.
				""")
					
					#print('Bot replying type 2 to: ', submission.title)
					posts_replied_to.append(submission.id)
					MessageBox(None, 'New Type 2 Reply', 'Message', 0)
					with open('posts_replied_to.txt', 'w') as f:
						for post_id in posts_replied_to:
							f.write(post_id + '\n')
							f.write(post_id + ' type 2' + '\n')
			

