

import csv
import sys

a= 5
b= 6
print(a+b)
print(a*b)
print(a/b)
print(a-b)

# Example function that generates output
def my_function():
    print(a + b)
    print(a * b)
    print(a / b)
    print(a - b)

# Redirect standard output to a file
sys.stdout = open('output.txt', 'w')

# Call the function that generates output
my_function()

# Restore standard output
sys.stdout = sys.__stdout__

# Open CSV file for writing
with open('output.csv', mode='w', newline='') as file:
    # Create CSV writer object
    writer = csv.writer(file)

    # Write data to CSV file
    with open('output.txt') as f:
        for line in f:
            row = line.strip().split(',')
            writer.writerow(row)
