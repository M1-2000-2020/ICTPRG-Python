food = ['Pizza','Pancake', 'Chips', 'Burgers', 'Pasta']
print(food)
user = input("Which item would you like to change: ")
index1 = food.index(user)
print(index1)
user2 = input("What food would you like to change it to: ")
print(user2)
index2 = food.insert(index1, user2)
food.remove(user)
print(food)

