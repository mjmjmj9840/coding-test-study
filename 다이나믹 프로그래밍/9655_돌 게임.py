n = int(input())
# (n - 4)번째 돌을 가져가는 사람이 이김
n %= 4
if n % 2 == 1:
    print("SK")
else:
    print("CY")
