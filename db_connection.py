# pip install mysq-connector-python
# mysql, 파이썬 연동 라이브러리
import mysql.connector

try:
    connector = mysql.connector.connect(
        host = "localhost", 
        port = "3306", 
        user = "root", 
        password = "1234", 
        database="board")
    cursor = connector.cursor()

except mysql.connector.Error as err:
    print(err)

add_data = "INSERT INTO new_auther(name, email) VALUES(%s, %s)"
data = ("John3", "Hello3@naver2.com")

try:
    cursor.execute(add_data, data)
    connector.commit()

except mysql.connector.Error as err:
    print(err)


cursor.close()
connector.close()




