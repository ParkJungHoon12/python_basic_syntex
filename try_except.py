# 예외처리 : try except 구문
# 예외처리를 하는 이유는 프로그램 실행 중간에 예외가 발생하더라도 프로그램이 강제로 종료되지 않도록 위해

#while True:
    
#    try:
#       first = int(input("분자를 입력"))
#       second = int(input("분모를 입력"))
#       a = first / second

#    except ZeroDivisionError as zd: 
#       print(f"{zd}")

#    except ValueError as ve:
#       print(f"{ve}")    

#    else :
#       print(a)
#       break
    
#    finally :
#       print("try one more")



# 예외 처리의 에러 강제의 예시


class Bird:
    def fly(self):
        raise Exception
    
class Eagle(Bird):
    def fly(self):
        print("fly fly")

eagle1 = Eagle()
eagle1.fly()
