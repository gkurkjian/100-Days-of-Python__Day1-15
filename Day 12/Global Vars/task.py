# Modifying Global Scope
enemies = 1


# ## This way it's not the best way to modify
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

## This will be more accurate that will take the global var and return after
def increase_enemies(enemy):
    print(f"enemies inside function (Before modification): {enemies}")

    ## Return the modified value
    return enemy + 11


enemies = increase_enemies(enemies)
print(f"enemies outside function (Modified return): {enemies}")
