# N, M, K = input().split()
# N = int(N)
# M = int(M)
# K = int(K)
# numbers = [int(x) for x in input().split()]

# numbers.sort()

# print(numbers)

# tmp_old = numbers.pop()
# tmp_new = 0

# result = tmp_old
# cnt = 0
# for i in range(M-1):
#     tmp_new = numbers.pop()
#     if(cnt <= K):
#         if(tmp_new == tmp_old):
#             cnt += 1
#         else:
#             cnt = 0
#         result += tmp_new
#         tmp_old = tmp_new

#     else:
#         for j in numbers.lenght():
#             if(tmp_old != numbers[numbers.length()-j]):
#                 tmp_new = numbers[numbers.length()-j]
#         if(tmp_old == tmp_new):
#             break


# print(result)

# N, M, K = input().split()
# N = int(N)
# M = int(M)
# K = int(K)
# numbers = [int(x) for x in input().split()]

'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0
'''

N = 5
M = 8
K = 3
numbers = [2, 4, 5, 4, 6]


result = 0

numbers.sort()


first = numbers[-1]
second = numbers[-2]


result += int(M/K) * first *K
result += M % K * second


print(result)
