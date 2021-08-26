N, K = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort(reverse=True)
a_list = a_list[K:] + b_list[:K]

print(sum(a_list))
