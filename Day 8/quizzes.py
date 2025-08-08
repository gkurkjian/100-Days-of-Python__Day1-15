### Quizz Number 1 ###
## weeks in year = 52, 52w * 90y = 4,680

# def life_in_weeks(age):
#     total_weeks = 90 * 52
#     weeks_lived = age * 52
#     weeks_left = (total_weeks - weeks_lived)
#     print(f"You have {weeks_left} weeks left.")
#
#
# life_in_weeks(56)



### Quizz Number 2 ###
## Love calculator
#def calculate_love_score(name1, name2):
    # Step 1: Combine both names into one string
    # Convert the combined string to lowercase to simplify counting

    # Step 2: Count how many times the letters in the word "TRUE" appear in the combined names
    # T count
    # R count
    # U count
    # E count
    # Add up the total count from "TRUE"

    # Step 3: Count how many times the letters in the word "LOVE" appear in the combined names
    # L count
    # O count
    # V count
    # E count (again)
    # Add up the total count from "LOVE"

    # Step 4: Combine the two totals (TRUE and LOVE) into a two-digit number
    # Example: true_total = 5, love_total = 3 → love_score = 53

    # Step 5: Print or return the love score
    #pass  # Remove this line when you start coding

# Step 6: Call the function with example names to test it
# calculate_love_score("Kanye West", "Kim Kardashian")



## first approach ##
# def calculate_love_score(name1, name2):
#     # your code here
#     combined_names = (name1 + name2).lower()
#
#     ## count t.r.u.e by each alphabet
#     t = combined_names.count("t")
#     r = combined_names.count("r")
#     u = combined_names.count("u")
#     e = combined_names.count("e")
#     ## combining them
#     true_count = (t + r + u + e)
#
#     ## count l.o.v.e by each alphabet
#     l = combined_names.count("l")
#     o = combined_names.count("o")
#     v = combined_names.count("v")
#     e = combined_names.count("e")
#     ## combining them
#     love_count = (l + o + v + e)
#
#     score = int(str(true_count) + str(love_count))
#     print(score)
#
# # Call your function with hard coded values
# calculate_love_score("Kanye West", "Kim Kardashian")


## Second approach ##

### Second way to implement ###
def calculate_love_score(name1, name2):
    ## combining the names to iterate in each of them
    combined_names = (name1 + name2).lower()

    letter_true = "true"
    letter_love = "love"
    count_true = 0
    count_love = 0

    for both_names in letter_true:
        count_true += combined_names.count(both_names)
        ##print(count_true)

    for both_names in letter_love:
        count_love += combined_names.count(both_names)
        ##print(count_love)

    ## One of the way to print each individual count(s) without combining them
    ## Ex, if we did final_count = (count_true + count_love) the output will be 12 not (7)(5)
    #print(f"Love score = {count_true}{count_love}")

    ## Another way to do it is to convert each entity into str but, the output will make it int.
    final_score = int(str(count_true) + str(count_love))
    print(f"{final_score}")

calculate_love_score(name1="Kanye West", name2="Kim Kardashian")