import os
print("auto close one")
with open("science-notes.txt","r")as f:
    for line in f:
        print(line.strip())

print()
print("word count")
with open ("science-notes.txt","r")as f:
    for line in f:
        words = line.split()
        print(len(words),"words - >",line.strip())
print()
print("merging the notes")
if os.path.exists("all-notes.txt"):
     print("all-notes.txt already exsit- overwriting")
else:
    print("file doesn't found - creating now")
if os.path.exists("file.txt"):
    os.remove("file.txt")
    print("file file is removed ")
else:
    print("file file doesn't exist")