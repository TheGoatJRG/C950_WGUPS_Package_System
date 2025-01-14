"""
John Glick
001418867
C950- WGUPS Delivery System

Ref: "Panopto: 'C950- Webinar 2- Getting Greedy, who moved my data?'"
Ref: Ideas for classes to represent packages and trucks (starting at lines 56 and 127.

WgupsUtil.py
"""

# Needed imports
import datetime
from datetime import timedelta
import csv


# Reading CSV file
# BIG O- O(n)
def read_csv(filename):
    """
    Reads the CSV file at the given path and returns a list of rows.

    Arguments:
        filename: The path to the CSV file.

    Return Value:
        A list of rows in the CSV file.
    """

    # Opens the CSV file in read mode.
    with open(filename, "r") as csvfile:
        # Creates a CSV reader object.
        csv_reader = csv.reader(csvfile)

        # Reads the rows from the CSV reader object and returns them as a list.
        return list(csv_reader)


# PACKAGE_CSV is the path to the CSV file containing the packages.
PACKAGE_CSV = "../data/PackageCSV.csv"

# ADDRESS_CSV is the path to the CSV file containing the addresses.
ADDRESS_CSV = "../data/AddressCSV.csv"

# DISTANCE_CSV is the path to the CSV file containing the distance between two addresses.
DISTANCE_CSV = "../data/DistanceCSV.csv"

# Reading of CSV files
Package_CSV = read_csv(PACKAGE_CSV)
Address_CSV = read_csv(ADDRESS_CSV)
Distance_CSV = read_csv(DISTANCE_CSV)


# BIG O- O(1)
class WgupsPackage:
    """A class representing a WGUPS package.

  Attributes:
    package_id: The ID of the package.
    package_address: The address of the package.
    package_city: The city of the package.
    package_state: The state of the package.
    package_zipcode: The zip code of the package.
    package_deadline_time: The deadline for delivery of the package.
    package_weight: The weight of the package.
    package_status: The status of the package (e.g., "delivered", "en route", "at hub").
  """

    def __init__(self,
                 package_id: int,
                 package_address: str,
                 package_city: str,
                 package_state: str,
                 package_zipcode: int,
                 package_deadline_time: str,
                 package_weight: int,
                 package_status: str):
        """Initializes a WgupsPackage object.

    Arguments:
      package_id: The ID of the package.
      package_address: The address of the package.
      package_city: The city of the package.
      package_state: The state of the package.
      package_zipcode: The zip code of the package.
      package_deadline_time: The deadline for delivery of the package.
      package_weight: The weight of the package.
      package_status: The status of the package (e.g., "delivered", "en route", "at hub").

    """
        attributes = {
            "package_departure_time": datetime.datetime.now(),
            "package_delivery_time": None,
            "package_address": package_address,
            "package_id": package_id,
            "package_state": package_state,
            "package_city": package_city,
            "package_deadline_time": package_deadline_time,
            "package_zipcode": package_zipcode,
            "package_status": "en route",
            "package_weight": package_weight,
        }

        for attribute, value in attributes.items():
            setattr(self, attribute, value)

    def __str__(self):
        """Returns a string representation of the object.

    Return Value:
      A string representation of the object.

    """
        return (
            f"Package ID: {self.package_id}, "
            f"Address: {self.package_address}, "
            f"City: {self.package_city}, "
            f"State: {self.package_state}, "
            f"Zip code: {self.package_zipcode}, "
            f"Deadline: {self.package_deadline_time}, "
            f"Weight: {self.package_weight}, "
            f"Status: {self.package_status}")


