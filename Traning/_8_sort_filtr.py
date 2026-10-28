                  # 1 применение


names = ["Anna", "Vitaly", "Valera", "August"]
name_sort = sorted(names, reverse = True)
print(name_sort)

def sort_len (el :str)->int:
    return len(el)

name_sort_len = sorted(names, key = sort_len)
print(1,name_sort_len)


                      #2 применение
#
people = [
    {"name": "Anna", "age": 25},
    {"name": "Vital", "age": 2593},
    {"name": "Ilya", "age": 959}
]

def sort_by_age(pers):
    return pers["age"]

sorted_people = sorted(people, key=sort_by_age)
print(2,sorted_people)


                       #3
#
people = [
    {"name": "Anna", "age": 25},
    {"name": "Vital", "age": 2593},
    {"name": "Ilya", "age": 959}
]

def sort_by_age_name(el):
    return el["name"], el["age"]

sort = sorted(people , key = sort_by_age_name, reverse = True)
print(3,sort)


                        # 4


def is_even(num):
    return num % 2 == 0

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

filters_number =  filter(is_even, nums)

print(4,list(filters_number))

                         #5


people = [
    {"name": "Anna", "age": 25},
    {"name": "Vital", "age": 2593},
    {"name": "Ilya", "age": 959}
]

def adilt (pep):
       return pep["age"] >    1000


filters_people = list(filter(adilt, people))
print(5,filters_people)




