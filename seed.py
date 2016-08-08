x=int(raw_input())
num=list(str(x))
seed=x
for i in num:
    seed=seed*int(i)
print "seed of",x,"is",seed
