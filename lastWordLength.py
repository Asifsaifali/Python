def lengthOfLastWord( s) :
        s = s.rstrip()
        x = s.split(" ")
        return len(x[-1])

x = lengthOfLastWord("Hello world")
print(x)