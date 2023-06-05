import requests
import json

url = "https://api.binance.com/api/v3/ticker/24hr"

response = requests.get(url)
data_json = json.loads(response.text)

symbol_name = 'BTCUSDT'
lastPrice_data = ""

for i in data_json:
    if i['symbol'] == symbol_name:
        lastPrice_data = i['lastPrice']
        break

print(f"{symbol_name} PRICE는 {lastPrice_data}")