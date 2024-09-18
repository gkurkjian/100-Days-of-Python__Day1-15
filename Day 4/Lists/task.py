### Learning List Data Structure in Python
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0]) ## Will print Delaware
print(states_of_america[-1])  ## Will print the last state which is Hawaii

### Modifying the data
### Please visit the website and review https://docs.python.org/3/tutorial/datastructures.html
states_of_america[1] = "Pencilvania"  ## Here we changed Pennsylvania or Pencilvania
print(states_of_america[1])

states_of_america.append("Angelaland")  ## It adds value at "the-end" of the string
print(states_of_america)  ## Look in the console's output at the end you'll see Angelaland

states_of_america.extend(["George", "KUKULANI"])  ## Will extend and add 2 variables in the list
print(states_of_america)

states_of_america.insert(0, "Hi")  ## Will insert new word at specified position
print(states_of_america)  ## the output on 1st position will print Hi and then rest of string
