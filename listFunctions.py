lucky_numbers = [54, 84, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Oscar", "Toby"]
friends.insert(1, "Kelly")
friends.remove("Jim")
# clear()
friends.pop() # Prints '['Kevin', 'Kelly', 'Karen', 'Oscar']'
print(friends.index("Kevin")) # Prints '0'
print(friends.index("Kelly")) # Prints 1
print(friends.count("Oscar")) # Prints 2
print(friends)

lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)