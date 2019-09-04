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
infile.close();

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

#creating an adjacency matrix. we'll use depth first search to visit each node.
graph = {};
#parsing tuple list to make matrix.
for i in range(n):
    graph[i+1] = [];
for i in kList:
    graph[i[0]].append(i[1]);

#Since we have a directed diagraph, we can use depth first search to determine
#which nodes we visit. We use iterave as opposed to recursive depth first search
#because, as a diagraph, the recursive algorithm will not end.
#This version of the algorithm based off of Koder Dojo
#https://www.koderdojo.com/blog/depth-first-search-in-python-recursive-and-non-recursive-programming
#modified by me to generate the number of times a node is visited on our graph.
def depthFirstIterative(graph, start):
    stack = [start];
    path  = [];
    #Create a list of zeros to hold visited node information
    nVisited = [];
    for i in range(n):
        nVisited.append(int(0));

    while stack:
        vertex = stack.pop();
        nVisited[vertex-1] += 1;
        if vertex in path:
            continue;
        path.append(vertex);
        for neighbor in graph[vertex]:
            stack.append(neighbor);
    return nVisited;

gameVals = depthFirstIterative(graph, 1);
# 1. The number of circles used in the game.
# 2. The number of arrows used in the game.
# 3. The total number of checks on all the circles combined.
# 4. The average number of checks in a circle marked during the game.
# 5. The maximum number of checks in any one circle.
totalChecks = 0;
for i in gameVals:
    totalChecks += i;
avgChecks = totalChecks/n;
maxChecks = max(gameVals);

#Setting the output data. We use append() purely for code readability.
#This is all output formatting.
outputData = [["1. Number of Circles:", f"{n}"]];
outputData.append(["2. Number of Arrows:", f"{k}"]);
outputData.append(["3. Total # of Checks:", f"{totalChecks}"]);
outputData.append(["4. Average # of Checks:", f"{avgChecks}"]);
outputData.append(["5. Maximum # of Checks:", f"{maxChecks}"]);
col_width = max(len(word) for row in outputData for word in row) + 2;  # padding

#More screen output formatting.
print(f"Game Results:");
print(f"*************************");
for row in outputData:
    print("".join(word.ljust(col_width) for word in row));
print(f"*************************");

#outputting to file
outfile = open("InClass3outfile.txt", "w");
outfile.write(f"Game Results\n");
outfile.write(f"*************************\n");
for row in outputData:
    outfile.write("".join(word.ljust(col_width) for word in row));
    outfile.write("\n");
outfile.write(f"*************************\n");
outfile.close();

input("Press Enter to terminate.");
