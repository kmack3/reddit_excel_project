import os
import string
from operator import itemgetter

stop = "stop_words.txt" # words to be removed from posts
out = "common.txt" # output file
path = './posts/' # path to posts
top_x = 1 # how many words do you want to get

stopwords = []
freq = {}

# get list of stopwords
for line in open(stop):
    for word in line.split():
        stopwords.append(word)

# get frequency counts of words in posts
for filename in os.listdir(path):
    for line in open(path+filename):
        for word in line.split():
            # remove punctuation
            word = (''.join(c for c in word if c not in string.punctuation))
            if word not in stopwords:
                if word not in freq:
                    freq[word]=0
                freq[word]+=1


# write most common words to file

count = 0
fout = open(out, 'w')
for key, value in sorted(freq.items(), key=itemgetter(1), reverse=True):
    if count < top_x:
        fout.write(key + " " + str(value)+ '\n')
        count += 1

fout.close()
