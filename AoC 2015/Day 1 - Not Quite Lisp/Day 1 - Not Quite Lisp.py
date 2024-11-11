floor = 0

with open("input.txt", "r") as input_file:
    while ((paren := input_file.read(1))!= ""):
        if (paren == "("):
            floor += 1
        elif (paren == ")"):
            floor -= 1

print(floor)