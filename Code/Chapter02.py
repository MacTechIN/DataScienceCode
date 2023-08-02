# 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서, 중복, 수정x, 삭제x) # 불변

# 선언
a = ()
b = (1,)
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))
print(type(a), type(b), type(c), type(d), type(e))

# 인덱싱
print('c :', c[1])
print('c :', c[0] + c[1] + c[2])
print('d :', d[-1])
print('e :', e[-1])
print('e :', e[-1][1])
print('e :', list(e[-1][1]))

# 함수
a = (5,2,3,1,4,2,2)
print(a)
print(a.index(1))
print(a.count(2))
print(a.remove(1), a) # remove() 튜플은 삭제x


# 팩킹 & 언팩킹(Packing, and Unpacking)
# 팩킹
t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])

# 언팩킹
t = ('foo', 'bar', 'baz', 'qux')
print(type(t))
(x1, x2, x3, x4) = t
print(x1, x2, x3, x4)
print(type(x1), type(x2), type(x3), type(x4))