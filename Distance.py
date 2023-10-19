mastHeight = input("Enter the height of the mast in meters: ")
barNumber = input("Enter the number of bars taken up by the mast: ")

mastHeight = float(mastHeight)
barNumber = float(barNumber)

distanceEstimate = mastHeight / barNumber * 4

print("Estimated distance is: ", distanceEstimate, "hectometers")