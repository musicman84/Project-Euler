#Task:
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import primes
num=600851475143
#Pfactors (within primes modules) creates an ordered list of
#prime factors, last entry is solution
print(primes.Pfactors(num)[-1])
