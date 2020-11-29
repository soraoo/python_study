# 字典
alien = {'color': 'green', 'point': 5}
print(alien['color'])
print(alien['point'])

alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

for k, v in alien.items():
    print(k)
    print(v)

for key in alien.keys():
    print(key)

for key in alien:
    print(key)

for value in alien.values():
    print(value)

# 创建集合
s = set([1, 2])
s = {1, 2}

msg = input('hehe')
print(msg)

