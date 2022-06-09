### write a script that resizes all images in a directory to 100 x 100 ###
import cv2
import glob


list_of_jpgs = glob.glob("batch_image_resizing/sample_images/*.jpg")

def trim_file_path(raw_path):
    return raw_path[35:]

trimmed_paths = list(map(trim_file_path, list_of_jpgs))

for index, image in enumerate(list_of_jpgs):
    print(index, image)
    cur_image = cv2.imread(image, 0)
    new_image = cv2.resize(cur_image, [100, 100])
    cv2.imwrite("batch_image_resizing/sample_images/resized_" + trimmed_paths[index], new_image)