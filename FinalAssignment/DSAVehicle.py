class Vehicle:
    """
    Vehicle class is used to store the information of a vehicle.
    """

    def __init__(self, vid):
        self.vid = vid
        self.curLoc = None
        self.destLoc = None
        self.distanceToDest = -1
        self.batteryLevel = -1

    def setLocation(self, loc):
        """
        Set the location of the vehicle.
        """
        self.curLoc = loc

    def setDestination(self, loc):
        """
        Set the destination of the vehicle.
        """
        self.destLoc = loc

    def setDistanceToDest(self, distance):
        """
        Set the distance to the destination of the vehicle.
        """
        self.distanceToDest = distance

    def setBatteryLevel(self, level):
        """
        Set the battery level of the vehicle.
        """
        self.batteryLevel = level

    def getLoc(self):
        """
        Get the location of the vehicle.
        """
        return self.curLoc

    def getDest(self):
        """
        Get the destination of the vehicle.
        """
        return self.destLoc

    def getDistanceToDest(self):
        """
        Get the distance to the destination of the vehicle.
        """
        return self.distanceToDest

    def getBatteryLevel(self):
        """
        Get the battery level of the vehicle.
        """
        return self.batteryLevel

    def __str__(self):
        return "Vehicle ID: " + self.vid + \
               " Current Location: " + str(self.curLoc) + \
               " Destination Location: " + str(self.destLoc) + \
               " Distance to Destination: " + str(self.distanceToDest) + \
               " Battery Level: " + str(self.batteryLevel)