# BIG O - O(n)
class WgupsTruck:
    """A class representing a WGUPS truck.

    Attributes:
      truck_capacity: The capacity of the truck in pounds.
      truck_speed: The speed of the truck in miles per hour.
      truck_load: The current load of the truck in pounds.
      truck_packages: A list of packages on the truck.
      truck_mileage: The total mileage traveled by the truck.
      truck_address: The address of the truck's current location.
      truck_depart_time: The time the truck departed the hub.

    """

    def __init__(self,
                 truck_capacity: int,
                 truck_speed: int,
                 truck_load: int,
                 truck_packages: str,
                 truck_mileage: int,
                 truck_address: str,
                 truck_depart_time: str):
        """Initializes a WgupsTruck object.

        Arguments:
          truck_capacity: The capacity of the truck in pounds.
          truck_speed: The speed of the truck in miles per hour.
          truck_load: The current load of the truck in pounds.
          truck_packages: A list of packages on the truck.
          truck_mileage: The total mileage traveled by the truck.
          truck_address: The address of the truck's current location.
          truck_depart_time: The time the truck departed the hub.

        """
        truck_attributes = {

            "truck_capacity": truck_capacity,
            "truck_speed": truck_speed,
            "truck_load": truck_load,
            "truck_packages": truck_packages,
            "truck_mileage": truck_mileage,
            "truck_address": truck_address,
            "truck_depart_time": truck_depart_time,
        }

        for attribute, value in truck_attributes.items():
            setattr(self, attribute, value)


# The starting address of all trucks based on constraints
TRUCK_ADDRESS = "4001 South 700 East"

# The speed of the truck in miles per hour based on constraints.
TRUCK_SPEED = 18

# The capacity of the truck in pounds based on constraints.
TRUCK_CAPACITY = 16

# The current load of the truck in pounds.
TRUCK_LOAD = None

# The time truck 1 departed the hub based on constraints.
WGUPS_TRUCK_1_DEPART_TIME = timedelta(hours=8)

# The time truck 2 departed the hub based on constraints.
WGUPS_TRUCK_2_DEPART_TIME = timedelta(hours=9, minutes=30)

# The time truck 3 departed the hub based on constraints.
WGUPS_TRUCK_3_DEPART_TIME = timedelta(hours=10, minutes=30)

# Manual Loading of all 3 trucks specific to constraints
# The packages on truck 1.
WGUPS_TRUCK_1_PACKAGES = [20, 30, 1, 15, 14, 34, 40, 37, 13, 19, 16, 31, 29]

# The packages on truck 2.
WGUPS_TRUCK_2_PACKAGES = [27, 36, 17, 24, 39, 35, 23, 18, 3, 26, 6, 38, 25]

# The packages on truck 3.
WGUPS_TRUCK_3_PACKAGES = [11, 22, 33, 2, 9, 10, 4, 32, 8, 5, 12, 7, 28, 21]

# Truck objects based on attributes specific to each truck - to be applied to nearest neighbor algorithm
# Truck 1
wgups_truck1 = WgupsTruck(TRUCK_CAPACITY, TRUCK_SPEED, TRUCK_LOAD,
                          WGUPS_TRUCK_1_PACKAGES, 0.0, TRUCK_ADDRESS,
                          WGUPS_TRUCK_1_DEPART_TIME)

# Truck 2
wgups_truck2 = WgupsTruck(TRUCK_CAPACITY, TRUCK_SPEED, TRUCK_LOAD,
                          WGUPS_TRUCK_2_PACKAGES, 0.0, TRUCK_ADDRESS,
                          WGUPS_TRUCK_2_DEPART_TIME)

# Truck 3
wgups_truck3 = WgupsTruck(TRUCK_CAPACITY, TRUCK_SPEED, TRUCK_LOAD,
                          WGUPS_TRUCK_3_PACKAGES, 0.0, TRUCK_ADDRESS,
                          WGUPS_TRUCK_3_DEPART_TIME)


# BIG O- O(n)
def get_address(address):
    """Returns the address ID for the given address.

    Arguments:
      address: The address to search for.

    Return Value:
      The address ID, or None if the address is not found.
      Big O- O(n)
    """
    return next((int(row[0]) for row in Address_CSV if address in row[2]), None)


# Used to find total distance from address to address
#  BIG O- O(1)
def distance_between_addresses(row, column):
    """Finds the distance between two addresses.

    Arguments:
      row: The x-coordinate of the first address.
      column: The y-coordinate of the second address.

    Return Value:
      The distance between the two addresses.
    """
    location_distance = Distance_CSV[row][column]
    # If location is empty instead look for value in other location
    if location_distance == '':
        location_distance = Distance_CSV[column][row]
    # returns the distance between two addresses
    return float(location_distance)
