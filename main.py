#Sergio Serrno, Chris Luna, 
# Dictionaries Practice #1
# Create a dictionary called fruits with the following key-value pairs:
fruits = {"apples": " red",
            "banana": "yellow",
            "mango": "green",
            "cherry": "red",
         "watermelon":"green",}
print(fruits)
# apple --> red
# banana --> yellow
# mango --> green
# cherry --> red
# watermelon --> green
# Display the dictionary on the screen.

# Dictionaries Practice #1
# Create a dictionary called my_dict that stores the following information about a person:
# name: Karen
# surname: Jurgens
# age: 35
# occupation: Journalist
# The names of the keys and values must be equal to the ones indicated above.
my_dict={"name":"Karen",
         "surname":"Jurgens",
        "age":"35",
        "occupation":"Journalist"}
print(my_dict)
#   Dictionaries Practice #2
# Use print to returns the second item of the list called points2, inside the following dictionary.
# If the value 300 were to change in the future, the code should work the same to return the value at that same position. To do this, you must refer to the names of the keys and/or indexes as appropriate.
my_dict2 = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
print(my_dict2['points']["points2"][1])#Use dictionary indices to extract the second item of points2


# Dictionaries Practice #3
# Update the information in our dictionary called my_dict (reassigning new values to the keys as appropriate), and add a new key called "country" (without a tilde). The new data is:
# name: Karen
# surname: Jurgens
# age: 36
# occupation: Editor
# country: Colombia
# to do this, you should not change the line of code already written, but update the values using dictionary methods.
# my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}
my_dict["age"]="36"
my_dict["occupation"]="Editor"
my_dict["country"]="Colombia"
print(my_dict)