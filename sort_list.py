# Get input from the user
user_input = input("Enter a list of numbers separated by comma and space: ")

# Convert the input to a list of numbers
numbers = [float(x) for x in user_input.split(", ")]

# Sort the list
sorted_numbers = sorted(numbers)

# Print the sorted list
print("Sorted Numbers:", sorted_numbers)