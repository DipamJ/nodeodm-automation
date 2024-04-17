from PIL import Image
import os

input_directory = 'C:/Users/dipam/NodeODMProject/odm_data_aukerman-master/images'
output_directory = 'C:/Users/dipam/NodeODMProject/odm_data_aukerman-master/images_optimized'
resize_factor = 0.5  # Reduces the image size to 50%
quality_setting = 85  # JPEG quality setting

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(input_directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Add any other file types if needed
        basename, extension = os.path.splitext(filename)
        image_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, basename + '.jpg')  # Ensure the output is JPG

        with Image.open(image_path) as img:
            # Calculate new dimensions
            new_width = int(img.size[0] * resize_factor)
            new_height = int(img.size[1] * resize_factor)

            # Resize the image using high-quality downsampling filter
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # Save the image as JPG with compression
            img.save(output_path, 'JPEG', quality=quality_setting)

print("Optimization complete!")
