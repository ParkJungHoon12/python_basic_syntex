# IF 문의 기본 문법

#if 참조건 :
#  실행문
#else :
#  실행문

#a = 1
#if True:
#    print("A는 10보다 큽니다")
#else:
#    print("A는 10보다 작습니다")

# IF 문에 들여쓰기를 한다는건 IF문에 종속되어있다는 것이다.
# 파이썬의 주요한 특징(괄호가없음)

#a = int(input("숫자를 입력해주세요"))
#if a>10:
#    print("a는 10보다 큽니다")

#else:
#    print("A는 10보다 작습니다")

#불형

# 문제 : 얼마를가지고 있습니까를 변수에 담고 만약 30000이상이 있으면
# 택시를 타고 가시오 출력, 그렇지 않으면, 걸어가시오를 출력

#money = int(input("얼마를 가지고 있습니까? "))

#if money >= 30000:
#    print("택시를 타고 가시오")
#else:
#    print("걸어가시오")

#else는 OPTIONAL 요소.

#for 문의 기본 구조 
# for 변수 in 반복가능한자료형(iterable)
# 실행문
#lista = [1,2,3,4,5,6,7,8,9,10]
#for a in lista:
#    print(a)
# range 문법


def test1(result):
    result += 10
    return result

def test2(result):
    result += 100
    return result

a = test1(20)
b = test2(20)

print(a)
print(b)


