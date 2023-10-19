shipLength = input("Enter the length of the ship in meters: ")
sailTime = input("Enter the time it takes for the ship to sail its own length in the format mm:ss : ")
mstoknots = 1.94384

def convertToSeconds(sailTime):
    minutes, seconds = map(int, sailTime.split(':'))
    totalSeconds = minutes*60 + seconds
    return totalSeconds

estimatedSpeed = float(shipLength) / convertToSeconds(sailTime) * mstoknots

print("Estimated speed is: ", estimatedSpeed, "knots")