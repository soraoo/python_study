# 3.1
names = ['Ai', 'Bi', 'Ci']
print(names[0])
print(names[1])
print(names[2])

# 3.2
print(f'{names[0]}, How Are U?')
print(f'{names[1]}, How Are U?')
print(f'{names[2]}, How Are U?')

# 3.5
people = ['A', 'B', 'C']
print(f'嘉宾有: {people}')
print(f'{people[1]}嘉宾无法赴约')
people[1] = 'N'
print(f'新的嘉宾是{people[1]}')
print(f'目前的嘉宾为: {people}')

# 3.6
print('现在找到了一个更大的餐桌')
people.insert(0, 'G')
print(f'邀请新的嘉宾{people[0]}到名单开头')
people.insert(2, 'H')
print(f'邀请了另一个新的嘉宾{people[2]}到名单中间')
people.append('K')
print(f'邀请最后一个嘉宾{people[-1]}到名单末尾')
print(f'发出邀请：{people}')

# 3.7
print('出事了 我只能邀请两个人')
p = people.pop()
print(f'Sorry, {p}')
p = people.pop()
print(f'Sorry, {p}')
p = people.pop()
print(f'Sorry, {p}')
p = people.pop()
print(f'Sorry, {p}')
print(f'剩下到嘉宾：{people}')
del people[1]
del people[0]
print(f'剩下的嘉宾：{people}')

# 3.8
places = ['A', 'C', 'E', "D", 'B']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

print(len(places))

for place in range(1, 10):
    print(place)

l = list(range(1, 5))
print(l)

# 列表解析
squares = [value ** 2 for value in range(1, 10)]
print(squares)
