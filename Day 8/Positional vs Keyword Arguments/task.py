# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

## Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is it like in location {location}?")

# greet_with("George", "Toronto")  ## Default calling

greet_with(location="Kukulani", name="George") ## Matching with the sequence
