import praw

reddit = praw.Reddit('Text Summary Bot')
subreddit  = reddit.subreddit("fo4")
for submission in subreddit.hot(limit=5):
    print("Title: ",submission.title)
    print("SelfText: ", submission.selftext)
    print("Score: ",submission.score)
    print("---------------------------------------")
