# this script looks through the posts in the given file and pulls out those that use a certain number of the stop words
# returns a list of filenames of relevant files

import os
import string


stop = "stop.txt"
path = './lag_posts/'

stopfactor = 0

fout = open("relevant_lag.txt", 'w')

stopwords = []
# get list of stopwords
for line in open(stop):
    for word in line.split():
        stopwords.append(word)

print(stopwords)
# start searching files
for filename in os.listdir(path):
    count = 0
    for line in open(path+filename):
        for word in line.split():
            word = (''.join(c for c in word if c not in string.punctuation))
            if word in stopwords:
                count+=1
    if (count > stopfactor):
        fout.write(filename + '\n')
    print(count)

fout.close()
