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


