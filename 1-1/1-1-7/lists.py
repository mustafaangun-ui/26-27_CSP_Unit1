list_1 = [3, 4, 5, 6, 7] # <--- numbers
list_2 = ["hello", "world"] # <--- words
print(list_2[0])
print(list_1[2])

# changing values, access the list via ID

list_2[0] = "goodbye"
print(list_2[0])

# using a loop with a list
for num in list_1:
    # printing elements - list is no different
    print(num)

    # popping an element removes it, but lets you access it
    print(list_1.pop)
    print(list_1)