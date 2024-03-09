dmg_one = 2
dmg_two = 4
dmg_three = 3
dmg_four = -1
dmg_five = 10
dmg_six = 5

# This program calculates the total damage from a triple attack combo. 
# The calculate_damage function takes three numbers as its
# parameters and returns the result of adding them all together.

def calculate_damage(opening_attack, core_damage, finishing_move):
    damage = opening_attack + core_damage + finishing_move
    return damage


print("Getting damage for", dmg_one, dmg_two, "and", dmg_three, "...")
print(calculate_damage(dmg_one, dmg_two, dmg_three), "points of damage dealt!")
print("=====================================")

print("Getting damage for", dmg_four, dmg_five, "and", dmg_six, "...")
print(calculate_damage(dmg_four, dmg_five, dmg_six), "points of damage dealt!")
print("=====================================")