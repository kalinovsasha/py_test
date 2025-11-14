                    
def my_generator(count:int):
    count -= 1
    while True:
        count += 1
        yield count

gen = my_generator(1)

i: int = 10
while i > 0:
    i-=1
    print(next(gen)) 
    