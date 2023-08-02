# 딕셔너리 선언
myDictionary = {
    "name" : "selena",
    "job" : "data scientist"
}
print(myDictionary['name'])
print(myDictionary['job'])
print(type(myDictionary))

# 변경 삭제
# 딕셔너리 값 추가
myDictionary['grade'] = [98, 100, 88]
print(myDictionary)

# 딕셔너리 값 수정
myDictionary['grade'] = [100, 100, 90]
print(myDictionary)

# 딕셔너리 값 삭제
del myDictionary['grade']
print(myDictionary)


# 선언
a = {'name': 'superman', 'phon_num' : '01046295415', 'birth' : '990119'}
b = {0 : 'Hello Python'}
c = {'arr' : [1,2,3,4,5]}
d = {
    'Name' : 'Niceman',
    'City' : 'Suwon',
    'Age' : 25,
    'Grade' : 'A',
    'Status' : True
}
e = ([
    ('Name' , 'Niceman'),
    ('City' , 'Suwon'),
    ('Age' , 25),
    ('Grade' , 'A'),
    ('Status' ,  True)
])
f = dict(
    Name = 'Niceman',
    City = 'Suwon',
    Age = 25,
    Grade = 'A',
    Status = True
)