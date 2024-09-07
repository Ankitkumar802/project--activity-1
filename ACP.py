# Step 1: Open first file in read mode and display content
firstfile = input("Enter the name of the first file: ")
secondfile = input("Enter the name of the second file: ")

f1 = open("codingal.txt", 'r')
print("Content of the first file before any changes:\n", f1.read())
f1.close()

# Step 2: Open second file in write mode, write new content, and display it
f2 = open("codingal1.txt", 'w')
new_content = "This is the new content written to the file."
f2.write(new_content)
f2.close()

f2 = open("codingal1.txt", 'r')
print("Content of the second file after writing new content:\n", f2.read())
f2.close()

# Step 3: Open first file in append mode, append content of second file to it
f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')

f1.write("\n" + f2.read())  # Append content from the second file to the first file
f1.seek(0)  # Move the file pointer to the beginning to read the entire content
print("Content of the first file after appending from the second file:\n", f1.read())

f1.close()
f2.close()
