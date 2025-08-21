## Global varibale
enemies = 10

def increase_enemies():
    global enemies
    print(f"Unmodified Global enemies inside function(): {enemies}") ## output will be 10

    ## local scope
    enemies += 1
    print(f"Modified Global enemies inside function(): {enemies}") ## output will be 11

increase_enemies()
print(f"Enemies outside function(): {enemies}")  ## output will be 11 bcz we modified it on line 10
