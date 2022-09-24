from BotConfig import *
# BotSecret contains passwords, client id, client secret, and user agent
from BotSecret import *
import praw
import sys

amounts = {'million', 'billion', 'trillion'}
currency = {'$', 'dollars', 'usd'}
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)
numFound = 0
subreddit = reddit.subreddit('boringdystopia+bottesting')

for submission in subreddit.stream.submissions():
    x_title = submission.title.lower()
    for i in amounts:  # goes through our keywords
        if i in x_title:
            for j in currency:
                if j in x_title:
                    with open(linuxFile) as f:
                        commented = f.readlines()
                        subid = submission.id
                        flag = 0
                        index = 0
                        for line in commented:
                            index += 1

                        # checking string is present in line or not
                            if subid in line:
                                flag = 1
                                print('Commented already.')
                                break

                    # checking condition for string found or not
                        if flag == 0:
                            numFound = numFound + 1
                            print('Bot replying to: ')
                            print(submission.title)
                            submission.reply(bot_reply)
                            with open(linuxFile, 'a') as g:
                                g.writelines(
                                    subid + '\n')
                            break
