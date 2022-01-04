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

#Calculate Midpoint of Two Points

coordinates = getCoordinates(2)

#xmid = x1+x2/2
#ymid = y1+y2/2

midPointX = (int(coordinates[0])+int(coordinates[2]))/2
midPointY = (int(coordinates[1])+int(coordinates[3]))/2

print("Midpoint of two points=(", midPointX, ",", midPointY, ")")


#Calculate Midpoint of Triangle

coordinates = getCoordinates(3)

#xmid = x1+x2+x3/3
#ymid = y1+y2+y3/3

midPointX = (int(coordinates[0])+int(coordinates[2])+int(coordinates[4]))/3
midPointY = (int(coordinates[1])+int(coordinates[3])+int(coordinates[5]))/3

print("Midpoint of triangle=(", midPointX, ",", midPointY, ")")
