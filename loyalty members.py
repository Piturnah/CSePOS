## for it to work you need to ask the persons name and store it the the varible 'name' :)
import csv

def checkMember(name):
    with open ('loyaltyPoints.csv','r') as csvLoyaltyPointsFile:
        csvReader = csv.reader(csvLoyaltyPointsFile)
        for row in csvReader:
            if row[0] == name:
                return_points(name)
                print(updatePoints(name,total))
                return name
                
            
        return False

def return_points(name):
    with open ('loyaltyPoints.csv', 'r') as csvfile:
        csvread = csv.reader(csvfile)
        
        for row in csvread:
            if row[0] == name:
                return row[1]
            
        csvfile.close()
    
def updatePoints(name,total):
    totalPoints = int(return_points(name))
    totalPoints += total
    ##return totalPoints 
    
    with open ('loyaltyPoints.csv', 'r') as csvfile:
        csvread = csv.reader(csvfile)
        csvarray = list(csvread)
        for row in csvarray:
            if row[0] == name:
                row[1]=totalPoints

    with open('loyaltyPoints.csv','w') as csvwrite:
        csvwriter = csv.writer(csvwrite)
        for row in csvarray:
            csvwriter.writerow(row)
                
        ##writer.writerows(line)

       
        csvfile.close()           
    return totalPoints 



