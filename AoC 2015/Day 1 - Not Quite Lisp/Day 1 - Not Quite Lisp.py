floor = 0
first_basement_pos = None
cur_pos = 0

with open("input.txt", "r") as input_file:
    for index, value in enumerate(input_file.read()):
        # determining floor
        if (value == "("):
            floor += 1
        elif (value == ")"):
            floor -= 1
        
        # checking if entering basement
        if (floor < 0):
            # add 1 because of the index starts at zero while
            # the puzzle requires the pos starts at one
            first_basement_pos = index + 1
            break

print("first_basement_pos: ", first_basement_pos)
print("floor: ", floor)