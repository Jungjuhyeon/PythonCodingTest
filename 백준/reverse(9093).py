import sys

num = int(sys.stdin.readline())

for i in range(num):
    listname = sys.stdin.readline().split()
    for j in listname:
        print(j[::-1],end =" ")
