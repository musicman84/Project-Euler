#Task:
#A palindromic number reads the same both ways. The largest palindrome made
#from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

import palindromenum
a=1000
amax=0
bmax=0
maxpal=0

for a in range(999,0,-1):
        for b in range(999,0,-1):
                if palindromenum.pal(a*b):
                        if (a*b)>maxpal:
                                maxpal=a*b
                                amax=a
                                bmax=b
                        break #end inner loop when first palindrome is found
print(amax)
print(bmax)
print("Result = ",maxpal)
