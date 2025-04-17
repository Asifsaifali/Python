# def fun():
#     print("this is the function")

# a = fun
# a()

a = {"this",  "that"}
b = {"that", "they"}
def fun(a,b):
    # a,b = b-a,a-b
    print(a-b)

# fun(a,b)

x =  ""
s =  "y"

y = ""
if x == "":
    print(s)
for i in x:
    for j in s:
        if i==j:
            continue
        else:
            y = j
print(y)