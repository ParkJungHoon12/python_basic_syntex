
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
def __my_swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] =temp

# mySort Func
def __myselectionsort(lista, option = True):
  ''' Option is True(Default): ascending sorting
      Option is False : decending sorting'''
  i = 0
  max = len(lista)

  while i < max:
    j = i+1
    
    while j < max:
      if option == True and lista[i] > lista[j]: # Acending
         __my_swap(lista, i, j) 
      elif option == False and lista[i] < lista[j]: # Decending
         __my_swap(lista, i, j)    
      j += 1

    i += 1

# main section
k = [93, 45, 21, 30, 20, 94, 66, 71, 45]

__myselectionsort(k)
print(k)

__myselectionsort(k, False)
print(k)







  



# 버블정렬
