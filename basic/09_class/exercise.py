class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f'{self.name} is now sitting')

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f'{self.name} rolled over!')


my_dog = Dog('Willie', 6)

print(my_dog.name)
print(my_dog.age)
my_dog.sit()
my_dog.roll_over()


# 9-1
class Restaurant:
    """餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name} - {self.cuisine_type}')

    def open_restaurant(self):
        print('opening')


my_restaurant = Restaurant('牛肉', '烧饼')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

