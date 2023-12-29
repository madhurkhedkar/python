list = [10, 20, 'madhur', -10, 30.5]
print(list)
print(len(list))

list.append(40)
list.remove('madhur')
del (list[1])
print(list)

# list.clear()
# print(list)

print(max(list))
print(min(list))

list.insert(3, 99)
print(list)

list.sort(reverse=True)
print(list)
