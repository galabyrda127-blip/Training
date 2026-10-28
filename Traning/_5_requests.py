import requests
import time
print("Подождите 15 секунд")
url = 'https://api.binance.com/api/v3/ticker/price'

bit_price = []
for i in range(1,15):
    req = requests.get(url, params={'symbol':'BTCUSDT'})
    price = float(req.json()['price'])
    bit_price.append(price)
    time.sleep(1)

print(bit_price)
# print(type(bit_price)) -> list
print(max(bit_price),"Максимальный")
print(min(bit_price), "Минимальный")
