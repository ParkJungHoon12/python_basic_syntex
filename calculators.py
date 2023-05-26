

#Boolean 타입
# in(또는 not in) 뒤에 iterable한 자료형이 나온다.
# a in lista, a not in lista, a in dicta, a in seta

# 비어있는 값들은 거짓, 값이 들어있으면 참

# while 조건 : 
#    실행문

# for 변수 in list:
#    실행문

class Korea: # 부모
    def say(self):
        print("Im from Korea")

class South_Korea: #자식
    def say1(self):
        print("Im from South Korea")


a = Korea()
b = South_Korea()


a.say()
b.say()