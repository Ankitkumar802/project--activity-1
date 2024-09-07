file_read = open('codingal.txt', 'r')
print("file in read mode...")
print(file_read.read())
file_read.close()

file_write = open('codingal.txt', 'w')
file_write.write("file in write mode.. ")
file_write.write("hi i am ankit. i am study in class 10th ")
file_write.close()

file_append = open('codingal.txt', 'a')
file_append.write("file in append mopde ...")
file_append.write("\n i am student of codingal. i am study in class 10th ")
file_append.close()