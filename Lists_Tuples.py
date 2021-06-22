"""
Learning ab
"""
# Syntax: name of list = [item1, item2, item3]

shopping_list = ["apples", "eggs", "dark chocolate", "tea", "bread"]

# Checking the data type using the type() method
print(type(shopping_list))


# Using index to print eggs
print(shopping_list[1])

# Using negative indexing to display the last item
print(shopping_list[-1])

# How to replace list item
shopping_list[0] = "mangoes"
print(shopping_list)

# How to add items to list .append
shopping_list.append("Tuna")
print(shopping_list)

# How to delete items from list
#del shopping_list[3]
shopping_list.pop(3)
print(shopping_list)

# How to remove
shopping_list.remove("Tuna")
print(shopping_list)

# Multiple data types in the same list
mix_list = [1, 2, 3, "one", "two", "three"]
print(mix_list)
