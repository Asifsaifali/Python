def isPalindrome(x):
        x=str(x)
        if int(x)<0:
            return False
        elif x[0:]==x[-1::-1]:
            return True    
        else:
            return False    
    

print(isPalindrome(1221))