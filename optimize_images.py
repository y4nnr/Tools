import os
from PIL import Image

def optimize_images(input_folder, output_folder, max_resolution=1080, quality=85):
    """
    Optimize all images in the input_folder by resizing and compressing them.
    The resizing maintains the aspect ratio, ensuring no distortion.

    Args:
        input_folder (str): Path to the folder containing raw images.
        output_folder (str): Path to save the optimized images.
        max_resolution (int): Maximum resolution for the longest side of the image.
        quality (int): Quality of the output images (1-100).
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                # Open the image
                with Image.open(input_path) as img:
                    # Convert to RGB if not already
                    img = img.convert("RGB")

                    # Get original dimensions
                    original_width, original_height = img.size

                    # Calculate new dimensions while maintaining aspect ratio
                    if max(original_width, original_height) > max_resolution:
                        if original_width > original_height:
                            scale_ratio = max_resolution / original_width
                        else:
                            scale_ratio = max_resolution / original_height

                        new_width = int(original_width * scale_ratio)
                        new_height = int(original_height * scale_ratio)
                        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                    # Save the optimized image
                    img.save(output_path, optimize=True, quality=quality)

                    print(f"Optimized: {filename} (Original: {original_width}x{original_height}, New: {img.size[0]}x{img.size[1]})")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print("All images have been optimized!")


# Specify the input and output folders
input_folder = "/Users/yann/Pictures/Shoes_DONE"  # Replace with the folder containing your raw images
output_folder = "/Users/yann/Pictures/Shoes_DONE/web_ready"  # Replace with the folder to save optimized images

# Run the optimization
optimize_images(input_folder, output_folder, max_resolution=1080, quality=85)
