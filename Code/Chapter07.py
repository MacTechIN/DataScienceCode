# While 흐름제어
# - while 기본 사용법
# - Break, Continue
# - While-Else 구문
# - 무한 반복 구문
# - 기본 패턴 실습

# while <expr>
    # <statement(s)>

# 예제1

n = 5
while n > 0:
    print(n)
    n -= 1

# 예제2
a = ['ytk', 'nwj', 'yjh']

while a:
    print(a.pop())

# 예제3
# break, continue
n = 5

while n > 0:
    n -= 1
    if n == 2:
         break
    print(n)
print("Loop Ended")


# 예제4

m = 5
while m > 0:
    m -= 1
    if m == 2:
         continue
    print(m)
print("Loop Ended")

#예제5
i = 1

while i <= 10:
    print('i : ', i)
    if i == 6:
        break
    i += 1

#예제6
n = 10

while n > 0:
    n -= 1
    print('n : ', n)
#    if n == 5:
#        break
else:
    print('else out')

#예제7

a = ['kdh', 'gsm', 'jsy', 'jjh', 'nys', 'sgm', 'ytg']
s = 'jjh'

i = 0

while i < len(a):
    print(len(a))
    if a[i] == s:
        print(s)
        break
    i += 1
else:
    print(s,'not found it list.')
