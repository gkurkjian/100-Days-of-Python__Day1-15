# ## Create a function called greet()
# def greet():
#     print("Hello")
# greet()
#
# ## Functions that allows for inputs
# def greet_with_name(name):  ## name in this case it's the parameter
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
# greet_with_name("Kukulani")  ## Here we're passing an argument in parameter.

def life_in_week(x):
    x = (x * 52 - 4680)
    print(f"You have {abs(x)} weeks left.")


life_in_week(56)
