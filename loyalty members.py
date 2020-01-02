import csv

def checkmembers(name):
    with open ('loyaltyPoints.csv','r') as csvLoyaltyPointsFile:
        csvReader = csv.reader(csvLoyaltyPointsFile)
        points = 0
        for row in csvReader:
            if row[0] == name:
                points = row[1]
                return points
        if points == 0:
            print("That person is not a member!")
            return points 

name= input("enter name: ")

points = checkmembers(name)
print(points)
