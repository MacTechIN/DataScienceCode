# #파이썬 함수 사용법
# # -함수 중요성
# # -함수 선언 및 사용
# # -다양한 리턴 사용
# -중첩 함수
# -함수 Hint
# -기타 사용법
# -람다(lambda) 개념
#
# 함수 정의 방법
# def function_name(parameter):
#     code

# 예제1
def first_func(w1):
    print("Hello, ", w1)

word = "Goodboy"

print(first_func)

#예제2
def return_func(w1):
    value = "Hello, " + str(w1)
    return value

x = return_func('GoodTeens!!')
print(x)

#예제3
#일반 함수의 전형적인 예제
def add(a, b): # a, b -> 매개변수
    result = a + b # 실행 명령문
    return result

a = add(3, 4)
print(a)

# 입력 값이 없는 함수
# 입력값 ->>> 함수 ->>> 결괏
def say():
    return 'Leeyohwan'

a = say()
print(a)

#결괏값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add(3, 4)

#def add(*args):
#     print("%d, %d의 합은 %d입니다." % (args[0], args[1], args[0]+args[1]))
#
# add(3, 4)

#입력값도 결괏값도 없는 함수
def say():
    print('Parkminjae!!')

say()

#매개변수 지정하여 호출하기
def add(a, b):
    return a + b

result = add(b=3, a=4)
print(result)

#입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
def add_many(*args): # 매개변수 입력을 갯수 상관없이 받는다.
    result = 0
    for i in args:
        result += i
    return result

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)


def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)

#예제
def print_param(*args):
    print(args)
    for p in args:
        print(p)

print_param('a', 'b', 'c', 'd')

#예제
def print_param2(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())

    for name, value in kwargs.items():
        print("%s : %s" % (name, value))

print_param2(first = 'a', second = 'b', third = 'c', fourth = 'd')

#예제
def print_param3(*args, **kwargs):
    print(args)
    print(kwargs)

print_param3('a', 'b')
print_param3(third = 'c', fourth = 'd')
print_param3('a',  'b', third ='c', fourth = 'd')

#예제
def print_param4(a, b, c):
    print(a,b,c)

p = ['c', 'a', 'b']
print_param4(*p)

p2 = {'c' : '3', 'a' : '1', 'b' : '2'}
print_param4(**p2)

#예제9
def args_func(args):
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-----')

args_func(str(4321))

#format 함수 설명
a = 2
b = 3
s='구구단 {1} x {0} = {2}'.format(a,b,a*b)
print(s)

#직접 대입하기
s1 = 'name : {0}'.format('taekyung')
print(s1)

# 변수로 대입 하기
age = 17
s2 = 'age : {0}'.format(age)
print(s2)

#이름으로 대입하기
s3 = 'number : {num}, gender : {gen}'.format(num=15, gen='Man')
print(s3)

# 인덱스를 입력하지 않으면?
s4 = 'name : {}, city : {}'.format('taekyung', 'suwon')
print(s4)

# 인덱스를 순서를 바뀌면?
s5 = 'name1 : {1}, name2 : {0}'.format('taekyung', 'younseo')
print(s5)

# 중괄호를 표현
s6 = 'Format example. {{}}, {}'.format('{}')
print(s6)

#중괄호로 겹쳐진 인자
s7 = 'This is value {{{0}}}'.format('banana')
print(s7)

#왼쪽 정렬
s9 = 'this is {0:-<10} | done {1:-<5} |'.format('left', 'a')
print(s9)
#오른쪽 정렬
s10 = 'this is {0:+>10} | done {1:+>5} |'.format('right', 'b')
print(s10)
#가운데 정렬
s11 = 'this is {0:*^10} | done {1:*^5} |'.format('center', 'c')
print(s11)

#정수 N자리
s12 = '정수 10,5자리 : {0:10d}, {1:05d}'.format(12345, 12)
print(s12)
#소수점 N자리
s13 = '소수점 2자리 : {0:0.2f}, 소수점 5자리 : {1:0.5f}'.format(123.1234567, 3.14)
print(s13)

#구구단 표시 (2단과 3단만 표시)
for a in range(2, 4):
    for b in range(1, 10):
        print('{0} X {1} = {2:2}'.format(a, b, a*b))

#format 함수를 사용하여 다음 문제를 해결하시오.
#오늘은 2022년 6월 22일 입니다.
a = '오늘은 {}년 {}월 {}일 입니다.'.format(2022,6,22)
print(a)

#변수를 활용하여 다음 문제를 해결하시오.
#오늘은 2022년 6월 22일 입니다.
year = 2022
month = 6
day = 22
a = '오늘은 {}년 {}월 {}일 입니다.'.format(year,month,day)
print(a)

#인덱스를 활용하여 다음 문제를 해결하시오.
year = 2022
month = 6
day = 22
a = '오늘은 {0}년 {1}월 {2}일 입니다.'.format(year,month,day)
print(a)
#오늘은 2022년 6월 22일 입니다.
year = 2022
month = 6
day = 22
a = '오늘은 {1}년 {2}월 {0}일 입니다.'.format(year,month,day)
print(a)
#오늘은 6년 22월 2022일입니다.
year = 2022
month = 6
day = 22
a = '오늘은 {2}년 {0}월 {1}일 입니다.'.format(year,month,day)
print(a)
#오늘은 22년 2022월 6일입니다.

#정렬, 소수점을 활용하여 다음 문제를 해결하시오.
#오늘은 ______2022년 6.0월 000022일 입니다.
print('오늘은 {0:_<10}년 {1:0.1f}월 {2:0>6}일 입니다.'.format(year,month,day))
#오늘은 0000022.0년 22.0000월 22일입니다.
print('오늘은 {2:09.1f}년 {2:.4f}월 {2}'.format(year,month,day))
