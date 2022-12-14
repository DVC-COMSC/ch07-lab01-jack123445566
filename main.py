# Create an empty list to store the numbers
numbers = []

# Ask the user to input 5 numbers
for i in range(5):
  # Take user input and append it to the list
  numbers.append(int(input("Enter a number: ")))

# Calculate the min and max values in the list
min_value = min(numbers)
max_value = max(numbers)

# Calculate the sum of all values in the list except the min and max
total = sum(numbers) - min_value - max_value

# Print the result
print("The total of all numbers except the min and max is: ", total)
