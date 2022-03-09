N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))

numbers.sort()
print(str(numbers)[1:-1].replace(',',''))