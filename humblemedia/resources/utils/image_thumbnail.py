from PIL import Image


def get_image_thumbnail(input_file, output_file, size):
    image = Image.open(input_file)
    image.thumbnail(size)
    image.save(output_file, image.format)

    return True
