for i in range(1,10,2):
    print(i)
print("loop with starting and ending point only")
for i in range(1,10):
    print(i)
print("loop with one point ")
for i in range (10):
    print(i)
    print("while loop")
    i=0
    while i<5:
        print(i)
        i=i+1
    print("nested loop ")
    for i in range (1,5):
        for j in range (1,4):
            print(i," ",j)