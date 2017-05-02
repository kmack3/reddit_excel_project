import praw

reddit = praw.Reddit(client_id='2YtQ3LoT3ImDnQ',
                     client_secret='0AmQwHwHO2SByypfkmE6vh4MMsI',
                     user_agent='Excel Scraping')

for submission in reddit.subreddit('excel').hot(limit=1):
    print(submission.title)
#    submission.comments.replace_more(limit=10)
#    for top_level in submission.comments:
#        print(top_level.body)
    all_comments = submission.comments.list()
    for comment in all_comments:
        print(comment.body)
