import os
import praw

dirs = ["all/", "random_posts_one/", "random_posts_two/"]
# dirs = ["test/"]

authors = open("authors.txt", 'w')
comments = open("comments.txt", 'w')
upvotes = open("upvotes.txt", 'w')

reddit = praw.Reddit(client_id='2YtQ3LoT3ImDnQ',
                     client_secret='0AmQwHwHO2SByypfkmE6vh4MMsI',
                     user_agent='Excel Scraping')


for dirc in dirs:
    print(dirc)
    count = 0
    for filename in os.listdir(dirc):
        if filename[0] != '.':
            filename = filename[0:-4]
            print(filename)
            submission = reddit.submission(id=filename)
            authors.write(str(submission.author) + '\n')
            comments.write(str(submission.num_comments) + '\n')
            upvotes.write(str(submission.upvote_ratio) + '\n')
        
