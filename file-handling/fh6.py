f= open("message3.txt", "r+")
for line in f.readlines():
    print(line)
f.close()
