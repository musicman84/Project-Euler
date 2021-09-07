#Task:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

import time#used to benchmark code for speed
start=time.time()
sum=0
n=1
nterm=3
while nterm<1000.0:
        if (nterm%5)>0:#ensuring there is no overlap between sets
                sum+=nterm#sum all multiples of 3 (excluding multiples of 5)
        n+=1
        nterm=n*3
n=1
nterm=5
while nterm<1000.0:
        sum+=nterm#sum all multiples of 5
        n+=1
        nterm=n*5

print(sum)
elapsed=time.time()-start
print(elapsed)
