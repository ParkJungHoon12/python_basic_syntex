# pip install mysq-connector-python
# mysql, 파이썬 연동 라이브러리
import mysql.connector
import requests
import json
import time

try:
    connector = mysql.connector.connect(
        host = "localhost", 
        port = "3306", 
        user = "root", 
        password = "1234", 
        database="practices")
    cursor = connector.cursor()

except mysql.connector.Error as err:
    print(err)

while True:
    url = "https://api.binance.com/api/v3/ticker/24hr"
    
    response = requests.get(url)
    data_json = json.loads(response.text)
    
    symbol_name = 'BTCUSDT'
    lastPrice_data = ""
    
    for i in data_json:
        if i['symbol'] == symbol_name:
            lastPrice_data = i['lastPrice']
            break
        
    add_data = "INSERT INTO coin_price(coin_name, last_price) VALUES(%s, %s)"
    data = (symbol_name, lastPrice_data)

    cursor.execute(add_data, data)
    connector.commit()
    time.sleep(10)

cursor.close()
connector.close()

