# list는 변수마다 값을 할당해서 사용하기에, 관리에 어려움이 있으므로
# 한 변수에 값을 집합시켜놓은 것.

#a = "김돌쇠"
#b = "김갑돌"
#c = "김갑순"

#print(a)
#print(b)
#print(c)

#하나의 변수에 여려개의 데이터를 관리
#lit의 경우에 [] 대괄호를 사용하여 데이터를 집합

#lista = ["a", "b", "c", "d", "e", "f", "g"]

# list 안의 각각의 값에 접근할 때에는 index를 활용
#print(lista[0])
#print(lista[1])
#print(lista[2])

#여러개의 데이터를 범위를 지정해서 가져오고 싶을때는 slicing사용
#Slicing의 결과값은 같은 리스트로 출력이 됨

#print(lista[:5])
#print(type(lista[:5]))

# 문자열은 메모리 내부적으로 list와 유사한 자료구조
# 문자열은 값을 추가하거나 수정할 수 없다

#list_ex1 = ['a', 'b', 'c', [1,2,3]]

#number = list_ex1[3]

#print(number[0]+number[2])

#list1 = [1,2,3,4]
#list2 = ["a", "b", "c"]

#list3 = list2 * 3 
#print(list3)

#리스트 길이구하기
#print(len(list3))

#리스트 값 수정하기 -> 1개의 값만 바꿀땐 1개의 값으로 
#여러 값을 바꿀땐 다른 리스트로 대체

#list = [1,3,5,6,7,9]
#list[1]  = 4
#list[2]  = [5,5,5]
#print(list)

# 리스트 요소 개수 세기
#list = ["1","2","3","4", "1"]
#print(list.count("1"))

# 리스트 값 삭제하기
#del list[2:6]

#모든 특정한 숫자 9 값을 삭제 하려면
#lists = [1, 3, 5, 9, 9, 9, 9, 5, 7, 9, 9, 10, 9, 9, 9, 9]
#i = 0

#while i != len(list):
#    while i < len(list):
#      if list[i] == 9:
#        del list[i]
#        i = 0
#        break
#      i += 1
#print(list)


#lista = [1,3,5,7]
#lista.append(9)
#lista.append(10)
#lista.insert(2, "abc")
#listb = [10,20,30]
#lista.extend(listb)
#print(lista)

# list의 정렬은 sort함수 사용
# sort()는 오름차순 정렬
# reverse = True 는 내림차순 정렬
# list뒤집기 : reverse()

#lista = ["김돌쇠", "김갑돌", "김갑순", "김철수"]


# list위치반환 : index()
# 마지막요소 끄집어내기 : Pop()
# remove and return last value

#print(lista.pop())
#print(lista)


# 문자리스트를 문자열로 만들기 (join)
#lista = ["hello", "world", 3]
#st1=""
#st2 = st1.join(lista)

# 문자열를 문자 리스트로 만들기 (list, split)
#sta = "Hello world python"
#mySta1 = list(sta)
#mySta2 = sta.split(" ")

#print(mySta1)
#print(mySta2)


insta1 = [1,2,3,4,3,2,1]

print(insta1.pop())