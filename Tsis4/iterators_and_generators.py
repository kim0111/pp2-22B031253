#1
def generateScuares(n):
    for i in range(1, n+1):
        yield i**2


for x in generateScuares(9):
    print(x)

#2
n = int(input())
f = [x for x in range(0, n) if x % 2 == 0]
print(f)

#3

def func(n):
    f = [x for x in range(0, n) if x % 3 == 0 and x % 4 == 0]
    print(f)


n = int(input())
func(n)


#4
def scuares(a, b):
    for i in range(a, b):
        yield i**2


x = int(input())
y = int(input())


for x in scuares(x, y):
    print(x)


#5
n = int(input())
f = [x for x in range(1, n+1)]

f.reverse()

print(f)