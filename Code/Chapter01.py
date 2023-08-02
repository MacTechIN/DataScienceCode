# sepearatar 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='   ')
print('010', '7777', '1234', sep='-')
print('python', 'gmail.com', sep='@')

# end 옵션
print('Welcome to', end=' | ')
print('IT News', end=' | ')
print('Web Site')

# format 사용(d : 3, s : 'python', f : 3.133434)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print('%10s'% ('nice111'))
print('{:>10}'.format('nice111'))
print('{:@>10}'.format('nice111'))
print('{:10}'.format('nice111'))
print('{:<10}'.format('nice111'))
print('{:^10}'.format('nice1111'))
print('%5.7s' % ('nice111'))
print('%.7s' % ('pythonstudy'))
print('{:10.11}'.format('pythonstudy'))

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))
print('%d' % (42))
print('{:<4d}'.format(42))

# %f
print('%f' % (3.1443434343))
print('{:f}'.format(3.1443434343))
print('%1.8f' % (11113.1443434343))
print('%1.2f' % (11113.1443434343))
print('%06.2f' % (3.1443434343))
print('{:06.2f}'.format(3.1443434343))


# 문법의 의해 이해
# 문법을 잘 이해 할려면 ? ->>> 복습을 반드시 하라!!!

# 다양한 변 수 선언법
# 변수 할당 설명
# Object Identity
# 변수 네이밍 규칙
# 예약

# 기본 선언 및 출력 및 연산
n = 800
print(n * 3)

# 변수의 자료형
# int
n = 3000
print(type(n))
print()
# str
n = 'nice'
print(type(n))

# 동시 선언
x = y = z = 700
print(x, y, z)

# 선언
n = 300
print(n)
# 재선언
n = 700
print(n)

# 변수 값이 출력되는 과정
# Object References
# 변수 값 할당 상태
# 타입에 맞는 오브젝트 생성
# 값 생성
# 콘솔 출력

# 예시1
print(type('300'))
print(type(int(300)))

# 예시2
n = 777
print(n, type(n))

# 예시3
n = 300
m = n
print(m, n)
print(type(m), type(n))


#  가장 중요한 부분
# id(identity)확인 : 객체의 고유값 확인

m = 800
n = 800

print(id(m))
print(id(n))

print(id(m) == id(n))


m = 800
n = 800
z = 800
i = 800
#m = n = z= i = 800

print(id(m))
print(id(n))
print(id(z))
print(id(i))
print(id(m) == id(n))

# 다양한 변수 선언
# Camel Case : numberofCoLLegeGraduates -> Method
# Pascal Case : NumberofcoLLegegraduates -> class
# Snake Case : number_of_college_graduates

NumberofcoLLegegraduates = 3
print(NumberofcoLLegegraduates)

number_of_college_graduates = 3
print(number_of_college_graduates)

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
# 1AGE  = 7


#  예약어는 변수명으로 불가능

# if for def raise
# None del import return
# and while as except with breakpoint
# class from or and
# continue pass elif
#     pass

# 슬라이싱
str_s1 = "Nice Python"
print(len(str_s1))

print(str_s1[0:3])
print(str_s1[0:6])
print(str_s1[5:])
print(str_s1[:5])
print(str_s1[:])
print(str_s1[:len(str_s1)-2])
print(str_s1[1:15:5])
str_s1 = "Nice Python"
print(str_s1[-5:])
print(str_s1[:-5])
print(str_s1[2:-3])
print(str_s1[2:-3:2])
print(str_s1[1:-4:3])
print(str_s1[::2])
print(str_s1[::-2])


myList = [1, 1.25, 1, 'word', [1, 2, [3, 4, ['python', 2]]]]
print(myList)
print(type(myList))
print(myList[4][2][2][0])


# 리스트 수정, 삭제
c = [70, 75, 80, 85]
c[2] = 8
print('c : ', c)

c[1:2] = [['a', 'b', 'c']]
print(c)


c = [70, 75, 80, 85]
del c[2:4]
print(c)


# 리스트 함수
a = [5, 2, 3, 1, 4]
print(a)
a.append(10)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
b = [5, 2, 3, 1, 4]
print('a : ', b.index(3), b[4]) # index() -> 해당 숫자의 위치(인덱싱)를 알려준다.

b = [5, 2, 3, 1, 4]
print(b.pop())
print(b.pop())
print(b.pop())
print(b.pop())
print(b.pop())

b = [5, 2, 3, 1, 4]
del b[2]
print(b)


b = [5, 2, 3, 1, 4, 7, 8, 9]
while b:
    data = b.pop()
    print(data)

myList = [2024, 3, 9*9, ['풋살', ['승마', '수영']]]
myList.insert(2,"삽입")
print(myList)

a = [5, 2, 3, 10, 4]
ex = [8, 9, 10, 11, 12]
a.extend(ex)
print(a)
a.sort()
print(a)
print(a.count(10))