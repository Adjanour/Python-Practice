x = ["two","four"]
z = ["two","four"]

print(x == z)
print(x is z)
y = x

# "is" 

y.append(6)
print(y)
print(x)

fav = {"F":"afksdf","M":"sage"}
x = fav["F"]
fav["F"] = "illiac"

print(x)

# for x in range(0.5,5.5,0.5):
#     print(x)
    
print("two" in x)


# print(1 +2 +"3")

x = {"heads":[7,5],"tails":[2]}
x["heads"] = x["tails"]
x["tails"].append(9)
print(x)

# range object does not support object item assignment

x = range(5)
# print(x)
# y = x[1:4]
# x[2] = -1
# print(y)
# # x = x + y
# # print(x)


s = "abcde"
# t = s.substring(2,4)
# nothing like substring on str object, ie attribute error

# t[0] = "Z"
# x = s + t
# print(x)

def s(n):
    return n * n
t = 0
for n in [1,3,5,]:
    t = t + s(n)
print(t)


c
b

11.a
12.a
13.