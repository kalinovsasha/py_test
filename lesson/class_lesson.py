
class test:
    def __init__(self, say: str = 'hello') -> None:
        self.say = say
        self.__name = 'sasha'
        self.__age: int = 30
    def hello (self):
        print("hello_method")
    def get_name(self):
        return self.__name
    def set_name(self, name:str) -> None:
        self.__name = name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int) -> None:
        self.__age=age
    def say_hello() -> None:
        print('hello')


#НАследование 
class Test2(test):
    def __init__(self, say: str = 'hello', city:str = 'grodno', name:str = "gena" ) -> None:
        super().__init__(say)
        self.__city = city
        # Вызываем сетер родителя
        self.set_name(name)
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city):
        self.__city = city
    def result(self):
        dic = {
            #Тк поле наследуетя, то забирается через геттер
            "name": self.get_name(),
            # тут сетеры заданы через проперти
            "city": self.__city,
            "age": self.age
        }
        print(dic)
    #Переопределение методов
    def say_hello(self) -> None:
        print('Privet')
    #Статический метод, можно вызывать без создания объекта
    @staticmethod
    def say_bye(a:str = 'bye'):
        print(a)
    # Переобпределение стандартного метода, который выводит объект  класса как строку
    def __str__(self):
        return f"{self.get_name()} {self.__city} {self.age}"
  
    


a = Test2("hi", 'grodno')
a.set_name('iis')
a.age = 22
a.say_hello()
a.result()
print(a)

Test2.say_bye("Byebye")
