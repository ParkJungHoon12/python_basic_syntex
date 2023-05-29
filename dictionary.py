# 파이썬 에서의 dictionary는 다른 language의 map 또는 hashmap과 유사한 자료형
# json이라는 자료형태와도 유사함

# key : 열쇠
# value : 값

# 딕셔너리 자료구조는 Key와 Value로 이루어져 있다.

# Key는 중복이 불가하고, Value는 중복 가능(다른 Key에도 존재할 수 있다.)
# 해시함수를 통해 메모리 주소를 제어

dic1 = { "이름":"홍길동",  "나이":25,  "성별":"남" }
#print(dic1)

#print(dic1["나이"])
#print(dic1.get("나이"))
#print(dic1)

# 리스트는    a = [value, ...]
# 튜플은      a = (value, ...)
# 딕셔너리는  a = {key:value, ...}

#key, value 추가
#dic1["신분"] = "학생" 
#print(dic1)

#key, value 삭제
#del dic1['성별']
#print(dic1)

# Key를 뽑아낸 값
#keylists= dic1.keys()

# Value를 뽑아낸 값
#valueLists = dic1.values()

# 공 리스트 생성
#answer1 = []
#answer2 = []

# 값 입출력
#for i in keylists:
# answer1.append(i)
# answer2.append(dic1.get(i))

#print(answer1)
#print(answer2)

# dic의 확장
#dic1 = {"a": 1, "b":2, "c":3}
#dic2 = {"a": 5, "d":4, "f":5}

#dic1.update(dic2) #중복된 key중 후에 업데이트 된것이 최종 value로 들어감 ("a" == 5)
#print(dic1)


# 딕셔너리로 변화해서 출력

#lista = ['A','A','B','O','O',"AB","AB"]

#dicta = {}
#for a in lista:
#    if a not in dicta.keys():
#       dicta[a] =lista.count(a)

#print(dicta)


a = [1,2]
b = [3,4]

print(a+b)

