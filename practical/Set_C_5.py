from PIL import Image

def compress_jpg(input_path, output_path, quality=20):
    """
    Compress a JPG image by reducing its quality.

    :param input_path: Path to the input image file.
    :param output_path: Path to save the compressed image.
    :param quality: Quality level for the compressed image (1 to 100).
    """
    # Open an image file
    with Image.open(input_path) as img:
        img = img.convert("RGB")
        img.save(output_path, "JPEG", quality=quality)

input_image_path = 'zoro.jpeg'
output_image_path = 'compressed-zoro.jpeg'

compress_jpg(input_image_path, output_image_path, quality=20)