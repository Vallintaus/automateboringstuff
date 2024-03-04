def print_asterisk_pyramid(height):
    for i in range(height):
        # Calculate the number of asterisks for the current row: 1, 3, 5, ...
        num_asterisks = i * 2 + 1
        # Calculate the number of spaces needed to center the asterisks
        num_spaces = height - i - 1
        # Print the row
        print(' ' * num_spaces + '*' * num_asterisks)

# Example usage
height = int(input("Enter the height of the pyramid: "))
print_asterisk_pyramid(height)
