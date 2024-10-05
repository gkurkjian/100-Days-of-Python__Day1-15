
### From the Quiz ###
##You are going to write a function called calculate_love_score() that tests the compatibility
#between two names.  To work out the love score between two people:
# 1. Take both people's names and check for the number of times the letters in the word
# TRUE occurs. 2. Then check for the number of times the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number and print it out.
# e.g. name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5
#
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3
# Love Score = 53
#
# Example Input calculate_love_score("Kanye West", "Kim Kardashian")
# Example Output 42 How to test your code and see your output?
#
# Udemy coding exercises do not have a console, so you cannot use the input() function.
# You will need to call your function with hard-coded values like so:
# def calculate_love_score(name1, name2): # your code here # Call your function with
# hard coded values calculate_love_score("Kanye West", "Kim Kardashian")


# def calculate_love_score(name1, name2):
#     combined_names = (name1 + name2).lower()  ## combined_names
#
#     true_count = 0  ## setting count to int 0
#     love_count = 0
#
#     for letter in "true":
#         true_count += combined_names.count(letter)  ## iterating in combined_names and increasing
#                                                     ##the count number when it occures
#
#     for letter in "love":
#         love_count += combined_names.count(letter)
#
#     love_score = int(str(true_count) + str(love_count))  ## converting str to int
#
#     print(f"Love score = {love_score}")
#
# calculate_love_score(name1="George Kurkjian", name2="Angela Yu")


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
    print(f"The love score should be {final_score}")

calculate_love_score(name1="Kanye West", name2="Kim Kardashian")
