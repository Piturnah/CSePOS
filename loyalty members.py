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
            
def updatePoints(name):
    totalBill = getTotalBill(self)
    newPoints = totalBill * 10
    oldPoints = return_points(name)
    totalPoints = newPoints + oldPoints
    return totalPoints
    
    with open ('loyaltyPoints.csv', 'r') as csvfile:
        csvread = csv.reader(csvfile)
        for row in csvread:
            if row[0] == name:
                line = csvfile(r)
                line[0][1] = totalPoints
                
        csvwrite = csv.writer(open('loyaltyPoints.csv', 'w'))
        writer.writerows(line)
               
     
