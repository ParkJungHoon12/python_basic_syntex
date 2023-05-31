
#range의 의미 : iterable 한 객체
#v1 = list(range(1,10))
#print(v1)

# range(x,y) : x 이상 y미만에 숫자가 담긴 객체가 나옴
# range(y) : 0 이상 y미만에 숫자가 담긴 객체가 나옴

#v1 = list(range(10,20))

# for a in 리스트를 써서 v1의 값을 모두 출력
# for a in range를 써서 v1[index]의 형태로 v1의 값을 모두 출력


#lista = [10,20,30,40,50,60,70,80,90,10]
#for a in lista:
 #   a = 100  #이러한 방법으로 변경 불가

    # for a in 리스트 구문은 원본리스트 데이터를 변경할 수 없다.


    # 리스트를 만드는 방법중에 list comprehension 이 있다.
    # 리스트에 0~9까지 담는 방법

    # 방법 1
#lista = [0,1,2,3,4,5,6,7,8,9]

     # 방법 2
#lista = list(range(10))

     # 방법 3
#lista = []
#for a in range(10):
#  lista.append(a)

    # 방법 4
#lista = [a*2 for a in range(1,10,2)]
#print(lista)

# continue문
   # 아래 실행문을 실행시키지 않고 조건으로 다시 간다.

# for문과 Break문 : For문에서 Break문을 반드시 써야 하는 상황


#lista = [90, 25, 67, 45, 80]
#count = 0
#for i in lista:
#    count = count + 1
#    if i >= 60:
#        print("%d번 학생은 합격입니다." %count)
#    else:
#        print("%d번 학생은 불합격입니다." %count)

# 혈액형이 a형인 고객 선착순 1명만 찾는 상황.

#lista = ['b', 'b', 'ab', 'a', 'b', 'a']
# 출력결과 : N번째 고객이 이벤트에 당첨되었습니다.

#count = 1

#for i in lista:
#    if i == 'a':
#        print("%d번째 고객이 당첨되었습니다." %count)
#        break # Break를 넣고 안넣고 차이 확인
#    count = count + 1

# for문을 이용한 구구단
# 5단결과 출력 " 5X1 = 5"

#for i in range(5, 10):
 #    for j in range(1, 10):
 #         print("{0}X{1} = {2}".format(i, j , i*j))


#lista = [10,20,30,40]

# Case 1
#temp  = lista[0]
#lista[0] = lista[1]
#lista[1] = temp
      

# Case 2
#lista[0], lista[1] = lista[1], lista[0] 
#print(lista)


# for 문을 이용한 정렬 알고리즘
# 선택정렬 : 0번째인덱스부터 가장 작은 값을 채워나가는 정렬
# 첫번째 for문은 채워나가야할 index를 의미
# 두번째 for문은 비교의 대상



# def __my_swap(a, i, j):
 #    temp = a[i]
#  a[i] = a[j]
  #   a[j] =temp

# mySort Func
# def mySort(lista):
 #  i = 0
 #  max = len(lista)

 #  while i < max:
  #   j = i+1
   #  while j < max:
    #   if lista[i] > lista[j]: # Acending
     #     __my_swap(lista, i, j) 
      # j += 1
   #  i += 1

# main section


#test_lambda = lambda a : a ** 2


#cal_dict = {"plus" : lambda a,b : a + b,
#            "minus" : lambda a,b : a - b,
#            "multyply" : lambda a,b : a * b}


#print( cal_dict["plus"](1,2) )

#oddOrNot = lambda x : True if x % 2 == 0 else False

#print( oddOrNot(3) )

#map함수 : 특정함수와 반복가능한 자료형을 입력받아, 특정함수가 수행한 결과값을 return
#map(함수, list or tuble or 등등 )

#lst = list( map( (lambda x : x*2) , [1,2,3,4] ) )
#print(lst)

# filter의 역할은 대상이 되는 리스트에서 함수를 적용하여 참/거짓 조건으로 값을 걸러내는 것
# 0 을 걸러내는 함수임


#lst = list( filter( (lambda x : x*2) , [-1,0,3,-2,5] ))
# print(lst)



#lista = [4,7,1,2,5,6,8]
#new_list = list(filter(lambda x : True if x % 2 != 0 else False, lista))
#print(new_list)

# 주어진 자료들의 총 합
#print(sum([1,2,3]))

# 문자를 아스키코드 변환 : ord()
#print(ord('a'))

# 숫자 97이 의미하는 아스키코드상의 문자는 뭘까?
#print(chr(97))

#str1 = '123asdf4124sdgs'
#str2 = ""

#for i in str1:
#    if i.isalpha() == True:
#       str2 += i 

#print(str2)

# 절대값 구하기
#print(abs(-3))
#lista = [1,-5, 12,-5]

#print(list(map(abs, lista)))


# 재귀함수를 통한 factorial 예제
# 재귀함수란 함수내에서 함수자기자신을 호출하는 함수
# 재귀함수에서는 반드시 재귀함수를 종료시키는 조건이 들어가야한다.



#def my_factorial(n):
#    if n == 1:
#        return 1
#    else:
#        return n * my_factorial(n-1)





#print( my_collatz(1062323523523632663233351234) )


# 재귀함수를 반드시 써야만 하는 상황.
# 반복의 횟수를 알 수 없을때 쓴다.

# 순열(리스트에서 m개의 순열 리스트 출력)

class mother:
    result = 5

    def sum(self, a, b):
        return a + b
    

class child(mother):
    def sum(self, a, b):
        return self.result + a + b + 1
    

k1 = mother()
k2 = child()

print(k1.sum(2,3)) 
print(k2.sum(2,3))