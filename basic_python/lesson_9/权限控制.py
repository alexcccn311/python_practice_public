# 作者：Alex
# 2024/10/24 11:15
class Person:
    def __init__(self, name,age,identity,nickname,gender):
        self.name = name
        self._age = age
        self.__identity = identity
        self.__nickname = nickname
        self.__gender = gender

    def _get_age(self):
        return self._age

    @property
    def fun_identity(self):
        return self.__identity

    @fun_identity.setter
    def fun_identity(self, new_identity):
        self.__identity = new_identity

    def get_name(self):
        return self.name


class Slave(Person):
    __slots__ = ['level']
    def __init__(self, name,age,identity,nickname,gender,level):
        super().__init__(name,age,identity,nickname,gender)
        self.level = level

    def __str__(self):
        attrs = [f"{key}: {getattr(self, key)}" for key in self.__slots__]
        print("\n".join(attrs))

person1 = Slave("Alex", 18, "Slave", "Lex", "Male",18)
person2 = Person("Bob", 22, "Engineer", "Bobby", "Male")
person3 = Person("Cindy", 25, "Doctor", "Cin", "Female")
person4 = Person("Daisy", 30, "Teacher", "Day", "Female")
person5 = Person("Ethan", 35, "Scientist", "E", "Male")

"""print(person1.name)
print(person1._age)
print(person1._get_age())
print(person1.get_name())
print(person1._Person__get_identity())
print(person1._Person__identity)
print(dir(Person))
print(person1.fun_identity)
person1.fun_identity= 'Master'
print(person1.fun_identity)
print(person1.level)
print(person1)
print('\t'.join(person2.__dict__))
for item, value in vars(person1).items():
    print(f"{item}: {value}")
for item, value in person1.__dict__.items():
    print(f"{item}: {value}")
person1.__str__()
print(Slave.__base__)
print(Slave.__mro__)"""

