# 1
print("Traning")

def sort_len (el :str):
    return len(el)
#            =
sort_len_lambda = lambda el : len(el)

print(sort_len("ab6756765cde"))
print(sort_len_lambda("abcde"), end = 3 * "\n")



  #2
print("Traning")

fruits = ["apple", "banana", "cherry"]

sorted_fruits = sorted(fruits, key = lambda el: len(el))

print(sorted_fruits, end = 3 * "\n")

#3
print("Traning")

longest_word = max(sorted_fruits, key = lambda el : len(el))
print(longest_word, end = 3 * "\n")

#4
print("Traning")

people = [
    {"name": "Andfffsrvna", "age": 25},
    {"name": "Visdftal", "age": 2593},
    {"name": "Ilsfya", "age": 959}
]

people_sort = sorted(people, key = lambda el : len(el["name"]), reverse = True)
print(people_sort)