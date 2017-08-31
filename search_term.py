import praw

term = "big"
terms = "scalability_terms.txt" # list of terms to search in the excel subreddit
before = 1495612800 # time we got irb approval
file_path = "scalability_posts/"
max_posts = 100 # maximum number of posts that will be collected
				# from one subreddit

# get list of all ones already scraped
already_pulled = []
#for filename in open("already_pulled.txt"):
#    already_pulled.append(filename)

reddit = praw.Reddit(client_id='2YtQ3LoT3ImDnQ',
                     client_secret='0AmQwHwHO2SByypfkmE6vh4MMsI',
                     user_agent='Excel Scraping')

posts = reddit.subreddit('excel').search(term)
count = 0
for submission in posts:
	if (count < max_posts and ((submission.id + ".txt") not in already_pulled)):
		print((str(count)) + " " + submission.id)
		count+=1
		submission.comments.replace_more(limit=0)
		f = open(file_path + submission.id + ".txt", 'w')
		f.write(term + "\n")
		f.write(str(submission.id) + '\n')
		f.write(submission.title + '\n\n')
		f.write(submission.selftext)
		f.write("\n\n\n")
		all_comments = submission.comments.list()
		comment_count = 0
		for comment in all_comments:
		    f.write("-------------\n" + comment.body + '\n')
		f.close()
