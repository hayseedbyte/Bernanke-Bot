from BotConfig import *
# BotSecret contains passwords, client id, client secret, and user agent
from BotSecret import *
import praw
import sys


def summoned_reply(comment):
    submission = comment.submission
    print(submission)
    submission.reply(bot_reply)


r = praw.Reddit(client_id=client_id,
                client_secret=client_secret,
                username=username,
                password=password,
                user_agent=user_agent)

messages = r.inbox.stream()
for message in messages:
    try:
        if message in r.inbox.mentions() and message in r.inbox.unread():
            summoned_reply(message)
            message.mark_read()
    except praw.exceptions.APIException:
        print("error")
