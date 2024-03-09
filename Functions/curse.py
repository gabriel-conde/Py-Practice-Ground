# Define a function named curse that takes a parameter weapon_damage.
def curse(weapon_damage):
    # Calculate the lesser cursed damage by multiplying the weapon_damage by 0.5.
    lesser_cursed = weapon_damage * 0.5 
    # Calculate the greater cursed damage by multiplying the weapon_damage by 0.25.
    greater_cursed = weapon_damage * 0.25
    # Return a tuple containing both the lesser_cursed and greater_cursed values.
    return lesser_cursed, greater_cursed

# Define a function named test that takes a parameter weapon_damage.
def test(weapon_damage):
    # Print the original weapon damage.
    print("Weapon's base damage:", float(weapon_damage))
    # Print a message indicating that the weapon is being cursed.
    print("Cursing...")
    # Call the curse function with the provided weapon_damage and assign the returned values to lesser_cursed and greater_cursed.
    lesser_cursed, greater_cursed = curse(weapon_damage)
    # Print the damage after applying the lesser curse.
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    # Print the damage after applying the greater curse.
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    # Print a separator line for readability.
    print("=====================================")

# Define the main function.
def main():
    # Call the test function with different weapon_damage values to demonstrate the curse function.
    test(100)
    test(500)
    test(1000)

# Call the main function to execute the program.
main()
