
file = open("codingal.txt", 'r')
cont = 0

conttent = file.read()
Colist = conttent.split("\n")

for i in Colist:
    if i:
        cont +=1

print("this is the number of liners in the file")
print(cont)