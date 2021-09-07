#Task:
#Find the sum of all the primes below two million.

import primes
primelist=primes.primesieve(2000000)
length=len(primelist)
sum=0
for i in primelist:
        sum+=i
print('solution = ',sum)

