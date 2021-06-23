""""
Code along for dict and sets
"""
# Create a dictionary
students_1 = {
    "name": "James",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["data types", "git and github", "operators", "Lists and Tuples"]
}

# Syntax check
print(students_1)

# Find type
print(type(students_1))

# Fetch the value saved in a key
print(students_1["stream"])

# Fetch the value of list in dict
print(students_1["completed_lessons_names"][1])

# Activity: print the second last index of the key completed_lessons_names
print(students_1["completed_lessons_names"][-2])

#
students_1["completed_lessons"] = 3
print(students_1["completed_lessons"])

# Remove
students_1["completed_lessons_names"].remove("operators")
print(students_1["completed_lessons_names"])

# Print only keys
print(students_1.keys())

# Print only values
print(students_1.values())


#create a set
car_parts = { "engine", "wheels", "windows"}

# add to sets
car_parts.add("seats")
print(car_parts)

# remove from sets
car_parts.discard("wheels")
print(car_parts)

