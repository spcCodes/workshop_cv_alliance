import os
import shutil
from sklearn.model_selection import train_test_split

def move_files(source_folder, files, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    for filename in files:
        src = os.path.join(source_folder, filename)
        dst = os.path.join(destination_folder, filename)
        shutil.move(src, dst)

# Define paths to your data folders
train_folder = 'data/object_Detection/hard_workers/train'
images_folder = os.path.join(train_folder, 'images')
labels_folder = os.path.join(train_folder, 'labels')

# Create new train and validation folders
new_train_folder = 'data/object_Detection/hard_workers/new_train'
new_val_folder = 'data/object_Detection/hard_workers/validation'

# Get list of image filenames
image_files = os.listdir(images_folder)

# Split data into train and validation sets (80% train, 20% validation)
train_files, val_files = train_test_split(image_files, test_size=0.2, random_state=42)

# Move images to new train folder
move_files(images_folder, train_files, os.path.join(new_train_folder, 'images'))

# Move labels to new train folder (if applicable)
move_files(labels_folder, [f.replace('.jpg', '.txt') for f in train_files], os.path.join(new_train_folder, 'labels'))

# Move images to new validation folder
move_files(images_folder, val_files, os.path.join(new_val_folder, 'images'))

# Move labels to new validation folder (if applicable)
move_files(labels_folder, [f.replace('.jpg', '.txt') for f in val_files], os.path.join(new_val_folder, 'labels'))
