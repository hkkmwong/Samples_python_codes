import random

# Generate six unique random numbers between 1 and 49
random_numbers = sorted(random.sample(range(1, 50), 6))

# Generate a seventh random number that doesn't repeat any of the first six numbers
seventh_number = random.choice([num for num in range(1, 50) if num not in random_numbers])

# Print the results
print("Six unique random numbers (sorted):", random_numbers)
print("Seventh random number:", seventh_number)
