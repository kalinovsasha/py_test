def decorator(func):
    def wrapper(*args):
        a = list(args)
        a = ' '.join(a)
        print(f"{a}  лог")
        func(*args)
    return wrapper

@decorator
def test(*a):
    print(f'{a} основная функа')


test("a","a")