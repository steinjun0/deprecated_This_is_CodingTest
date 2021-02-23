# 18:47

position = input()
if position[0] == 'a':
  x = 1
elif position[0] == 'b':
  x = 2
elif position[0] == 'c':
  x = 3
elif position[0] == 'd':
  x = 4
elif position[0] == 'e':
  x = 5
elif position[0] == 'f':
  x = 6
elif position[0] == 'g':
  x = 7
elif position[0] == 'h':
  x = 8
y = int(position[1])


def calculator(next_x, next_y):
  if next_x > 0 and next_x < 9:
    if next_y > 0 and next_y <9:
      return 1
  return 0

result = 0

next_x = [x+1, x+2, x-1, x-2, x+1, x+2, x-1, x-2]
next_y = [y+2, y+1, y-2, y-1, y-2, y-1, y+2, y+1]

result = 0
for i in range(8):
  result += calculator(next_x[i], next_y[i])

print(result)



# ord
# ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.
# ※ ord 함수는 chr 함수와 반대이다.

# chr
# chr(i)는 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다.