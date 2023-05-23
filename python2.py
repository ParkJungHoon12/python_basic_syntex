# 주석은 파이썬의 인터프리터가 인식하기 못하도록 하는 기호
# 단축키는 ctrl 슬래시 
# 아래 a =1 의 의미는 a 라는 이름의 변수에 1을 담겠다는 뜻

#a = 1   
#b = '1' #파이썬이 추론을하여 변수인식

#print는 실행후 결과값을 가시적으로 보여주기 위해 터미널창에 출력하는 것
#print(a)
#print(b)
#a = a + 1
#print(a)

# 변수명명규칙
# 변수명을 지을때는 숫자가 먼저 나와서는 안된다.
# 변수명 중간에 띄어쓰기, 특수기호등을 일반적으로 쓰지 않는다.
# 특수부호는 일반적으로 사용하지 않지만, 언더바('_')는 빈번히 사용한다.
# 변수 자료형 출력해 보기
#print(type(a))
#print(type(b))

#c = 2.1
#print(type(c))

# * : asterlisk, ster (곱셈기호)

# 'a'라는 문자를 변수에 저장하게되면, 메모리상에 어떤 숫자값으로 저장될까
#x = 'a'
#print(ord(x))

#x = 'b'
#print(ord(x))


# 문자 자료형
# 문자는 ""쌍따옴표 또는 ''혿따옴표로 표현의 한다.

#제곱
#제곱근
#제곱근은 math라는 라이브러리를 임포트 해야한다.

#print(32*32)

#import math
#print(math.pow(2,10))

# multy line 으로 문자열을 표현하고 싶으면,  쌍따옴표 또는 홋따옴표 3개를 사용하면 된다.
#a = """hello 

#world"""

#print(a)

# 이스케이프 문을 활용한 줄바꿈
# 역슬래시의 또다른 활욜
# 쌍따옴표는 파이썬에서 문자를 의미한다라는 문구를 출력해보세요

#a = "쌍따옴표(\")는 파이썬에서 문제를 의미한다"

#print(a)

#문자열 더하기 곱하기
#a라는 변수에 python이라는 문자열을 담고
# b라는 변수에는 is fun이라는 문자열을 담는다

#C 라는 변수에 두 문자열을 더한 값을 넣어 C를 출력

# python이라는 문자열이 2번 출력 되게 하고 is fun이 1번 출력되게
#a = 'python '
#b = 'is fun'

#c = a*2 + b
#print(c)


# 파이썬에서 인덱스란 기본적으로 특정 위치를 가리키는 용도로 사용된다
# 인덱스의 사용 방법은 원하는 대상에다가 [숫자값] 입력해준다

#a = "python's fun"
#print(a[3])

# 프로그래밍에서는 대부분의 순서는 0부터 시작된다.
# 0,1,2,3,4, 체계

#문자열의 마지막을 출력하라
#문자열의 길이 마지막을 출력하는 함수
#a = "python's fun python's fun python's fun"
#print(a[-1])
#print(a[len(a)-1])

# 문자열의 슬라이싱 
# 슬라이싱이란 문자열을 잘라내는것을 의미
# 대상변수[x:y] : x이상 y미만의 인덱스를 가진 문자열을 잘라낸다


#a = "python's fun"
#b = a[2:7:2]
#print(b)

#a = "20220505children's_day"

#date = a[:8] 
#day = a[8:]

#print(date)
#print(day)

#myage = 3
#myname = 3

#print('my age is %d %s' %(myage, myname))

#a = "           arc-duc-scc            "

#print(a.strip("a"))
#print(a)

#문자열 포멧팅이랑 문자열 중간에 특정 문자(또는 숫자 등)을 삽입하는 방식
# %s : 문자열, %d : 정수, %f : 실수


#language = input("input subject : ") #파이썬에서 input은 문자임
#times = input("input times : ")

#print("I studied %s %s times" %(language, times))



#포멧팅을 왜 쓰는가?
#1) 따옴표를 여러번 안 닫아도 된다.
#2) 문자열을 직접 삽입하면 1회성으로 coding할수밖에 없지만. 포멧팅은 변수값을 삽입 할 수 있다.
# 아래와 같이 코딩하면 따옴표로 열고 닫고를 너무 많이해서 귀찮다.
# a = "I studied" + language + "very hard" + times + "times"

#age    = int  (input("나이가 몇살이신가요? "))
#weight = float(input("몸무게가 몇킬로그램이신가요? "))

#print("my age is %d, and weight is %f kg" %(age, weight))
      
# count : 대상 문자열에 지정한 문자가 몇개가 있는지 출력하는 함수
# find, index : 대상 문자열에 지정한 문자가 몇번째 index에 있는지 알아내는 함수(최초)

#a = "python"

#print(a.count('o'))
#print(a.find('o'))
#print(a.index('o'))
#print(a.find("x"))

#whatyouwant = input("문자를 입력하세요 ")
#search = input("찾고자 하는 문자 1개만 입력하세요")


#result = whatyouwant.find(search)

#if result != -1:
#    print("요청하신 문자는 %d 번째 있습니다" %(result))

#else:
#    print("찾고자 하는 값이 없습니다.")


#대소문자 변경 : upper() / lower()

#a = "hello"
#print(a.upper())
#b = "HELLO"
#print(a.lower())

# 문자열 양쪽 공백을 없는 함수 : Strip()

#a = "     hello world     "
#print(a.strip())


#x = 2
#Y = 2.5*pow(x,2) + 3.3*x + 6
#print(Y)

#word1 = input("첫번째 단어: " )
#word2 = input("두번째 단어: " )
#word3 = input("세번째 단어: " )

#answer = word1[0] + word2[0] + word3[0] 

#print("약자 : %s" %(answer))


a = (3, (1,2), [1,2,3], "4")

print(len(a))

