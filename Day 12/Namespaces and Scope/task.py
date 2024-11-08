## Global Scope
enemies = 10


def increase_enemies():
    global enemies
    print(f"Unmodified Global enemies inside function(): {enemies}")
    ## Local Scope
    enemies += 1
    print(f"Modified Global enemies inside function(): {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
