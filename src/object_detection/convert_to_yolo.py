'''
train/images
train/labels
validation/images
validation/labels


datasets/images/train
datasets/images/validation
datasets/labels/train
datasets/labels/validation
'''

import os
import shutil

# Define source and destination directories
source_train_images = 'data/object_Detection/hard_workers/train/images'
source_train_labels = 'data/object_Detection/hard_workers/train/labels'
source_validation_images = 'data/object_Detection/hard_workers/validation/images'
source_validation_labels = 'data/object_Detection/hard_workers/validation/labels'

destination_images_train = 'data/object_Detection/hard_workers/datasets/images/train'
destination_images_validation = 'data/object_Detection/hard_workers/datasets/images/validation'
destination_labels_train = 'data/object_Detection/hard_workers/datasets/labels/train'
destination_labels_validation = 'data/object_Detection/hard_workers/datasets/labels/validation'

# Function to move files from source to destination
def move_files(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    files = os.listdir(source)
    for file_name in files:
        shutil.move(os.path.join(source, file_name), os.path.join(destination, file_name))

# Move train images
move_files(source_train_images, destination_images_train)

# Move validation images
move_files(source_validation_images, destination_images_validation)

# Move train labels
move_files(source_train_labels, destination_labels_train)

# Move validation labels
move_files(source_validation_labels, destination_labels_validation)
