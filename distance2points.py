import math

#Function Define Coordinates
def getCoordinates(n):
        print("Insert Coordinates")
        x1 = input("x1=")
        y1 = input("y1=")

        x2 = input("x2=")
        y2 = input("y2=")
        if n == 2:
                return x1, y1, x2, y2
        else:
                x3 = input("x3=")
                y3 = input("y3=")
                return x1, y1, x2, y2, x3, y3

#Calculate distance between two points

coordinates = getCoordinates(2)

#distance = square root of [(x1-x2)^2 +(y1-y2)^2]

distance = math.sqrt((int(coordinates[0])-int(coordinates[2])) ** 2 + (int(coordinates[1])-int(coordinates[3])) ** 2)

print("Distance between two points = ", distance)
