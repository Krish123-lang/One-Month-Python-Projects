with open(r"D:\DajngoProjects\One-Month-Python-Projects\1.Basic\file_handling\test.txt") as f:
    print(f.read())


with open("test.txt", "w") as f:
    f.write("Fuck This world !")
    
    
with open("test.txt") as f:
    print(f.read())
    