import praw
import pprint

reddit = praw.Reddit(client_id='2YtQ3LoT3ImDnQ',
                     client_secret='0AmQwHwHO2SByypfkmE6vh4MMsI',
                     user_agent='Excel Scraping')


submission = reddit.submission(id='4usd8o')
print(submission.title) # to make it non-lazy
pprint.pprint(vars(submission))
pprint.pprint(vars(submission._comments))

#comment = reddit.comment(id='ctd5ycu')
#pprint.pprint(vars(comment))


#submission.comments.replace_more(limit=0)
#comment_queue = submission.comments[:]  # Seed with top-level
#print(comment_queue)
#while comment_queue:
#        comment = comment_queue.pop(0)
#        comment_queue.extend(comment.replies)
#        print(comment.replies)
