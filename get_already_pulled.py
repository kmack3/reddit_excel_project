import os

folders = [
            "forever",
            "large",
            "freeze",
            "crash",
            "slow",
            "lag",
            "long_time",
            "big",
          ]
f = open("already_pulled.txt", 'w')

for folder in folders:
    print(folder)
    for filename in os.listdir("scalability_posts/"+folder+"/"):
        if ('.txt' in filename):
            print(filename)
            f.write(str(filename) + '\n')

f.close()
