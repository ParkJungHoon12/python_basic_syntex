# File Syetem 입출력 라이브러리 : open
# Open 함수는, w ,r, a 옵션을 갖고있다.
# w는 write, r은 read, a는 이미 있는것에다가 추가
# 아스키코드는 한글이 다 깨짐 -> 인코딩 UTF-8 해줘야함
# f = open("test.txt", "w")
# f.close()

#f = open("test.txt", "w", encoding = "UTF-8")
#data = ""
#for i in range(10):
#    data = "%d번째 주소입니다\n" %i
#    f.write(data)
#f.close()


#f = open("test.txt", "r", encoding="UTF-8")
# 첫번째 줄만 가져오는 함수
#line = f.readline()
# print(line)
# while, if 문으로 전체 출력
#while line:
#    print(line)
#    line = f.readline()
#f.close()



#f = open("test.txt", "r", encoding="UTF-8")
# 첫번째 줄만 가져오는 함수
#line = f.read()
# print(line)
# while, if 문으로 전체 출력

#for i in line:
#  print(i[0])
#f.close()


f = open("test.txt", "a", encoding="UTF-8")

# 0~9번쨰 줄입니다. -> 10 ~19번쨰 줄입니다.

lines = ""

for i in range(10,20):
  lines += "%d번째 줄입니다.\n" %i
  
f.write(lines)


f.close()








