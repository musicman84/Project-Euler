def pal(n):
        n_string=str(n)
        L=len(n_string)

        for i in range(int(L/2)):
                if n_string[i]!=n_string[L-i-1]:
                        return (False)
        
        return(True)    
