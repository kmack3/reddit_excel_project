import praw

path = "lag_posts/"
# "posts/"
reddit = praw.Reddit(client_id='2YtQ3LoT3ImDnQ',
                     client_secret='0AmQwHwHO2SByypfkmE6vh4MMsI',
                     user_agent='Excel Scraping')

posts = reddit.subreddit('excel').search('lag')
# reddit.subreddit('excel').hot(limit=100):

for submission in posts:
    f = open(path + submission.id + ".txt", 'w')
    f.write(submission.title + '\n')
    all_comments = submission.comments.list()
    for comment in all_comments:
        f.write(comment.body + '\n')
    f.close()
