import os

dirs = ["all/", "random_posts_one/", "random_posts_two/"]
scale_posts = []

for word in open("scale_posts.txt", 'r'):
    scale_posts.append(word[0:-1])

print(scale_posts)

for dirc in dirs:
    print(dirc)
    for filename in os.listdir(dirc):
        if filename[0] != '.' and filename in scale_posts:
            print('cp ' + str(dirc) + filename + ' scale/' + filename)
            os.system('cp ' + str(dirc) +  filename + ' scale/' + filename)
