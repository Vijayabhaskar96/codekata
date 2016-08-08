a=list()
print "Enter the size of the array"
N=int(raw_input())
print "Enter ",N," elements of the array"
for i in range(N):
    element=int(raw_input())
    a.append(element)
for i in reversed(sorted(a)):
    print i
