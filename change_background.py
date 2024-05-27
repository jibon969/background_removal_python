from rembg import remove
from PIL import Image
import os

def change_background(input_image_path, background_image_path, output_image_path):
    try:
        # Open the input image and remove its background
        input_image = Image.open(input_image_path)
        print(f"Opened input image: {input_image.size}, {input_image.mode}")
        image_without_bg = remove(input_image)
        print("Background removal completed.")

        # Verify background removal by saving intermediate result
        intermediate_path = os.path.splitext(output_image_path)[0] + '_without_bg.png'
        image_without_bg.save(intermediate_path)
        print(f"Intermediate image without background saved to {intermediate_path}")

        # Open the new background image
        background_image = Image.open(background_image_path)
        print(f"Opened background image: {background_image.size}, {background_image.mode}")

        # Resize background to match the input image size
        background_image = background_image.resize(image_without_bg.size)

        # Paste the input image onto the background image
        background_image.paste(image_without_bg, (0, 0), image_without_bg)

        # Save the resulting image
        background_image.save(output_image_path)
        print(f"Image saved to {output_image_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_image_path = r'C:/Users/Jibon-Ahmed/Downloads/project/ahmed.png'          
background_image_path = r'C:/Users/Jibon-Ahmed/Downloads/project/ahmed.png'  
output_image_path = r'C:/Users/Jibon-Ahmed/Downloads/project/output.png'   

change_background(input_image_path, background_image_path, output_image_path)
