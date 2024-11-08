game_level = 10
enemies = ["George", "Lithin", "Kukulani"]

def create_enemy():
    new_enemy = ""  ## initializing an empty var
    if game_level > 5:  ## accessing to Global var
        new_enemy = enemies[0]  ## setting the Local var into Global var entity
    else:
        new_enemy = enemies[2]  ## Same as line abot setting the Local var into Global var entity
    print(new_enemy)

create_enemy()
