N = int(input())
array = set(map(int, input().split()))
M = int(input())
requests = list(map(int, input().split()))

for x in requests:
    if x in array:
        print("yes", end=' ')
    else:
        print("no", end=' ')
