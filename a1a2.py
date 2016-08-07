a1=(map(int,raw_input("Enter values of set a1 seperated by blankspaces").strip().split()))
a2=(map(int,raw_input("Enter values of set a2 seperated by blankspaces").strip().split()))

count=0
for value in a1:
    if value in a2:
        count+=1
if count==len(a1):
    print "a1 is subset of a2"
else:
    print "a1 is not a subset of a2"

