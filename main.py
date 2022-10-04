"""
Author: Emmy Nsabimana
"""

import os

input_test = input("Test filename input: ")

def generate_folder_structure(input_file):

    # extension checkup
    if not input_file.endswith('.raw'):
        raise ValueError("Invalid file extension. Please add file with .raw extension")

    output_directory = "output"
    sub_directories = ['extra', 'segmentation-12345', 'superresolution-1234']

    # Check root dir existance
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Create sub directories in the root folder.
    for sub_dir in sub_directories:
        if not os.path.exists(os.path.join(output_directory, sub_dir)):
            try:
                os.makedirs(os.path.join(output_directory, sub_dir))
            except OSError:
                print ("Path already exists")

    try:
        os.mknod(os.path.join(output_directory, "imageData.json"))
        os.mknod(os.path.join(output_directory, input_file))
    except OSError:
        print ("File already exists")

    # Generate files in the 'extra' directory 
    extra_dir_files = 'output.out'
    try:
        os.mknod(os.path.join(output_directory, "extra", extra_dir_files))
    except OSError:
        print ("File already exists")

    # Generate files in the 'segmentation' directory.
    segmentation_files = ['imageData.json', 'output.out']
    for file in segmentation_files:
        try:
            os.mknod(os.path.join(output_directory, "segmentation-12345", file))
        except OSError:
                print ("File already exists")

    # Generate files in the 'superresolution' directory.
    superresolution_files = ['imageData.json', 'output.out', 'progress.out', 'properties.json']
    for super_file in superresolution_files:
        try:
            os.mknod(os.path.join(output_directory, "superresolution-1234", super_file))
        except OSError:
                print ("File already exists")


if __name__ == '__main__':
    generate_folder_structure(input_file=input_test)
