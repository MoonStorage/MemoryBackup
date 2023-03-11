# Libraries
import sys
from functions import *


# Classes
class Colors:
    END_C = "\033[0m"
    BLUE_C = "\033[94m"
    RED_C = "\033[91m"


# Constants
IS_UNIX = False

# Checks
sys_argv = sys.argv

if len(sys_argv) < 2:

    # Error
    print(Colors.RED_C + "ERROR: Please provide the source." + Colors.END_C)

else:

    # Location
    location = sys_argv[1].strip()

    # Clear terminal
    if IS_UNIX:
        os.system("clear")
    else:
        os.system("cls")

    # Destination
    with open("./destination.txt", "r") as file:
        destination = str(file.read())

        if destination[len(destination) - 1] == "/":
            destination = destination[:-1]

    # Initial print
    print(Colors.BLUE_C + "WELCOME!!!\n" + f"Source: {location}" + Colors.END_C + "\n")

    # Scan files
    scan(location, 0, destination)
