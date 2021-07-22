# 럭키 스트레이트
n = input()
length = len(n)
left = sum(map(int, n[:length//2]))
right = sum(map(int, n[length//2:]))

if left == right:
    print("LUCKY")
else:
    print("READY")
