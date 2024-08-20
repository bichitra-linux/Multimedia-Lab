from PIL import Image

def compress_png(input_path, output_path):
    """
    Compress an image using PNG format for lossless compression.

    :param input_path: Path to the input image file.
    :param output_path: Path to save the compressed image.
    """
    # Open an image file
    with Image.open(input_path) as img:
        # Ensure the image is in RGB mode
        img = img.convert("RGB")
        # Save the image in PNG format for lossless compression
        img.save(output_path, "PNG", optimize=True)

# Example usage
input_image_path = 'zoro.jpeg'
output_image_path = 'compressed-zoro.png'

# Compress the image using PNG format for lossless compression
compress_png(input_image_path, output_image_path)