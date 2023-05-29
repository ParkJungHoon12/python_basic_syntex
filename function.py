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



def myIndex(list, number):
  index = 0

  for i in list:
    if i == number:
        break
    index = index + 1

  print(index)


list = [1,4,9,3,9,6]
myIndex(list, 9)

