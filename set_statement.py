# set은 집합이라 부르기도 한다. 
# set의 특성은 딕셔너리와 마친가지로, index(순서)가 없고, 중복이 없다.

#s1 = {"이름", "나이", "성별"}
#s2 = set("test")

# list의 중복을 제거하기위해서
# list를 가지고 set으로 형변환 시키는 방식도 많이 사용
# print(s1[1]) <- 오류를 일으킴



#lista = ['A', 'A', 'A', 'B', 'B', 'AB', 'O']
#setA = set(lista)
#print(len(set(lista)))

#setA의 값을 하나씩 출력하려면? for문을 사용한다. (index로 접근 어려움)

#for a in setA:
#    print(a)

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
s1.update(s2)
# 프로그래밍에서 | 기호는 or(또는)을 의미
# 합집합 : s1.union(s2)   또는 | 기호
# 교집합 : s1.intersection(s2) 또는 & 기호
# 프로그래밍에서 &은 합집합 또는 엠퍼센트라고 부른다.
# 딕셔너리와 같이 update도 있음 (값을 반환하는것이 아닌 원본 set에 즉시 업데이트 )

#print(s1)
#print(s2)
#print(s1.union(s2))          # 합집합
#print(s1.intersection(s2))   # 교집합
#print(s2.difference(s1))     # 차집합
#s1.update(s2)

#set값 삭제시 remove 함수 사용(원본 set에 즉시 업데이트 )
s1.remove(2)
print(s1)

s1.discard(-1)
print(s1)






