set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6}
set1.remove(3)
set2.add(9)
print(set2) #уникальный элемент
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
set_squares = {x ** 2 for x in range(12)}
print(set_squares)
print({1, 2, 3, 4} == {4, 3, 2, 2, 2, 1, 1, 1})
