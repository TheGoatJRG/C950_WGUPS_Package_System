"""
John Glick
001418867
C950- WGUPS Delivery System

WgupsMain.py
"""
# Needed imports
from WgupsPackageSystem import WgupsPackageSystem


# Main class
# Big O- O(n)
class Main(WgupsPackageSystem):
    """The main class of the WGUPS system.

    This class handles user input and displays the status of packages.
    """

    def __init__(self):
        """Initializes the main class."""
        # Prints the welcome message which includes total mileage (below 140)
        self.print_welcome_message()
        self.print_total_mileage()
        # Package status checker
        self.check_package_status()


if __name__ == "__main__":
    main = Main()
