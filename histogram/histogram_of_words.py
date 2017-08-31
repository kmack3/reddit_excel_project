import os
import string
from operator import itemgetter

stop = "stop_words.txt" # words to be removed from posts
out = "10_scalability_posts.txt" # output file
path = './small_scalability_posts/' # path to posts
top_x = 50 # how many words do you want to get

stopwords = []
freq = {}

# get list of stopwords
for line in open(stop):
    for word in line.split():
        word = (''.join(c for c in word if c not in string.punctuation))
        stopwords.append(word)

# get frequency counts of words in posts
count = 1
for filename in os.listdir(path):
    print("Processing file " + str(count))
    count += 1
    for line in open(path+filename):
        for word in line.split():
            # remove punctuation
            word = str((''.join(c for c in word if c not in string.punctuation)))
            word = word.lower()
            if word not in stopwords:
                if word not in freq:
                    freq[word]=0
                freq[word]+=1


# write most common words to file

sortedlist = sorted(freq.items(), key=lambda x:x[1], reverse=True)

count = 0
fout = open(out, 'w')

for key,val  in sortedlist:
    if count < top_x:
        fout.write(str(key) + " " + str(val)+ '\n')
        count += 1

fout.close()
