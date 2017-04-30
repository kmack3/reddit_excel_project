import praw

reddit = praw.Reddit(client_id='2YtQ3LoT3ImDnQ',
                     client_secret='0AmQwHwHO2SByypfkmE6vh4MMsI',
                     user_agent='Excel Scraping')

for submission in reddit.subreddit('excel').hot(limit=10):
    print(submission.title)
