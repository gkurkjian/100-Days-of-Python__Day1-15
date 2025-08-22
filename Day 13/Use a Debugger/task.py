import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)  ## if we shift one space back, the output will depend on randint [40]
                                ## but one space back the output will be [4, 8, 12, 18, 27, 40] depend on randint
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
