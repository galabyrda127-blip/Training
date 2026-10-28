x = int(input("Введите число"))
y = range(1,x+1)
ssum = 0
l = 0
for i in y:
    if i == 8:
        print("вы уже дошли по циклу до 8")
    if i  == 17:
        break
    if  i % 2 == 0:
        continue
    ssum += i
    l += 1




    print(len(range(i)))
print("колво", l)
print(f"сумма {ssum}")
