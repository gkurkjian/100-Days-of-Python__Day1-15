from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_num)  ## this included to see the random num
print(dice_images[dice_num])

## To fix this I've changed the range between (a: 0, b: 5)