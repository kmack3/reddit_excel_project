import os
# dirs = ["test/"]
dirs = ["all/", "random_posts_one/", "random_posts_two/"]

# computes number of unique authors 
def count_authors():
    allauthors = []
    authors = open("authors.txt", 'r')
    for author in authors:
        for word in author.split():
            print(word)
            if word != '\n':
                allauthors.append(word)
                break
    print("Num unique authors: " + str(len(set(allauthors))))

# computes number of authors called "None" 
def count_none_authors():
    count = 0
    authors = open("authors.txt", 'r')
    for author in authors:
        for word in author.split():
            print(word)
            if word != '\n':
                if word == "None":
                    count += 1
    print("Num none authors: " + str(count))

# computes average upvote percentage
def avg_upvote():
    totalpercentages = 0
    totalfiles = 0
    percentages = open("upvotes.txt", 'r')
    for percent in percentages:
        for word in percent.split():
            totalpercentages += float(word)
            totalfiles += 1
            break
    print("Avg upvote percentage: " + str(float(totalpercentages)/totalfiles))

#computes num posts that metion databases 
def count_db():
    dbwords = ["Access", "database", "databases", "Database", "Databases", "SQL", "sql", "Sql"]
    totaldb = 0
    for dirc in dirs:
        print(dirc)
        for filename in os.listdir(dirc):
            linenum = 1
            stop = False
            print(filename)
            if (filename[0] == '.'):
                continue
            for line in open(dirc + filename, 'r'):
                for word in line.split():
                    if word in dbwords:
                        totaldb+=1
                        stop = True
                        break
                if stop:
                    break;
    print("Num referencing db: " + str(totaldb))


# computes nubmer of posts where poster selected "solution verified"
def count_solved():
    totalsolved = 0
    for dirc in dirs:
        print(dirc)
        for filename in os.listdir(dirc):
            print(filename)
            if (filename[0] == '.'):
                continue
            for line in open(dirc + filename, 'r'):
                words =line.split()
                if ("Solution" in words) and ("Verified" in words):
                    totalsolved += 1
                    break
    print("Num solved: " + str(totalsolved))



#computes num posts that received an answer
def count_answered():
    totalanswered = 0
    totalfiles = 0
    for dirc in dirs:
        print(dirc)
        for filename in os.listdir(dirc):
            linenum = 1
            stop = False
            check = False
            print(filename)
            if (filename[0] == '.'):
                continue
            for line in open(dirc + filename, 'r'):
                for word in line.split():   # only get here if line has at least one word
                    if check:
                        print(word)
                        if not word == "Hi!":
                            totalanswered+=1
                        stop = True
                        break
                    if word == "-------------":
                        check = True
                if stop:
                    break;
            totalfiles+=1
    print("Num answered: " + str(totalanswered))
    print("Num not answered: " + str(totalfiles-totalanswered))


# computes average number of words per post
def count_words():
    totalwords = 0
    totalfiles = 0
    for dirc in dirs:
        print(dirc)
        for filename in os.listdir(dirc):
            linenum = 1
            numwords = 0
            stop = False
            print(filename)
            if (filename[0] == '.'):
                continue
            for line in open(dirc + filename, 'r'):
                if linenum >= 3:
                    for word in line.split():
                        if word == "-------------":
                            stop = True
                        else:
                            numwords+=1
                if stop:
                    break;
                linenum+=1
            totalwords = totalwords + numwords
            totalfiles+=1
    print("Avg words: " + str(float(totalwords)/totalfiles))


count_none_authors()

## computes average number of comments
#def count_comments():
#    totalcomments = 0
#    totalfiles = 0
#    for dirc in dirs:
#        print(dirc)
#        for filename in os.listdir(dirc):
#            linenum = 1
#            numcomments = 0
#            stop = False
#            print(filename)
#            if (filename[0] == '.'):
#                continue
#            for line in open(dirc + filename, 'r'):
#                for word in line.split():
#                    if word == "-------------":
#                        numcomments+=1
#            totalcomments = totalcomments + numcomments
#            totalfiles+=1
#    print("Avg comments: " + str(float(totalcomments)/totalfiles))
