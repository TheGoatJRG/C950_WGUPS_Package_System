"""
John Glick
001418867
C950- WGUPS Delivery System

Ref: "Panopto: 'C950- Webinar 2- Getting Greedy, who moved my data?'"
Ref: How to load packages into the hash table from CSV file (line 68)

Ref: "The Nearest Neighbors Algorithm in Python"
Ref: Nearest neighbor algorithm used for package delivery system (line 27)

WgupsPackageSystem.py
"""

# needed imports
import datetime
import csv
import sys
import WgupsHashTable
import WgupsUtil
from WgupsUtil import WgupsPackage, PACKAGE_CSV
from app.WgupsUtil import get_address, distance_between_addresses


# NEAREST NEIGHBOR ALGORITHM
# BIG O- O(N^2)
# Ref from "The Nearest Neighbors Algorithm in Python"
def package_delivery(wgups_truck):
    """Delivers all packages on the given truck.

    Arguments:
      wgups_truck: The truck to deliver packages on.

    """
    # Initialize undelivered_packages and clear truck packages
    undelivered_packages = [hash_package.search(package_id) for package_id in wgups_truck.truck_packages]
    wgups_truck.truck_packages = []

    # Used to cycle through list of undelivered packages until there are none left
    # Finds the nearest package and adds it to list
    while undelivered_packages:
        distance_to_next_location = sys.maxsize
        package_new = None

        # Find the package that is closest to the truck's current location.
        for pack in undelivered_packages:
            dist = distance_between_addresses(get_address(wgups_truck.truck_address),
                                              get_address(pack.package_address))
            if dist < distance_to_next_location:
                distance_to_next_location = dist
                package_new = pack

        # Move the package and update the truck's properties
        wgups_truck.truck_packages.append(package_new.package_id)
        undelivered_packages.remove(package_new)

        # Truck properties updated including mileage, address, depart_time
        wgups_truck.truck_mileage += distance_to_next_location
        wgups_truck.truck_address = package_new.package_address
        wgups_truck.truck_depart_time += datetime.timedelta(

            # add distance/velocity to the time
            hours=distance_to_next_location / WgupsUtil.TRUCK_SPEED)

        # Set the package's delivery and departure time as per the truck's current time
        package_new.package_delivery_time = wgups_truck.truck_depart_time
        package_new.package_departure_time = wgups_truck.truck_depart_time


# referenced from Panopto webinar video- C950- Webinar 2- Getting Greedy, who moved my data?
# BIG O- O(n)
def packages_loaded(filename, hash_package):
    """Loads package data from a CSV file into a hash table.

    Arguments:
      filename: The path to the CSV file.
      hash_package: The hash table to store the package data.

    Raises:
      FileNotFoundError: If the file does not exist.

    """
    with open(filename) as package_information:
        new_package_information = csv.reader(package_information, delimiter=',')
        for pack in new_package_information:
            packObj = WgupsPackage(int(pack[0]), pack[1], pack[2], pack[3], pack[4], pack[5], pack[6],
                                   "Package at Hub ")

            # Used to insert address data into hash table
            address_hash.insert(pack[1], packObj)
            # Used to insert the package data into hash table
            hash_package.insert(int(pack[0]), packObj)


# Creates instances of hash tables
hash_package = WgupsHashTable.WgupsHashTable()
address_hash = WgupsHashTable.WgupsHashTable()
packages_loaded(PACKAGE_CSV, hash_package)



