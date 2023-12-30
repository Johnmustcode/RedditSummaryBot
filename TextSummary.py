import praw
import os
from openai import OpenAI

from dotenv import load_dotenv


load_dotenv() # load .env file in current library
reddit = praw.Reddit('Text Summary Bot')
subreddit  = reddit.subreddit("brisbane")
valid_post_num  = 0 # check valid post number
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
)

# for submission in subreddit.hot(limit=5):
#     print("Title: ",submission.title)
#     print("SelfText: ", submission.selftext)
#     print("Score: ",submission.score)
#     print("---------------------------------------")


# go over hot posts in subreddit
for submission in subreddit.hot(limit=8): # 10 post now
    if valid_post_num >= 5:
        break
    # print("Processing submission:", submission.title)
    # print("Processed text: ", submission.selftext)
    # print(submission)
    # print("---------------------------------------")
    # print("\n")
    # initial prompt


    prompt = """Here is a piece of text: ###{}###. 
    Please summarize it and provide useful information,
    if the post is identified as a useless information, reply like: "no".
    if no useful information, it's useless.
    if the post include information like ###&#x200B###, it's useless.
    if the post is calling for comments or feedback, it's useless.
    if the post provide no useful information, it's useless.""".format(submission.selftext[:500])

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
    gpt_response = response.choices[0].message.content.strip().lower()
    if gpt_response.startswith("no") or gpt_response.replace('.', '') == "no":
        print("Received 'No' response, skipping to next post...")
    else:
        valid_post_num += 1
        print(gpt_response)
        print("----------------------------")

# Further update
# GPT loop, further filter?
# other platform?
