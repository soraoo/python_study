def greet_user():
    """显示简单的问候语"""
    print("Hello")


def make_pizza(*toppings):
    print(toppings)


def build_profile(**user_info):
    print(user_info)


greet_user()
make_pizza('hehe', 'gg')
build_profile(name='hehe', age='xixi')
