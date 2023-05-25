

#Boolean 타입
# in(또는 not in) 뒤에 iterable한 자료형이 나온다.
# a in lista, a not in lista, a in dicta, a in seta

# 비어있는 값들은 거짓, 값이 들어있으면 참

# while 조건 : 
#    실행문

# for 변수 in list:
#    실행문

def nn(a):
    b = a*a
    return b


a = [1,2,3,4,5]


print(list(map(nn, a)))