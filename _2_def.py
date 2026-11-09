x = int(input("число 1:"))
y = int(input("число 2 :"))
def maxx(a, b):
    if a > b:
        return a
    else:
        return b
tob = "наибльшее"
print(tob, maxx(x,y))



v =str(input("Напишите что-нибудь на  англиском:"))
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for c in s:
        if c in vowels:
            count += 1

    return count

label = "Кол-во гласных:"

print(label, count_vowels(v))



g = int(input("Введите день:"))
t = input("Введите месяц :")

def date( *, d:int, m: str):
    if d > 31:
     return "В месяце нет столько дней"
    else:
      return f"Вы ввели {str(d)} день и {m} месяц"

print(date(d=g,m=t))




