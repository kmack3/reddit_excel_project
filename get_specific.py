import praw
import pprint

authors = open("authors.txt", 'w')
comments = open("comments.txt", 'w')
upvotes = open("upvotes.txt", 'w')

reddit = praw.Reddit(client_id='2YtQ3LoT3ImDnQ',
                     client_secret='0AmQwHwHO2SByypfkmE6vh4MMsI',
                     user_agent='Excel Scraping')


submission = reddit.submission(id='6it6pf')
print(submission.title) # to make it non-lazy
print(submission.url) 
# pprint.pprint(vars(submission))
