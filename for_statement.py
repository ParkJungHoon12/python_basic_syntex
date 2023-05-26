
#range의 의미 : iterable 한 객체
#v1 = list(range(1,10))
#print(v1)

# range(x,y) : x 이상 y미만에 숫자가 담긴 객체가 나옴
# range(y) : 0 이상 y미만에 숫자가 담긴 객체가 나옴

#v1 = list(range(10,20))

# for a in 리스트를 써서 v1의 값을 모두 출력
# for a in range를 써서 v1[index]의 형태로 v1의 값을 모두 출력


lista = [10,20,30,40,50,60,70,80,90,10]
for a in lista:
    a = 100  #이러한 방법으로 변경 불가

    # for a in 리스트 구문은 원본리스트 데이터를 변경할 수 없다.