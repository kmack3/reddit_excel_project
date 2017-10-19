import praw
import time

path = "junk/"
start = time.time()
reddit = praw.Reddit(client_id='2YtQ3LoT3ImDnQ',
                     client_secret='0AmQwHwHO2SByypfkmE6vh4MMsI',
                     user_agent='Excel Scraping')


count = 0
while (count <= 1600):
	submission = reddit.subreddit('excel').random()
	# print(submission.created)
	print(count)
	count+=1
	submission.comments.replace_more(limit=0)
	f = open(path + submission.id + ".txt", 'w')
	f.write(str(submission.id) + '\n')
	f.write(submission.title + '\n')
	f.write(submission.selftext)
	f.write("\n\n\n")
	all_comments = submission.comments.list()
	comment_count = 0
	for comment in all_comments:
		#comment_count = comment_count + 1
	    f.write("-------------\n" + comment.body + '\n')
	f.close()

end = time.time()
print (end - start)
