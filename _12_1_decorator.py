def decorator(func):
    def wrapper(*args, **kwargs):
        print("do")
        res = func(*args, **kwargs)
        print("posle")
        return res
    return wrapper

@decorator
def hello(*, name, age):
    date_birthday = 2026 - age
    print("promezhytok")
    return f"Hello, {name}, {date_birthday}"


result = hello(name="John", age=23)

print(result)
