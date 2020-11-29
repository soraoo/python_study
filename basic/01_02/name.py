#####################
# 字符串
##################


name = "ada lovelace"
print(name.title())  # 首字母大写
print(name.upper())  # 全部大写
print(name.lower())  # 全部小写

# 格式化字符串
first_name = "ada"
last_name = "lovelace";
full_name = f"{first_name} {last_name}"
print(full_name)

# 删除空白
py = " python "
print(py.rstrip())
print(py.lstrip())

# 练习
# 2.3
name = "zxc"
msg = f"Hello {name}, would you like to learn some Python today?"
print(msg)

# 2.4
name = "zxc"
print(name.lower())
print(name.upper())
print(name.title())

# 2.5
print('Albert Einstein once said,"A person who never made a mistake never tried anything new"')

# 2.6
famous_person = "Albert Einstein"
msg = f'{famous_person} once said,"A person who never made a mistake never tried anything new"'
print(msg)

# 2.7
name = "  \tAlbert \nEinstein "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

