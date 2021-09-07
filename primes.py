#Module containing prime number functions
#Written my Kevin Mason

import math
#calculates all prime numbers below n
def primesieve(n):
        n=int(n.real)#ensure input is an int
        #pick up input that is 0 or less and give empty array as output
        if n<=0:
            return([])
        
        a=[0]*(n+1)#create empty array
        for i in range(n+1):
                a[i]=i
        #a is array [0,1,2,3....n]
        a[0]=0#0 and 1 are not primes
        a[1]=0
        p=2#first prime
        while p**2<=n:
                j=p**2#sufficient to start from p^2
                #remove mulitples of p from list (a)
                while j<=n:
                        a[j]=0
                        j+=p
                p+=1

        #remove empty
        b=[]
        for i in range(n+1):
                if a[i]>0:
                        b.append(a[i])
        return(b)


#creates list of prime factors
def Pfactors(num):
        num=int(num.real)#ensure input is an int
        #pick up input that is 0 or less and give empty array as output
        if num<=0:
            return([])
        
        factorspassone=[]
        factors=[]
        SRnum=int(math.sqrt(num))

        prime=primesieve(SRnum)#create list of primes up to and including SRnum
        #find primes which are factors of num
        for i in prime:
                if num%i==0:
                        factorspassone.append(i)

        #Divide through by Primes found so far
        #Gives order of primes and remainder prime
        for i in factorspassone:
                while num%i==0:
                        num/=i
                        factors.append(i)
        if num!=1:
                factors.append(int(num))
        return(factors)
        
#checks if number is prime, returns true if it is
def isPrime(n):
        n=int(n.real)#ensure input is an int
        #pick up input that is 0 or less and return false
        if n<=0:
            return(False)
        sqrtnum=int(math.sqrt(n))
        primes=primesieve(sqrtnum)
        for i in primes:
                if n%i==0:
                        return(False)
        return True

