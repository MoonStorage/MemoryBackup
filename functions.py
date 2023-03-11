# Libraries
import hashlib
import os
import imghdr
import pathlib
import random
from datetime import datetime
import string
import shutil
import ntpath


# Classes
class Colors:
    END_C = "\033[0m"
    GREEN_C = "\033[92m"


# Data
allowed_file_types = ["png", "gif", "jpg", "jpeg"]


# File scan
def scan(point, index_, destination):
    index = index_
    dirs = os.listdir(point)

    # Loop through each
    for item in dirs:
        item_name = point + "/" + item

        # File
        if not os.path.isdir(item_name):

            # Validate file type
            if imghdr.what(item_name) in allowed_file_types:
                index += 1
                process_file(item_name, index, destination)

        # Directory
        else:
            if not get_basename(item).startswith("."):
                scan(item_name, index, destination)


# Get basename
def get_basename(path: str):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


# Generate file hash
def generate_hash(path):

    # Variables
    buf_size = 65536
    sha512 = hashlib.sha512()

    # Read buffer
    with open(path, "rb") as file:

        while True:
            data = file.read(buf_size)
            if not data:
                break
            sha512.update(data)

    # Return hash
    return sha512.hexdigest()


# Is saved
def is_saved(file_hash: str, destination: str):
    map_destination = destination + "/map.txt"

    # Map file existence
    if os.path.exists(map_destination):
        hash_matched = False

        with open(map_destination, "r") as file:
            hashes = file.readlines()

            # Check every hash
            for each_hash in hashes:
                if each_hash.strip() != "" and file_hash == each_hash.strip():
                    hash_matched = True
                    break

            # Return status
            return hash_matched
    else:
        return False


# Store hash
def store_hash(file_hash: str, destination: str):
    map_destination = destination + "/map.txt"

    with open(map_destination, "a") as file:
        file.write("\n" + file_hash)


# Process file
def process_file(file, file_index, destination):

    # Saved directory
    saved_directory_title = "saved"
    saved_directory = destination + f"/{saved_directory_title}/"

    # Make saved directory if not there
    if not os.path.exists(saved_directory):
        os.mkdir(saved_directory)

    # Generate file hash
    file_hash = generate_hash(file)

    # Proceed is file is new
    if not is_saved(file_hash, destination):

        # Prepare new file data
        extension = pathlib.Path(file).suffix
        salt = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
        date_object = datetime.now()
        current_time = str(date_object.year) + str(date_object.month) + str(date_object.day) + str(
            date_object.hour) + str(date_object.minute) + str(date_object.second)
        new_file = saved_directory + current_time + salt + extension

        # Save file
        shutil.copyfile(file, new_file)

        # Store file hash
        store_hash(file_hash, destination)

        # Notify
        print(f"({file_index}) " + Colors.GREEN_C + f"SAVED: {file}" + Colors.END_C)

    else:
        print(f"({file_index}) " + "SKIPPED" + Colors.END_C)
