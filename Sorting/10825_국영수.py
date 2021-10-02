n = int(input())
score = [0] * n
for i in range(n):
    name, kor, eng, math = input().split()
    score[i] = [name, int(kor), int(eng), int(math)]

score.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))
for name, _, _, _ in score:
    print(name)