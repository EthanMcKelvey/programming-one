colors = ["red", "green", "blue"]
print(colors)
print(colors[1])  # green

fruits = ["apple", "banana", "orange", "kiwi", "mango"]

for item in fruits:
    print(item)
print("")

for index in range(len(fruits)):
    print(fruits[index])
print("")

#lastfruits = fruits[len(fruits)-1]
lastfruits = fruits[-1]
print(lastfruits)
input()