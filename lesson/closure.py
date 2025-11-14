users: dict = {
    'name': 'sasha',
    'age': 18
}

users['city'] = 'grodno'

def printer():
    print(users)

def closure(a:int):
    buf = a - 1
    def inner():
        nonlocal buf
        buf = buf + 1
        print(buf)
    return inner