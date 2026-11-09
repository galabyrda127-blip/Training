def average(num):
    return sum(num) / len(num)

try:
    n = list(map(int, input("введите числа через пробел").split()))
    print(average(n))
except ZeroDivisionError:
    print("ZeroDivision")

 #2

import requests
import time
print("Подождите 15 секунд")
try:
    url = 'https://api.binance.com/api/v3/ticker/price'

    bitprice = []
    for i in range(1,5):
        req = requests.get(url, params={'symbol':'BTCUSDT'})
        price = float(req.json()['price'])
        bitprice.append(price)
        time.sleep(1)

    print(bitprice)
    print(max(bitprice), "Максимальный")
    print(min(bitprice), "Минимальный")
except requests.exceptions.ConnectionError as error:
    print(f"Something went wronng  {error}")