
#Tuple은 변경불가능한 자료형으로서, ()을 통해 표현

#t1 = (1,2,'a',4)
#print(t1)
#indexing, slicing 가능 (리스트와 동일하게 허용 * 조회는 가능함!)
#print(t1[0])

#삭제 및 변경 불가
#del t1[0] #<- 에러 발생
#print(t1)

#튜플을 쓰는 이유는 개발자가 해당 자료를 수정하지 못하도록 
#강제적으로 지정한 것
#리스트에비해 메모리 효율적
#paymethod = ('cash', 'card', 'tmoney')
#p1 = input("어떤 방법으로 결제하시겠습니까? ")
#if p1 not in paymethod:
#    print("사용하실 수 없는 결제 방법입니다")
#else:
#    print("%s를 선택하셨습니다." %(p1))
 
# 딕셔너리(자바에서 맵)



import class_statement