# Class for main user interface
# BIG O- O(n)
class WgupsPackageSystem:
    def __init__(self):
        pass

    @staticmethod
    # Prints the welcome message to the user
    # BIG O- O(1)
    def print_welcome_message():
        print("**********************************************************\n"
              "***************WELCOME TO THE WGUPS SYSTEM!***************\n"
              "**********************************************************")

    @staticmethod
    # Prints the total mileage of the delivery route to the user (must be under 140)
    # BIG O- O(1)
    def print_total_mileage():
        print("The total mileage of the delivery route is: ",
              total_truck_distance, "miles. \n**********************************************************")

    @staticmethod
    # BIG O- O(n)
    def check_package_status():
        """Prompts the user to check the status of one or more packages.

        If the user chooses to check the status of one or more packages, they are prompted to enter
        the time they would like to check the status of the package(s). They are then prompted to enter
        whether they would like to check the status of one package or all packages. If the user chooses
        to check the status of one package, they are prompted to select if they would like to search by package ID
        number or by address then specific packages are displayed.. If users selects to check the status of all packages,
        the status of all packages is printed to the console.
        """
        text = input(
            "The WGUPS System allows you to search the status of deliveries for packages by time, ID, and address. \n"
            "Would you like to check package status? \n\n"
            "Type 'Y': Yes \n"
            "Type 'N': No  \n"
            "Enter choice: ")
        if text.lower() in ("yes", "y"):
            user_time = input(
                "\n**********************************************************\n"
                "WGUPS opens at 8AM. Please enter a time (format HH:MM) to check package status: \n")

            def convert_time(user_time):
                hours, minutes = user_time.split(":")
                return datetime.timedelta(hours=int(hours), minutes=int(minutes))

            convert_timedelta = convert_time(user_time)

            if convert_timedelta < datetime.timedelta(hours=8):
                print("WGUPS isn't open yet.")
            else:
                second_input = input("\n**********************************************************\n"
                                     "Status of one package or all packages? \n\n"
                                     "Type 'O': One package \n"
                                     "Type 'A': All packages \n")

                if second_input.lower() in ("one", "o"):
                    third_input = input("\n**********************************************************\n"
                                        "Would you like to check a single package by package ID or address? \n\n"
                                        "Type 'I': Package ID \n"
                                        "Type 'A': Address \n")

                    if third_input.lower() in ("a", "address"):
                        solo_input = input("\n**********************************************************\n"
                                           "Please enter street address exactly: ")
                        package = address_hash.search(solo_input)
                        status_of_package(package, convert_timedelta)
                        print(str(package))


                    elif third_input.lower() in ("i", "id"):
                        solo_input = input("\n**********************************************************\n"
                                           "Please enter package ID number: ")

                        package = hash_package.search(int(solo_input))
                        status_of_package(package, convert_timedelta)
                        print(
                            "%-15s%s\n"
                            "%-15s%s\n"
                            "%-15s%s\n"
                            "%-15s%s\n"
                            "%-15s%s\n"
                            "%-15s%s\n"
                            "%-15s%s\n"
                            "%-15s%s" % (
                                "Package ID:", package.package_id,
                                "Address:", package.package_address,
                                "City:", package.package_city,
                                "State:", package.package_state,
                                "Zip code:", package.package_zipcode,
                                "Deadline:", package.package_deadline_time,
                                "Weight:", package.package_weight,
                                "Status:", package.package_status
                            )
                        )
                    print("\n**********************************************************\n"
                          "Thank you for using the WGUPS System!")

                def print_package_status(packageID):
                    package = hash_package.search(packageID)
                    status_of_package(package, convert_timedelta)
                    print(str(package))

                if second_input.lower() in ("all", "a"):
                    for id_of_package in range(1, 41):
                        print_package_status(id_of_package)
                    print("\n**********************************************************\n"
                          "Thank you for using the WGUPS System!")
        else:
            print("\n**********************************************************\n"
                  "Thank you for using the WGUPS System!")
            exit()


# Determine and display package status
# BIG O- O(1)
def status_of_package(package, convert_timedelta):
    """Updates the status of the package.

    Arguments:
      package: An instance of the package.
      convert_timedelta: A datetime object representing the current time.

    """
    delivery_time = str(package.package_delivery_time)[:-3]
    if package.package_delivery_time > convert_timedelta:
        package.package_status = f"PACKAGE EN ROUTE - Expected delivery at: {delivery_time}"
    elif package.package_delivery_time < convert_timedelta:
        package.package_status = f"PACKAGE DELIVERED AT {delivery_time}"
    else:
        package.package_status = f"PACKAGE AT HUB - Expected delivery at: {delivery_time}"


# Trucks loading process
package_delivery(WgupsUtil.wgups_truck1)
package_delivery(WgupsUtil.wgups_truck2)
package_delivery(WgupsUtil.wgups_truck3)
total_truck_distance = WgupsUtil.wgups_truck3.truck_mileage + WgupsUtil.wgups_truck2.truck_mileage + \
                       WgupsUtil.wgups_truck1.truck_mileage