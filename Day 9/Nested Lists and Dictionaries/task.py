capital = {
    "France": "Paris",
    "Germany": "Berlin"
}

## Nest List in Dictionary
##If we're going to sort which cities we've travelled in the country we cannot put each key;
##such as, "France": "Paris", "lille", etc. We can list them as "France": ["Paris", "Lille"]
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }
#
# ## Pause 1
# ##Printout "Lille" from the Nested List
# print(travel_log["France"][1])

## Pause 2
##Try to print "D" from the nested_list
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])  ## the output will be "D"

## Pause 3
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

##Printout Stuttgart

##This is my way I did
print(travel_log.get("Germany").get("cities_visited")[2])  ## Stuttgart

##This is Angela's way
print(travel_log["Germany"]["cities_visited"][2])  ## Stuttgart


# ## From the Quizz
# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }
# # print(dict[1])  ## This is an error, it'll not display the 2nd item from the dict
# print(dict["b"])  ## This will fetch the 2nd item from the dict

# ## Second quizz
# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }
# print(order["main"][2][0])