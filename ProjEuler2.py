#Task:
#By considering the terms in the Fibonacci sequence whose values
#do not exceed four million, find the sum of the even-valued terms.

#initialise seq.
t0=1
t1=0

total=0

while (t0+t1)<4000000.0:#t0+t1 is next term in Seq.
        for i in range(3):#logic shows every 3rd entry (and no others) of Fib. Seq. are even
            #standard Fib Seq calculation
                t2=t0+t1
                t0=t1
                t1=t2
        print(t2)
        total+=t2
print('solution = ',total)

