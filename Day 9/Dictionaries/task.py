from xml.dom.minidom import ProcessingInstruction

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Bug"])


my_empty_dictionary = {}  ## creating an empty dictionary
print(type(my_empty_dictionary))  ## <class 'dict'>

## Adding new value into the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary["Loop"])

## Edit the item in the dictionary
programming_dictionary["Bug"] = "Kaka"

print(programming_dictionary["Bug"])

print("############################### \n \n")

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
