student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# ## Finding the total score in the List using sum()
# total_exam_score = sum(student_scores)
# print(total_exam_score)
#
# ## Finding the total score in the List using For Loop
# sum = 0
# for score in student_scores:
#     sum += score
#
# print(sum)


#### Pause 1 - Max
find_max_number = max(student_scores)
print(find_max_number)

### Using for loop to find out the Max number

store_max_num = 0    ## setting var to 0
for score in student_scores:  ## setting for loop to iterate through the List of numbers
    if score > store_max_num:  ## checking condition if score[0] > store_max_num var?
                               ## in 1st case score = 150, store_max_num = 0
        store_max_num = score  ## than set the store_max_num = exact number of score
                               ## this will keep iterate throughout the List of numbers

print(store_max_num)
