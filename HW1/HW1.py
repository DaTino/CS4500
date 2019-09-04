# HW1 by Alberto Maiocco
# This program plays a game on a strongly directed graph (diagraph).
# Using a file that specifies a diagraph, this
# program will determine the following:
# 1. The number of circles used in the game.
# 2. The number of arrows used in the game.
# 3. The total number of checks on all the circles combined.
# 4. The average number of checks in a circle marked during the game.
# 5. The maximum number of checks in any one circle.
# We assume the input file describes a diagraph, but we will check
# that it is correctly formatted.

#Open the input file in read mode
infile = open("HW1infile.txt", "r");

#Read lines from infile and initialize relevant variables.
#specs is a list containing the lines of the infile.
#n is the number of circles between 2 and 10 inclusive
#k is the number of arrows between circles
#kList is a list containing the arrow specifications.
specs = infile.readlines();
n     = int(specs[0]);
k     = int(specs[1]);
kList = [];
#for the list of arrows, we create ordered pairs by stripping the whitespace
#from the file's lines and push the numbers into tuples. kList becomes a
#list of tuples signifying the arrows' directions.
for i in specs[2:]:
    i = i.replace("\n", "");
    temp = i.split(" ");
    kList.append((int(temp[0]), int(temp[1])));
    print(temp);


    # temp = i;
    # arrowSource = [];
    # jDex = 0;
    # for j in temp:
    #     if (j.isspace()) == False:
    #         arrowSource.append(j)
    #     else:
    #         jDex = j
    #         break;
    # temp = "".join(temp[jDex:].split());
    # kList.append((arrowSource, temp));


print(kList[0]);

print(f"Circles: {n}, Arrows: {k}, kList[0]: {kList[0]}");

#for i in kList:
#    print(i);
