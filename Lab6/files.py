import os
#1
# path = r"C:\Users\Юра\PycharmProjects\Lab6"
# for i in os.listdir(path=path):
#     print(i)


#2


#3


#4 Write a Python program to count the number of lines in a text file.
# p = r"test.txt"
# with open(p, "rt+") as f:
#     c = 0
#     for lines in f:
#         c += 1
#     print(c)


#5 Write a Python program to write a list to a file.
# l = [1, 2, 3]
# with open("test.txt", "w+") as f:
#     for i in l:
#         f.write(str(i))


#6 Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
# for i in range(97, 123):
#     f = open(f"{chr(i)}.txt", "w")
#     f.close()


#7 Write a Python program to copy the contents of a file to another file
# with open("test.txt") as f:
#     with open('test2.txt', "w") as c:
#         for line in f:
#             c.write(line)



#8 Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
# p = "C:/Users/Юра/PycharmProjects/Lab6/test2.txt"
# if not os.path.exists(path=p):
#     print("Doesnt exist")
#
# os.remove(p)


