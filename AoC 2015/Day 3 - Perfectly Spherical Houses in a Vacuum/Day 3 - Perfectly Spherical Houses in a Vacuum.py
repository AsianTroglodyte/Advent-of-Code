x = 0
y = 0
visited_houses_set = {"0, 0"}

with  open("input.txt", "r") as input_file:
    for line in input_file.read():
        match line:
            case "^": 
                y += 1
            case "v":
                y -= 1
            case ">":
                x += 1
            case "<":
                x -= 1
        # visited_houses_set_prev_len = len(visited_houses_set)
        visited_houses_set.add(str(x) + ", " + str(y))

        # if (len(visited_houses_set)):


print("just santa: ", len(visited_houses_set))


# new visited_houses_set
visited_houses_set = {"0, 0"}
# santa coordinates
x1, y1 = 0, 0 
# robot coordinates
x2, y2 = 0, 0
# when set to 
santa_turn = True

with  open("input.txt", "r") as input_file:
    for line in input_file.read():
        if (santa_turn):
            match line:
                case "^": 
                    y1 += 1
                case "v":
                    y1 -= 1
                case ">":
                    x1 += 1
                case "<":
                    x1 -= 1
            visited_houses_set.add(str(x1) + ", " + str(y1))
        elif (not santa_turn):
            match line:
                case "^": 
                    y2 += 1
                case "v":
                    y2 -= 1
                case ">":
                    x2 += 1
                case "<":
                    x2 -= 1
            visited_houses_set.add(str(x2) + ", " + str(y2))
        santa_turn = not santa_turn
        # if (len(visited_houses_set)):

print("with robot: ", len(visited_houses_set))
