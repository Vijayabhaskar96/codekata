num=map(int,raw_input("Enter a number"))
sumofnum=str(sum(num))
revofsum=list(reversed(sumofnum))
if list(sumofnum)==revofsum:
    print "Sum of the given number is a palindrome"
else:
    print "Not Palindrome"
