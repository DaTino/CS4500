# In Class Small Group Programming Challenge 2
# by Dara Lim, Safi Khan, and Alberto Maiocco

#Importing random number generator module
import random;

#Open file with AtBat, Random Seed, and BatAverage information
infile = open("InClass3infile.txt", "r");

#Read lines from inFile and set variables
myVars = infile.readlines();
AtBats = int(myVars[0]);
Rseed = int(myVars[1]);
BatAverage = float(myVars[2]);
NumSims = int(myVars[3]);

#Close inFile
infile.close();

#Set random seed for random number generator
random.seed(Rseed);

#lists to hold each season's information
hitList     = [];
avgList     = [];
streakList  = [];

#Start simulation: run through AtBat times.
#If current at bat is less than or equal to the batting average, record a hit
#otherwise, record a miss.
#for recording the hit streak, we set a flag to true if we record a hit,
#if we record a hit and the flag is true we increment the hitStreak.
#If we record a miss, set the flag to false, and check if the current streak
#is longer than the longest streak recorded. If it is, it is now the longest steak.
#if not, we discrad it.
for j in range(NumSims):
    #Set accumulative variables for output statistics
    hits = 0;
    miss = 0;
    currentAtBat = -1;
    hitFlag = False;
    curHitStreak = 0;
    longestHitStreak = 0;

    for i in range(AtBats):
        #simulate an AtBat
        currentAtBat = random.uniform(0.000, 1.000);
        #check if AtBat is hit or miss
        if currentAtBat <= BatAverage:
            hits = hits + 1;
            if hitFlag == True:
                    curHitStreak = curHitStreak + 1;
            hitFlag = True;
        else:
            miss = miss + 1;
            hitFlag = False;
            if curHitStreak >= longestHitStreak:
                longestHitStreak = curHitStreak;
                curHitStreak = 0;


    # We increment the longestHitStreak by 1 to account for the initial hit,
    # and we don't if we get no hits.
    if hits != 0:
        longestHitStreak = longestHitStreak + 1;

    # append each season's data to the lists to record data over all seasons
    hitList.append(hits);
    avgList.append(hits/(AtBats));
    streakList.append(longestHitStreak);

totalHits = 0;
totalAvg  = 0.000;
minMax    = 0;
avgMax    = 0;

for i in hitList:
    totalHits = totalHits + i;

totalAvg = totalHits/(AtBats*NumSims);

print(f"{totalHits}");
print(f"{totalAvg:.3f}");

#for output formatting
outputData = [["Seed:","Batting Average:","At Bats:"],[f"{Rseed}", f"{BatAverage:.3f}", f"{AtBats}"], ["Simulated Hits:", "Simulated Batting Average:", "Longest Hit Streak:"], [f"{hits}", f"{hits/(AtBats):.3f}", f"{longestHitStreak}"]];
#creates uniform columns for output
col_width = max(len(word) for row in outputData for word in row) + 2;  # padding

print(f"Batter Simulation Results");
print(f"*************************");
for row in outputData:
    print("".join(word.ljust(col_width) for word in row));
print(f"*************************");

#outputting to file
outfile = open("InClass3outfile.txt", "w");
outfile.write(f"Batter Simulation Results\n");
outfile.write(f"*************************\n");
outputIncrementer = 0;
#Formatting to match screen output
for row in outputData:
    for word in row:
        outfile.write("".join(word.ljust(col_width)));
        outputIncrementer = outputIncrementer + 1;
        if outputIncrementer % 3 == 0:
            outfile.write("\n");
outfile.write(f"*************************");
outfile.close();


input("Press Enter to terminate.");
