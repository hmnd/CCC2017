arrayLength = input()
team1 = input()
team2 = input()
team1 = [int(i) for i in team1.split()]
team2 = [int(i) for i in team2.split()]
dayCount = 0
maxDays = 0
team1Count = 0
team2Count = 0
for i in team1:
    dayCount += 1
    team1Count += team1[dayCount-1]
    team2Count += team2[dayCount-1]
    if team1Count == team2Count:
        maxDays = dayCount
print(maxDays)
