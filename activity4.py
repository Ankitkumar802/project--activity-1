firstfile = input("Enter the name of the first file: ")
secondfile = input("Enter the name of the second file: ")

# Open both files in read mode
f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

# Print the content of both files before appending
print('Content of the first file before appending:\n', f1.read())
print('Content of the second file before appending:\n', f2.read())

# Close the files after reading
f1.close()
f2.close()

# Open first file in append mode and second file in read mode again
f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')

# Append the content of the second file to the first file
f1.write(f2.read())

# Reopen the files to read and show the updated content
f1.seek(0)
f2.seek(0)

print("Content of the first file after appending:\n", f1.read())
print("Content of the second file after appending:\n", f2.read())

# Close the files after appending and reading
f1.close()
f2.close()
