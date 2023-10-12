# Prints a line of equal signs
print("====================================================================================")

# Welcome Message
print("                        Welcome to UMBC Auto World")
print("     Please answer a few questions so that we can get you the exact car you want!")
# Prints a line of equal signs
print("====================================================================================")
print()
# Make and Model 
print("1. What Make and Model of car intrests you?")
print("  a. Honda Civic")
print("  b. Honda Accord")
print("  c. Honda Pilot")
print("  d. Honda Ridgeline")
makeModelChoice = input("Please enter a - d for your choice: ")
print()
print()

# Exterior Color
exteriorColorChoice = input("2. What color exterior would you like?: ")
print()
print()

# Interior Color
interiorColorChoice = input("3. Would you like a Black or Brown color interior? ")
print()
print()

# Interior Material
interiorMaterial = input("4. Would you like a Leather Interior? (Yes or No)")
print()
print()

# Sunroof Option
optionSunroof = input("5. Would you like a Sunroof? (Yes or No)")
print()
print()
#  Time Line
purchaseTimeLine = input("6. Are you looking to purchase this car within the next two weeks? (Yes or No)")
print()
print()

# Print Summary
print("=====================")
print(" Summary of Purchase")
print("=====================")
print()
print("Make and Model:", makeModelChoice)
print("Exterior Color:", exteriorColorChoice)
print("Interior Color:", interiorColorChoice)
print("Leather Interior:", interiorMaterial)
print("Sunroof Desired:", optionSunroof)
print("Looking to Purchase in the next two weeks:", purchaseTimeLine)
print()
print()