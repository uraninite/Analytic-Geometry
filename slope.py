import math

#Function Define Coordinates
def getCoordinates(n):
        print("Insert Coordinates")
        
        x1 = input("x1=")
        y1 = input("y1=")
        if n == 1:
                return x1, y1

        elif n == 2:
                x2 = input("x2=")
                y2 = input("y2=")
                return x1, y1, x2, y2

        else:
                x3 = input("x3=")
                y3 = input("y3=")
                return x1, y1, x2, y2, x3, y3

#Calculate slope

coordinates = getCoordinates(1)

#slope = y/x

slope = int(coordinates[1])/int(coordinates[0])

print("Slope = ", slope)

#Calculate slope between two points

coordinates = getCoordinates(2)

#slope = (y2-y1)/(x2-x1)

slope = (int(coordinates[3])-int(coordinates[1]))/(int(coordinates[2])-int(coordinates[0]))

print("Slope between two points = ", slope)
