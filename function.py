# 특정한 input이 있을때
# 해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자.
# 그런데.해당 연산은 매우 빈번하게 사용이 된다고 가정하자.

#result = (lambda a : ((a + 10 * 20) / 10) ** 2)(3)
#print(result)

# 복잡 로직의 연산을 함수화 시켜서 재사용할 수 있게 해보자.
# input값이 있어도 되고, 없어도 된다.
# return값이 있어도 되고, 없어도 된다.
#def myFunc(myInput):
#    calc = ((myInput + 10 * 20) / 10) ** 2
#    return calc



# 함수 직접 구현해보기 (1~ 100 합)

#def myFunc(num):
#    sum = 0
#    for i in range(num+1):
#        sum += i
#    return  sum


#print(myFunc(100))

#def myFunc(number1, number2):
 #   return 2 * (number1 + number2)

#print(myFunc(1,2))


# 예제1
#def phase(d):
#   return round(d**2 * 3.14, 2)

#d = int(input("반지름을 입력하시오: "))

#print("원의 넓이 : %f" %phase(d))


# 예제2

#def hello1():
 #   print("hello1 python")


#def hello2():

#hello1()
#print(hello2())

# 입력값이 정해져 있지 않고 multiple한 함수

# def sum(*totalsum):
#     total = 0
#     for a in totalsum:
#         total += a
#     return totalsum

# totalvalue = sum(1,2,3,4,5)
# print(totalvalue)

#def cal(a, b):
    #result1 = a+b
   # result2 = a-b
  #  result3 = a*b
 #   return result1, result2, result3


#calValue = cal(1,2)

#for i in calValue:
 #   print("첫번째 결과값 ")


#def cal(a, b, c = 'plus'):
    #if c == 'plus':
     #   result = a+b

   # elif c == 'minus':
      #  result = a-b

  #  elif c == 'multiply':
       # result = a*b

 #   return result

#print(cal(1,2))
#print(cal(1,2,'minus'))
#print(cal(1,2,'multiply'))  


#def whoAreYou(name, age, gender):
#    print(f"제 이름은{name}이고, 나이는 {age}, 성별은 {gender}입니다")


# 전역변수를 수정하려면 global 을 붙인다.
# 객체는 힙메모리에 저장디는데, 함수내에서도 접근하여 추가.수정이 가능하다.
# 스택영역에 있는 지역변수는 함수가 끝나면 휘발되지만, 힙메모리는 휘발되지 않는다.

