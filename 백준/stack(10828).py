import sys


num = int(sys.stdin.readline())
stack = list()

for i in range(num):
    user_input = sys.stdin.readline().split()

    if user_input[0] == "push":
        stack.append(user_input[1])
    elif user_input[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif user_input[0] == "size":
        print(len(stack))
    elif user_input[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif user_input[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

# 이코드는 시간초과가 뜸.

# input() 함수를 사용할 경우, 시간초과 에러가 뜨므로 시간단축을 위해 sys.stdin.readline()을 사용한다. 
# 입출력 속도 비교 : sys.stdin.readline > raw_input() > input()



