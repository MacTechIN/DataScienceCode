'''
IF 구문 실습
-관계 연산자
-논리 연산자
-일반 조건문
-다중 조건문
-중첩 조건문
'''

# 기본 형식
print(type(True)) # 0이 아닌 수, "abc", [1, 2, 3, 4], {1, 2, 3} ...
print(type(False)) # 0, "", [], (), {} ...

# 예제1
if True:
    print('Good')

if False:
    print('Bad')

# 예제2
if False:
    print('Bad!')
else:
    print('Good!')

# 관계 연산자
# >, >=, <, <=, ==, !=

# 예제3
x = 15
y = 10

# 양변이 같은 경우 참
print(x == y)
# 양변이 다를 경우 참
print(x != y)
# 왼쪽이 클 때 참
print(x > y)
# 왼쪽이 크거나 같을 때 참
print(x >= y)
# 오른쪽이 클 때 참
print(x < y)
# 오른쪽이 크거나 같을 때 참
print(x <= y)

# 예제4
city = ""
if city:
    print("You are in : ", city)
else:
    print("plz enter your city")

city = "Suwon"
if city:
    print("You are in : ", city)
else:
    print("plz enter your city")

# 논리 연산자(중요★)
# and, or, not

# 예제5
a = 75
b = 40
c = 10

print('and : ', a > b and b > c)
print('or : ', a < b or b > c)
print('not : ', not a > b)
print('not : ', not b < c)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리 순서로 적용
#
# 예제6
print('e1 : ', 3 + 12 > 7 + 3)
print('e2 : ', 5 + 10 * 3 > 7 + 3 * 20)
print('e3 : ', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10)

# 예제7

score1 = 90
score2 = 'A'

# 복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 == "A":
    print("Pass!!")
else:
    print("Fail!!")

# 예제8
id1 = "vip"
id2 = "admin"
grade = "Platinum"

if id1 == "vip1" or id2 == "admin":
    print("관리자 인증")

if id2 == "admin" and grade == "Platinum":
    print("최상위 관리자")


# 다중 조건문
# 예제9
num = 75

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
elif num >= 60:
    print('Grade : D')
else:
    print('Fail!!')

# 중첩 조건문
# 예제10

grade = 'A'
total = 96

if grade == 'A':
    if total >= 97:
        print("장학금 100%")
    elif total >= 95:
        print("장학금 80%")
    else :
        print("장학금 70%")
else:
    print("장학금 비대상자")


# in, not in
# 예제11

q = [10, 20, 30]
w = {70, 80, 90, 90}
e = {"name": 'Lee', "city": 'Seoul', "Grade": 'A'}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("Suwon" not in e.values())

password_origin = 1234
password = int(input('password : '))

if password_origin == password:
    print('Login OK!!')
    a = password
    print('설정한 암호 {} 입니다.'.format(a))
else:
    print('Uncorrect!!', password)

num = int(input('점수를 입력하세요 : '))

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
elif num >= 60:
    print('Grade : D')
else:
    print('Fail!!')

endOfSelenaClass = False
SelfReviewScore = 30

if endOfSelenaClass :
    if SelfReviewScore >= 90 :
        print("Perfect Score")
    elif SelfReviewScore >= 50:
        print("Half Score")
    else :
        print("Zero Score")
else :
    print("Focus Class")


