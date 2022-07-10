from cv2 import imread, imwrite, resize
from os import scandir, chdir

# Takes all of the jpeg images in the your desired directory (img_dir)
# Resizes them based off of img_type ("arial", or "ground")
# Stores them in your destination directory (dest_dir)

# Arial images - 750x750
# Ground images - 1232x224


def image_resize(img_dir, dest_dir, img_type):

    # Keeps track of naming
    count = 0

    # Loops through each file in the img_dir
    for imgfile in scandir(img_dir):

        # Checks if it is a jpeg type
        if imgfile.name.endswith(".JPEG") or imgfile.name.endswith(".jpeg") or imgfile.name.endswith(".jpg"):

            img = imread(imgfile.path)

            if img_type == "arial":

                arialResized = resize(img, (750, 750))
                filename = f"resized-arial{count}.jpg"
                chdir(dest_dir)
                imwrite(filename, arialResized)
                count += 1

            elif img_type == "ground":

                groundResized = resize(img, (1232, 224))
                filename = f"resized-ground{count}.jpg"
                chdir(dest_dir)
                imwrite(filename, groundResized)
                count += 1


image_path = r""  # Directory containing images
dest_path = r""  # Destination directory
img_type = ""  # "arial" or "ground"

image_resize(image_path, dest_path, img_type)
