# 파일 읽기 및 쓰기
#
# 읽기 모드 : r, 쓰기 모드 : w, 추가 모드 : a, 텍스트 모드 : t, 바이너리 모드 : b
# 상대 경로(../../, ../, ./), 절대 경로(C:\python_basic\python.txt)


f = open('./resource/it_news.txt', 'r', encoding='UTF-8')
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)
f.close()

# with ~ as(alias)
# open() 열면 객체가 pc 메모리를 계속 점유하고 있다. 그래서 반드시 close()해야 한다.
# with ~ as 을 사용하면 개발자가 실수로 close()를 하지 않아도 with ~ as 구문이 자동으로
# 객체를 close를 해 준다.

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c)) # 반복문 (for, while문)에서 사용 여부 확인

print()

# read() : 전체 읽기, read(10) : 10byte
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    # c = f.read()
    # print(c)
    c = f.read(10)
    print(c)
    c = f.read(10)
    print(c)
    c = f.read(10)
    print(c)
    f.seek(0,0)
    c = f.read()
    print(c)

print()

# readline : 한 줄 씩 읽기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    # c = f.read()
    # print(c)
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

print()

# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
# 정말 많이 사용한다.

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

print()

# 파일 쓰기(write)

# 예제1
with open('./resource/contents1.txt', 'w') as f:
    f.write("I love python\n")
# 예제2
with open('./resource/contents1.txt', 'a') as f:
    f.write("I love python2\n")

# 예제3
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)
# 예제4
with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
