import praw
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # load .env file in current library
reddit = praw.Reddit('Text Summary Bot')
subreddit  = reddit.subreddit("brisbane")

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
)

# for submission in subreddit.hot(limit=5):
#     print("Title: ",submission.title)
#     print("SelfText: ", submission.selftext)
#     print("Score: ",submission.score)
#     print("---------------------------------------")


# go over hot posts in subreddit
for submission in subreddit.hot(limit=2):
    print("Processing submission:", submission.title)
    print("Processed text: ", submission.selftext)
    print(submission)
    print("---------------------------------------")
    print("\n")
    # initial prompt
    prompt = "Here is a piece of text: '{}'. Please summarize it and provide useful information, if no useful information just reply no.".format(submission.selftext[:500])

    # sending prompt to gpt model
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4",
        stream=False,
    )

    # print the response from the gpt
    print(response.choices[0].message.content)
    print("---------------------------------------")

# Further update
# If the post simply includes video, ignore it, read next post
# IF the post provides no useful information, read next post