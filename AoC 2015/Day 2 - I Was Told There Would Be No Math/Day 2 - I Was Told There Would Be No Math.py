import re
tot_sqr_feet = 0

# getting 
with open("input.txt", "r") as input_file:
    # print(input_file.read())
    for line in input_file:
        # resetting square feet to record next set of dimensions
        sqr_feet = 0

        # no need to check if items are valid
        dimensions = re.findall("[\d]+", line)

        length = int(dimensions[0])
        width = int(dimensions[1])
        height = int(dimensions[2])

        # getting total square feet of right rectangular prism box
        sqr_feet = (2 * length * width) + (2 * width * height) + (2 * height * length)

        # getting area of smallest side
        xtra_paper = min(length * width, width * height, height * length) 

        tot_sqr_feet += sqr_feet + xtra_paper

        # for debugging and stuff
        # print(line, end="")
        # print(dimensions[0] + " " + dimensions[1] + " " + dimensions[2], end="\n\n")

print("total square feet required: ", tot_sqr_feet)

tot_ribbon_ft = 0

with open("input.txt", "r") as input_file:
    # print(input_file.read())
    for line in input_file:
        # getting dimension and getting int version of them. no need to check if items are valid
        dimensions = re.findall("[\d]+", line)
        dimensions = [int(dimension) for dimension in dimensions]
        length = int(dimensions[0])
        width = int(dimensions[1])
        height = int(dimensions[2])

        smallest_2_num = []

        temp_smallest_num = 0
        # finding two smallest values
        temp_smallest_num = min(dimensions)
        smallest_2_num.append(temp_smallest_num)
        dimensions.remove(temp_smallest_num)

        temp_smallest_num = min(dimensions)
        smallest_2_num.append(temp_smallest_num)
        dimensions.remove(temp_smallest_num)

        # smallest perimeter
        smallest_perim = (2 * int(smallest_2_num[0])) + (2 * int(smallest_2_num[1]))
        # print(smallest_perim)
        cubic_volume = length * width * height

        tot_ribbon_ft += smallest_perim + cubic_volume

        # print(line + f"smallest perim: {smallest_perim}", end="\n\n")
        # print(dimensions[0] + " " + dimensions[1] + " " + dimensions[2], end="\n\n")

print("tot_ribbon_ft: ", tot_ribbon_ft)