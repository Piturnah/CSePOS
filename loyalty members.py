import csv

def checkMember(name):
    with open ('loyaltyPoints.csv','r') as csvLoyaltyPointsFile:
        csvReader = csv.reader(csvLoyaltyPointsFile)
        for row in csvReader:
            if row[0] == name:
                return True
            else:
                return False

def return_points(name):
    with open ('loyaltyPoints.csv', 'r') as csvfile:
        csvread = csv.reader(csvfile)
        
        for row in csvread:
            if row[0] == name:
                return row[1]
