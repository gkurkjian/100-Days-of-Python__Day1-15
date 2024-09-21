states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)

num_of_states = len(states_of_america)
print(num_of_states) # 50

print(states_of_america[num_of_states -1]) # The last state it's Hawaii


##### Second part of the lesson Nested Lists ######

fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
print(f"Here we're printing individual Lists\n", fruits, veg, "\n")

fruits_and_veg = [fruits, veg]
print(f"Here we're Nesting the 2 Lists inside 1 List\n", fruits_and_veg, "\n")


### This is from the Quiz ###
# Question 2:
# Given the code below:

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(f"This is from the quiz\n", fruits)
# What do you think will be printed?
### The Answer is, fruit[-1] will remove the last entity "Pears" and remove/replace it with
### "Melons", fruit.append("Lemons") will insert at the end. Therefore, the answer will be;
### "Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Melons", "Lemons"]





