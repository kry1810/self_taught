with open("tesutesu.txt", "w")as f:
    f.write("Hi from pythoniacdsk!")

my_list = []
with open("tesutesu.txt", "r") as f:
    my_list.append(f.read())

print(my_list)