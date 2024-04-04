varFile = open("TeachingPython/bascii 2023/3rd time (16 mar 24)/sample_file.txt", "r")

# longString = varFile.read() # 1
# oneLineString = varFile.readline() # 2
stringToList = varFile.readlines() # 3

print(stringToList)
z = []
for name in stringToList:
    a = name.strip("\n").split(" ")
    z.append(a)
print(z)

varFile.close() # Always close the file after opening it


## List Comprehension

a = [_.strip("\n").split(" ") for _ in open("TeachingPython/bascii 2023/3rd time (16 mar 24)/sample_file.txt", "r").readlines()]
print(a)